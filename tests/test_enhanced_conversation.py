"""
Enhanced Conversation System Tests
Tests for ChatGPT-like conversational AI features
"""

import unittest
from model.enhanced_conversation_engine import (
    EnhancedQAEngine,
    ConversationContext,
    process_question_with_context,
    get_conversation_history,
    get_conversation_stats,
    clear_enhanced_conversation,
)
from model.semantic_engine import (
    calculate_similarity,
    find_similar,
    extract_concepts,
    understand_intent,
    get_complexity_level,
)


class ConversationContextTests(unittest.TestCase):
    """Test conversation context management."""
    
    def setUp(self):
        self.context = ConversationContext()
    
    def test_add_turn(self):
        """Test adding a conversation turn."""
        self.context.add_turn(
            question="What is AI?",
            answer="AI is artificial intelligence.",
            intent="definition",
            topic="artificial intelligence",
            language="english",
            confidence=0.9,
            sources=["Knowledge Base"]
        )
        self.assertEqual(len(self.context.turns), 1)
        self.assertEqual(self.context.turns[0]["topic"], "artificial intelligence")
    
    def test_topic_stack(self):
        """Test topic stack management."""
        self.context.add_turn("Q1", "A1", "definition", "AI", "english", 0.9, [])
        self.context.add_turn("Q2", "A2", "explanation", "machine learning", "english", 0.9, [])
        self.context.add_turn("Q3", "A3", "comparison", "deep learning", "english", 0.9, [])
        
        self.assertEqual(self.context.get_recent_topic(), "deep learning")
        self.assertEqual(len(self.context.topics_stack), 3)
    
    def test_conversation_summary(self):
        """Test conversation summary generation."""
        self.context.add_turn("Q1", "A1", "definition", "AI", "english", 0.9, [])
        self.context.add_turn("Q2", "A2", "explanation", "machine learning", "english", 0.9, [])
        
        summary = self.context.get_conversation_summary()
        self.assertIn("AI", summary)
        self.assertIn("machine learning", summary)
    
    def test_context_window(self):
        """Test context window retrieval."""
        for i in range(5):
            self.context.add_turn(f"Q{i}", f"A{i}", "definition", f"topic{i}", "english", 0.9, [])
        
        window = self.context.get_context_window(depth=3)
        self.assertEqual(len(window), 3)
        self.assertEqual(window[-1]["question"], "Q4")


class EnhancedQAEngineTests(unittest.TestCase):
    """Test enhanced QA engine."""
    
    def setUp(self):
        self.engine = EnhancedQAEngine()
        self.engine.clear_conversation()
    
    def test_resolve_pronouns(self):
        """Test pronoun resolution."""
        # Add context first
        self.engine.context.add_turn(
            "What is AI?", "AI is...", "definition", "artificial intelligence", "english", 0.9, []
        )
        
        resolved, fallback = self.engine._resolve_pronouns("What are its applications?")
        # Should have fallback topic if pronouns couldn't be resolved explicitly
        self.assertIsNotNone(fallback)
    
    def test_entity_extraction(self):
        """Test entity extraction."""
        entities = self.engine._extract_entities("What is Machine Learning and AI?")
        # Should extract at least some entities
        self.assertIsInstance(entities, set)
    
    def test_process_question_with_context(self):
        """Test processing question with context."""
        response = self.engine.process_conversational_question("What is artificial intelligence?")
        
        self.assertIn("answer", response)
        self.assertIn("intent", response)
        self.assertIn("topic", response)
        self.assertIn("confidence", response)
        self.assertIn("follow_up_questions", response)
    
    def test_follow_up_questions_generation(self):
        """Test follow-up question generation."""
        follow_ups = self.engine._generate_follow_ups("machine learning", "definition", "ML is...")
        self.assertIsInstance(follow_ups, list)
        self.assertGreater(len(follow_ups), 0)
        self.assertLessEqual(len(follow_ups), 3)
    
    def test_conversation_history_accumulation(self):
        """Test that conversation history accumulates."""
        q1 = self.engine.process_conversational_question("What is AI?")
        q2 = self.engine.process_conversational_question("How does it work?")
        
        history = self.engine.get_conversation_history()
        self.assertEqual(len(history), 2)
    
    def test_conversation_stats(self):
        """Test conversation statistics."""
        self.engine.process_conversational_question("What is AI?")
        self.engine.process_conversational_question("What about machine learning?")
        
        stats = self.engine.get_conversation_stats()
        self.assertIn("total_turns", stats)
        self.assertIn("unique_topics", stats)
        self.assertEqual(stats["total_turns"], 2)


class SemanticEngineTests(unittest.TestCase):
    """Test semantic understanding engine."""
    
    def test_similarity_calculation(self):
        """Test text similarity calculation."""
        sim = calculate_similarity("What is AI?", "Define artificial intelligence")
        # Similarity should be a float between 0 and 1
        self.assertIsInstance(sim, float)
        self.assertGreaterEqual(sim, 0.0)
        self.assertLessEqual(sim, 1.0)
    
    def test_similarity_exact_match(self):
        """Test similarity of identical texts."""
        sim = calculate_similarity("machine learning", "machine learning")
        self.assertGreater(sim, 0.8)  # Should be very similar
    
    def test_similarity_no_match(self):
        """Test similarity of unrelated texts."""
        sim = calculate_similarity("machine learning", "cooking recipe")
        self.assertLess(sim, 0.5)  # Should be fairly different
    
    def test_find_similar_texts(self):
        """Test finding similar candidates."""
        candidates = [
            "Artificial intelligence is a branch of computer science",
            "Machine learning is a subset of AI",
            "Pizza is an Italian dish",
            "Deep learning uses neural networks",
        ]
        
        similar = find_similar("What is machine learning?", candidates)
        self.assertGreater(len(similar), 0)
        # First result should be about machine learning or AI, not pizza
        self.assertNotIn("Pizza", similar[0][0])
    
    def test_concept_extraction(self):
        """Test key concept extraction."""
        concepts = extract_concepts("What are the applications of artificial intelligence in healthcare?")
        self.assertIsInstance(concepts, list)
        self.assertGreater(len(concepts), 0)
    
    def test_intent_understanding(self):
        """Test intent understanding."""
        # Definition intent
        intent_scores = understand_intent("What is machine learning?")
        self.assertIn("definition", intent_scores)
        
        # Comparison intent
        intent_scores = understand_intent("Compare machine learning and deep learning")
        self.assertIn("comparison", intent_scores)
        
        # Process intent
        intent_scores = understand_intent("How does neural network training work?")
        self.assertIn("process", intent_scores)
    
    def test_complexity_levels(self):
        """Test complexity level detection."""
        simple = get_complexity_level("What is AI?")
        self.assertIn(simple, ["beginner", "intermediate"])  # Short questions are usually beginner or intermediate
        
        complex_text = get_complexity_level("Explain the backpropagation algorithm in convolutional neural networks for computer vision")
        self.assertIsInstance(complex_text, str)
    
    def test_answer_quality_calculation(self):
        """Test answer quality scoring."""
        from model.semantic_engine import get_semantic_engine
        engine = get_semantic_engine()
        
        quality = engine.calculate_answer_quality(
            "What is artificial intelligence?",
            "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence.",
            0.85
        )
        
        self.assertGreater(quality, 0.5)
        self.assertLessEqual(quality, 1.0)


class IntegrationTests(unittest.TestCase):
    """Integration tests for enhanced conversation system."""
    
    def setUp(self):
        clear_enhanced_conversation()
    
    def test_multi_turn_conversation(self):
        """Test a multi-turn conversation."""
        # Turn 1: Definition
        r1 = process_question_with_context("What is machine learning?")
        self.assertIn("answer", r1)
        self.assertTrue(len(r1.get("answer", "")) > 0)
        
        # Turn 2: Follow-up (should use context)
        r2 = process_question_with_context("How does it work?")
        self.assertIn("answer", r2)
        self.assertTrue(len(r2.get("answer", "")) > 0)
        
        # Check history
        history = get_conversation_history()
        self.assertGreaterEqual(len(history), 2)
    
    def test_conversation_with_language_mix(self):
        """Test conversation with mixed languages."""
        r1 = process_question_with_context("What is water?")
        self.assertIsNotNone(r1.get("answer"))
        
        r2 = process_question_with_context("Translate water into Twi")
        self.assertIsNotNone(r2.get("answer"))
    
    def test_conversation_stats_accumulation(self):
        """Test that stats accumulate correctly."""
        process_question_with_context("What is AI?")
        process_question_with_context("What about ML?")
        process_question_with_context("What is deep learning?")
        
        stats = get_conversation_stats()
        self.assertEqual(stats["total_turns"], 3)
        self.assertGreater(stats["unique_topics"], 0)


if __name__ == "__main__":
    unittest.main()
