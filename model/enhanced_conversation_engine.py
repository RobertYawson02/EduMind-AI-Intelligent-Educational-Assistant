"""
Enhanced Conversational AI Engine
Provides ChatGPT-like multi-turn dialogue with:
- Rich context awareness
- Intelligent topic tracking
- Multilingual support (English/Twi/Akan)
- Semantic understanding
- Answer refinement across turns
"""

import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

# Import components
from model.knowledge_engine import search_knowledge, format_knowledge
from model.akan_engine import search_akan, is_akan_related_question
from model.intent_engine import detect_intent, extract_topic
from model.ranking_engine import get_top_answers
from model.answer_synthesis_engine import synthesize_answer
from model.dataset_manager import load_processed_twi_dataset, dataset_available
from model.conversation_store import clear_turns, load_turns, save_turn


class ConversationContext:
    """Manages rich conversation context across multiple turns."""
    
    def __init__(self, max_history: int = 20):
        self.turns: List[Dict[str, Any]] = []
        self.topics_stack: List[str] = []
        self.entities_mentioned: set = set()
        self.language_preference: str = "english"
        self.max_history = max_history
    
    def add_turn(
        self,
        question: str,
        answer: str,
        intent: str,
        topic: str,
        language: str,
        confidence: float,
        sources: List[str],
    ) -> None:
        """Add a Q&A turn to conversation history."""
        turn = {
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "intent": intent,
            "topic": topic,
            "language": language,
            "confidence": confidence,
            "sources": sources,
        }
        self.turns.append(turn)
        
        # Trim history if needed
        if len(self.turns) > self.max_history:
            self.turns = self.turns[-self.max_history:]
        
        # Update topic stack
        if topic:
            if not self.topics_stack or self.topics_stack[-1] != topic:
                self.topics_stack.append(topic)
                if len(self.topics_stack) > 5:
                    self.topics_stack.pop(0)
    
    def get_recent_topic(self) -> Optional[str]:
        """Get the most recently discussed topic."""
        return self.topics_stack[-1] if self.topics_stack else None
    
    def get_conversation_summary(self) -> str:
        """Get a summary of the conversation so far."""
        if not self.turns:
            return ""
        
        topics_discussed = list(dict.fromkeys([t["topic"] for t in self.turns if t["topic"]]))
        intents = list(dict.fromkeys([t["intent"] for t in self.turns if t["intent"]]))
        
        summary = f"Topics: {', '.join(topics_discussed[:5])}"
        if intents:
            summary += f" | Intents: {', '.join(set(intents))}"
        
        return summary
    
    def get_context_window(self, depth: int = 3) -> List[Dict[str, Any]]:
        """Get the last N turns for context."""
        return self.turns[-depth:] if self.turns else []


class EnhancedQAEngine:
    """ChatGPT-like conversational QA engine."""
    
    def __init__(self, session_id: str = "default"):
        self.session_id = session_id or "default"
        self.context = ConversationContext()
        self._restore_context()
        self.akan_dataset = None
        self.twi_dataset = None
        self._load_datasets()

    def _restore_context(self) -> None:
        """Restore only this user's recent turns from durable storage."""
        for turn in load_turns(self.session_id):
            self.context.turns.append(turn)
            topic = turn.get("topic", "")
            if topic and (not self.context.topics_stack or self.context.topics_stack[-1] != topic):
                self.context.topics_stack.append(topic)
            if turn.get("language"):
                self.context.language_preference = turn["language"]
            self.context.entities_mentioned.update(
                re.findall(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b", turn.get("question", ""))
            )
        self.context.topics_stack = self.context.topics_stack[-5:]
    
    def _load_datasets(self) -> None:
        """Load Akan and Twi-English datasets."""
        if dataset_available("twi_english"):
            self.twi_dataset = load_processed_twi_dataset()
    
    def _extract_entities(self, text: str) -> set:
        """Extract named entities and key terms from text."""
        # Simple entity extraction - can be enhanced
        words = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', text)
        self.context.entities_mentioned.update(words)
        return set(words)
    
    def _resolve_pronouns(self, question: str) -> Tuple[str, str]:
        """
        Resolve pronouns to previous topics.
        e.g., "it" -> previous topic
        """
        resolved = question
        pronouns = {"it", "this", "that", "these", "those"}
        
        words = question.lower().split()
        recent_topic = self.context.get_recent_topic()
        
        if any(p in words for p in pronouns) and recent_topic:
            # Replace first pronoun with topic
            for pronoun in pronouns:
                if pronoun in words:
                    idx = words.index(pronoun)
                    words[idx] = recent_topic
                    resolved = " ".join(words)
                    break
        
        return resolved, recent_topic or ""
    
    def _find_related_turns(self, current_topic: str) -> List[Dict[str, Any]]:
        """Find related previous turns by topic."""
        return [
            turn for turn in self.context.turns
            if turn.get("topic") and turn["topic"].lower() in current_topic.lower()
        ]
    
    def _enhance_answer_with_context(
        self,
        answer: str,
        intent: str,
        topic: str,
        related_turns: List[Dict[str, Any]],
    ) -> str:
        """Enhance answer with contextual information from previous turns."""
        enhanced = answer
        
        if not related_turns:
            return enhanced
        
        # Add follow-up context
        if intent == "clarification":
            prev_answer = related_turns[-1].get("answer", "")
            if prev_answer:
                enhanced += f"\n\nBased on my previous explanation: {prev_answer[:100]}..."
        
        elif intent == "comparison":
            # Compare with previous topics
            if len(related_turns) > 1:
                enhanced += "\n\n(Compared to the previous topic)"
        
        return enhanced
    
    def process_conversational_question(
        self,
        question: str,
        force_language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Process a question with full conversational context.
        
        Returns:
            Dictionary with answer, metadata, and conversation state
        """
        
        # Reload so separate workers see the same session history.
        self.context = ConversationContext()
        self._restore_context()

        # Step 1: Resolve pronouns using conversation context
        resolved_question, fallback_topic = self._resolve_pronouns(question)
        
        # Step 2: Extract entities
        entities = self._extract_entities(question)
        
        # Step 3: Detect intent and language
        intent = detect_intent(resolved_question)
        topic = extract_topic(resolved_question) or fallback_topic
        language = force_language or self._detect_language(question)
        
        # Step 4: Check if this is follow-up to previous topic
        recent_topic = self.context.get_recent_topic()
        if not topic and recent_topic:
            topic = recent_topic
            is_followup = True
        else:
            is_followup = False
        
        # Step 5: Find related previous turns
        related_turns = self._find_related_turns(topic) if topic else []
        
        # Step 6: Route to appropriate engine based on language
        answer = ""
        sources = []
        confidence = 0.0
        
        if language == "akan" or is_akan_related_question(question):
            # Route to Akan/Twi engine
            akan_result, mode = search_akan(question)
            if akan_result:
                from model.akan_engine import format_akan_response
                answer = format_akan_response(akan_result, mode, question)
                sources = ["Akan/Twi Lexical Knowledge Base"]
                confidence = 0.95
        
        if not answer:
            # Route to knowledge engine
            knowledge = search_knowledge(resolved_question or question)
            if knowledge:
                answer = format_knowledge(knowledge)
                sources = ["Local Educational Knowledge Base"]
                confidence = knowledge.get("retrieval_score", 0.75)
        
        # Step 7: Enhance answer with context
        if answer:
            answer = self._enhance_answer_with_context(answer, intent, topic or "", related_turns)
        
        # Step 8: Add follow-up suggestions based on conversation
        follow_up_suggestions = self._generate_follow_ups(topic, intent, answer)
        
        # Step 9: Create response
        response = {
            "answer": answer,
            "intent": intent,
            "topic": topic or "general",
            "language": language,
            "confidence": confidence,
            "sources": sources,
            "is_followup": is_followup,
            "entities_mentioned": list(entities),
            "follow_up_questions": follow_up_suggestions,
            "conversation_context": self.context.get_conversation_summary(),
        }
        
        # Step 10: Store in conversation history
        self.context.add_turn(
            question=question,
            answer=answer,
            intent=intent,
            topic=topic or "general",
            language=language,
            confidence=confidence,
            sources=sources,
        )
        save_turn(self.session_id, self.context.turns[-1])
        
        return response
    
    def _detect_language(self, text: str) -> str:
        """Detect language of text."""
        if is_akan_related_question(text):
            return "akan"
        return "english"
    
    def _generate_follow_ups(self, topic: str, intent: str, answer: str) -> List[str]:
        """Generate intelligent follow-up questions."""
        follow_ups = []
        
        if not topic:
            return follow_ups
        
        if intent == "definition":
            follow_ups = [
                f"What are the applications of {topic}?",
                f"How does {topic} work?",
                f"Can you give examples of {topic}?",
            ]
        elif intent == "comparison":
            follow_ups = [
                f"What are the key differences?",
                f"Which is better for...?",
            ]
        elif intent == "explanation":
            follow_ups = [
                f"Can you provide more details about {topic}?",
                f"What are the benefits of {topic}?",
            ]
        else:
            follow_ups = [
                f"Tell me more about {topic}",
                f"What else should I know about {topic}?",
            ]
        
        return follow_ups[:3]  # Return top 3
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get full conversation history."""
        return self.context.turns
    
    def clear_conversation(self) -> None:
        """Clear conversation history."""
        clear_turns(self.session_id)
        self.context = ConversationContext()
    
    def get_conversation_stats(self) -> Dict[str, Any]:
        """Get statistics about the conversation."""
        turns = self.context.turns
        return {
            "total_turns": len(turns),
            "unique_topics": len(set(t.get("topic") for t in turns)),
            "average_confidence": (
                sum(t.get("confidence", 0) for t in turns) / len(turns)
                if turns
                else 0
            ),
            "languages_used": list(set(t.get("language") for t in turns)),
            "intents_used": list(set(t.get("intent") for t in turns)),
            "entities_mentioned": list(self.context.entities_mentioned),
        }


# Per-process cache; durable storage remains the source of truth.
_enhanced_qa_engines: Dict[str, EnhancedQAEngine] = {}


def get_enhanced_qa_engine(session_id: str = "default") -> EnhancedQAEngine:
    """Get or create the enhanced QA engine."""
    key = session_id or "default"
    if key not in _enhanced_qa_engines:
        _enhanced_qa_engines[key] = EnhancedQAEngine(key)
    return _enhanced_qa_engines[key]


def process_question_with_context(question: str, session_id: str = "default") -> Dict[str, Any]:
    """Process a question with full conversational context."""
    engine = get_enhanced_qa_engine(session_id)
    return engine.process_conversational_question(question)


def get_conversation_history(session_id: str = "default") -> List[Dict[str, Any]]:
    """Get the conversation history."""
    engine = get_enhanced_qa_engine(session_id)
    return engine.get_conversation_history()


def clear_enhanced_conversation(session_id: str = "default") -> None:
    """Clear the enhanced conversation context."""
    engine = get_enhanced_qa_engine(session_id)
    engine.clear_conversation()


def get_conversation_stats(session_id: str = "default") -> Dict[str, Any]:
    """Get conversation statistics."""
    engine = get_enhanced_qa_engine(session_id)
    return engine.get_conversation_stats()
