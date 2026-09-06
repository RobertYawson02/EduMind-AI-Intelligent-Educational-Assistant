"""High-value deterministic tests for the final-year QA system.

Run from the project root:
    python -m unittest discover -s tests -p 'test*.py' -v
"""

import unittest
from unittest.mock import patch

from model.akan_engine import search_akan
from model.answer_synthesis_engine import synthesize_answer
from model.conversation_engine import clear_conversation, save_conversation, resolve_topic
from model.knowledge_engine import search_knowledge, knowledge_base
from model.ranking_engine import get_top_answers, ranking_confidence
from model.qa_engine import process_question


class FinalSystemTests(unittest.TestCase):
    def setUp(self):
        clear_conversation()

    def tearDown(self):
        clear_conversation()

    def test_knowledge_base_has_real_scope(self):
        self.assertGreaterEqual(len(knowledge_base), 100)
        self.assertIsNotNone(search_knowledge("What is machine learning?"))
        self.assertIsNotNone(search_knowledge("What is cybersecurity?"))
        self.assertIsNotNone(search_knowledge("What is DNS?"))

    def test_akan_translation(self):
        result, mode = search_akan("Translate water into Twi.")
        self.assertIsNotNone(result)
        self.assertEqual(mode, "english_to_twi")

    def test_ranking_uses_tfidf_and_returns_ordered_candidates(self):
        results = {
            "knowledge": "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence. Applications include healthcare, education, banking, transportation and customer service.",
            "web": [{"title": "AI applications", "body": "AI is used in healthcare, education, banking and transportation.", "href": "https://example.com/ai"}],
        }
        ranked = get_top_answers(results, "What are the applications of artificial intelligence?", "artificial intelligence", "applications", 2)
        self.assertGreaterEqual(len(ranked), 1)
        self.assertGreaterEqual(ranked[0]["score"], ranked[-1]["score"])
        self.assertGreaterEqual(ranking_confidence(ranked), 0.0)
        self.assertLessEqual(ranking_confidence(ranked), 1.0)

    def test_synthesis_is_intent_aware(self):
        ranked = [
            {"source": "knowledge", "score": 88, "answer": "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence. Applications include healthcare, education, banking and transportation."},
            {"source": "educational_web", "score": 72, "answer": "AI is used in healthcare, education, finance and transportation."},
        ]
        result = synthesize_answer("What are the applications of artificial intelligence?", "applications", "artificial intelligence", ranked)
        self.assertTrue(result["answer"])
        self.assertGreaterEqual(result["confidence"], 0.0)
        self.assertLessEqual(result["confidence"], 1.0)
        self.assertTrue(result["sources"])

    @patch("model.qa_engine.route_question")
    def test_end_to_end_uses_router_ranker_synthesizer(self, router):
        router.return_value = {
            "question": "What is artificial intelligence?",
            "topic": "artificial intelligence",
            "intent": "definition",
            "language": "english",
            "is_akan": False,
            "akan": None,
            "knowledge": "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence.",
            "ghana_qa": None,
            "web": None,
            "sources": ["Local Educational Knowledge Base"],
        }
        response = process_question("What is artificial intelligence?")
        self.assertTrue(response["answer"])
        self.assertEqual(response["intent"], "definition")
        self.assertEqual(response["topic"], "artificial intelligence")
        self.assertGreaterEqual(response["confidence"], 0.0)
        self.assertIn("source", response)

    def test_follow_up_context(self):
        save_conversation("What is artificial intelligence?", "artificial intelligence", "definition", "english")
        self.assertEqual(resolve_topic("What are its applications?"), "artificial intelligence")


if __name__ == "__main__":
    unittest.main()
