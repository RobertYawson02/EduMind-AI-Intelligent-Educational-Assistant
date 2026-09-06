"""
Semantic Understanding Engine
Provides intelligent semantic matching using TF-IDF and word embeddings concepts.
Enables ChatGPT-like understanding of user intent and context.
"""

import re
import math
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SemanticUnderstanding:
    """Semantic understanding and matching engine."""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words='english',
            max_features=1000,
            ngram_range=(1, 2),
            strip_accents='unicode',
        )
        self.knowledge_vectors = None
        self.knowledge_texts = []
        self._fit_vectorizer()
    
    def _fit_vectorizer(self) -> None:
        """Initialize vectorizer with common educational terms."""
        common_texts = [
            "what is artificial intelligence machine learning deep learning",
            "how does computer work processor memory storage",
            "what is programming code algorithm data structure",
            "explain electricity power energy circuit",
            "what is biology cell organism evolution genetics",
            "what is history culture society civilization",
            "define mathematics algebra geometry calculus",
            "what is chemistry element atom molecule reaction",
            "what is physics motion force gravity",
            "what is database management system data",
        ]
        self.vectorizer.fit(common_texts)
    
    def vectorize_text(self, text: str) -> np.ndarray:
        """Convert text to TF-IDF vector."""
        if not text:
            return np.zeros((1, len(self.vectorizer.get_feature_names_out())))[0]
        return self.vectorizer.transform([text]).toarray()[0]
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity between two texts (0-1)."""
        if not text1 or not text2:
            return 0.0
        
        vec1 = self.vectorizer.transform([text1]).toarray()
        vec2 = self.vectorizer.transform([text2]).toarray()
        
        similarity = cosine_similarity(vec1, vec2)[0][0]
        return float(max(0.0, min(1.0, similarity)))  # Clamp to [0, 1]
    
    def find_similar_texts(
        self,
        query: str,
        candidates: List[str],
        threshold: float = 0.3,
        top_k: int = 5,
    ) -> List[Tuple[str, float]]:
        """Find most similar texts from candidates."""
        similarities = []
        
        for candidate in candidates:
            sim = self.calculate_similarity(query, candidate)
            if sim >= threshold:
                similarities.append((candidate, sim))
        
        # Sort by similarity descending
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:top_k]
    
    def extract_key_concepts(self, text: str, top_k: int = 5) -> List[str]:
        """Extract key concepts from text."""
        # Remove punctuation and split
        words = re.findall(r'\b[a-z]+\b', text.lower())
        
        # Common stop words to filter
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had',
            'do', 'does', 'did', 'what', 'which', 'who', 'when', 'where', 'why',
            'how', 'that', 'this', 'these', 'those', 'i', 'you', 'he', 'she',
        }
        
        concepts = [w for w in words if w not in stop_words and len(w) > 2]
        
        # Count frequencies
        freq = defaultdict(int)
        for c in concepts:
            freq[c] += 1
        
        # Return top concepts
        sorted_concepts = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [c[0] for c in sorted_concepts[:top_k]]
    
    def understand_intent_semantic(self, question: str) -> Dict[str, float]:
        """Understand intent using semantic patterns."""
        q_lower = question.lower()
        
        intent_patterns = {
            "definition": [
                "what is", "define", "meaning of", "what does",
                "explain", "describe", "clarify",
            ],
            "comparison": [
                "difference between", "compare", "vs", "versus",
                "better than", "same as", "different from",
            ],
            "process": [
                "how does", "how to", "step by step", "process",
                "procedure", "method", "way to",
            ],
            "cause_effect": [
                "why", "because", "cause", "effect", "result of",
                "leads to", "causes", "what happens",
            ],
            "example": [
                "example", "instance", "like", "such as",
                "for example", "e.g.", "case",
            ],
            "application": [
                "application", "use", "usage", "benefit", "advantage",
                "how is", "where is", "practical",
            ],
            "classification": [
                "type of", "kind of", "category", "class",
                "genre", "sort of", "what kind",
            ],
        }
        
        scores = {}
        
        for intent, patterns in intent_patterns.items():
            score = 0.0
            for pattern in patterns:
                if pattern in q_lower:
                    score += 1.0
            scores[intent] = score / len(patterns)
        
        return scores
    
    def understand_complexity_level(self, text: str) -> str:
        """Estimate the complexity level of a question."""
        # Heuristics:
        # Simple: basic terms, short sentences
        # Intermediate: technical terms, longer sentences
        # Advanced: complex terms, multiple clauses
        
        words = text.split()
        avg_word_length = sum(len(w) for w in words) / max(len(words), 1)
        
        technical_terms = {
            'algorithm', 'structure', 'framework', 'architecture',
            'mechanism', 'hypothesis', 'theorem', 'paradigm',
            'quantum', 'molecular', 'theoretical',
        }
        
        technical_count = sum(
            1 for w in words
            if w.lower() in technical_terms
        )
        
        complexity_score = (avg_word_length / 10.0) + (technical_count / len(words))
        
        if complexity_score < 1.0:
            return "beginner"
        elif complexity_score < 2.0:
            return "intermediate"
        else:
            return "advanced"
    
    def paraphrase_query(self, query: str) -> List[str]:
        """Generate alternative phrasings of a query."""
        paraphrases = [query]  # Include original
        
        # Pattern: "What is X?" -> "Define X", "Explain X"
        if query.lower().startswith("what is"):
            term = query[7:].strip().rstrip('?')
            paraphrases.append(f"Define {term}")
            paraphrases.append(f"Explain {term}")
        
        # Pattern: "How does X work?" -> "Explain how X works"
        if "how does" in query.lower() and "work" in query.lower():
            parts = re.split(r'how does|work', query, flags=re.IGNORECASE)
            if len(parts) >= 2:
                term = parts[1].strip().rstrip('?')
                paraphrases.append(f"Explain the workings of {term}")
        
        # Pattern: "Why is X?" -> "What causes X?", "X is caused by?"
        if query.lower().startswith("why is"):
            term = query[6:].strip().rstrip('?')
            paraphrases.append(f"What causes {term}?")
            paraphrases.append(f"Explain why {term}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique = []
        for p in paraphrases:
            if p.lower() not in seen:
                seen.add(p.lower())
                unique.append(p)
        
        return unique
    
    def calculate_answer_quality(
        self,
        question: str,
        answer: str,
        confidence: float,
    ) -> float:
        """Calculate overall quality score of an answer."""
        # Factors:
        # 1. Relevance to question (TF-IDF similarity)
        # 2. Answer length (too short is bad, too long might be bad)
        # 3. Model confidence
        
        relevance = self.calculate_similarity(question, answer)
        
        # Ideal answer length: 50-500 words
        words = len(answer.split())
        if words < 20:
            length_score = 0.5
        elif words < 50:
            length_score = 0.7
        elif words < 500:
            length_score = 1.0
        elif words < 1000:
            length_score = 0.9
        else:
            length_score = 0.7
        
        # Combined score (weighted)
        quality = (
            0.4 * relevance +     # 40% relevance
            0.3 * length_score +  # 30% appropriate length
            0.3 * confidence      # 30% model confidence
        )
        
        return float(max(0.0, min(1.0, quality)))


# Global instance
_semantic_engine: Optional[SemanticUnderstanding] = None


def get_semantic_engine() -> SemanticUnderstanding:
    """Get or create the semantic understanding engine."""
    global _semantic_engine
    if _semantic_engine is None:
        _semantic_engine = SemanticUnderstanding()
    return _semantic_engine


def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate semantic similarity between two texts."""
    engine = get_semantic_engine()
    return engine.calculate_similarity(text1, text2)


def find_similar(query: str, candidates: List[str], top_k: int = 5) -> List[Tuple[str, float]]:
    """Find most similar candidates to query."""
    engine = get_semantic_engine()
    return engine.find_similar_texts(query, candidates, top_k=top_k)


def extract_concepts(text: str, top_k: int = 5) -> List[str]:
    """Extract key concepts from text."""
    engine = get_semantic_engine()
    return engine.extract_key_concepts(text, top_k=top_k)


def understand_intent(question: str) -> Dict[str, float]:
    """Understand intent of a question."""
    engine = get_semantic_engine()
    return engine.understand_intent_semantic(question)


def get_complexity_level(text: str) -> str:
    """Get complexity level of text."""
    engine = get_semantic_engine()
    return engine.understand_complexity_level(text)
