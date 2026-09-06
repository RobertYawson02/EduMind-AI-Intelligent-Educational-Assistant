"""Deterministic integration tests for the QA coordinator and Flask API."""

import unittest
from unittest.mock import patch

from app import app
from model.qa_engine import process_question


def local_results(question, topic, intent):
    return {
        "question": question,
        "topic": topic or "artificial intelligence",
        "intent": intent,
        "knowledge": (
            "Artificial intelligence enables computer systems to perform tasks "
            "that normally require human intelligence. It supports learning, "
            "reasoning, healthcare, education, and fraud detection."
        ),
        "akan": None,
        "web": None,
    }


class QaIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.router = patch("model.qa_engine.route_question", side_effect=local_results)
        self.save = patch("model.qa_engine.save_conversation")
        self.router.start()
        self.save.start()

    def tearDown(self):
        self.save.stop()
        self.router.stop()

    def test_supported_intents_return_an_answer(self):
        questions = [
            "What is artificial intelligence?", "What is the meaning of AI?",
            "What are the advantages of AI?", "What are the disadvantages of AI?",
            "What are the applications of AI?", "Give examples of AI.",
            "List AI uses.", "What causes AI bias?", "What are the effects of AI?",
            "Explain the process of machine learning.", "Compare AI and ML.",
            "Summarize artificial intelligence.", "Give an exam answer on AI.",
            "Explain artificial intelligence.", "Calculate 2 + 2.",
        ]
        for question in questions:
            with self.subTest(question=question):
                response = process_question(question)
                self.assertTrue(response["answer"])
                self.assertIn("confidence", response)
                self.assertTrue(response["sources"])

    @patch("model.qa_engine.resolve_topic", return_value="artificial intelligence")
    def test_follow_up_uses_resolved_topic(self, _resolve_topic):
        response = process_question("What are its applications?")
        self.assertEqual(response["topic"], "artificial intelligence")

    def test_empty_question_is_safe(self):
        response = process_question("   ")
        self.assertEqual(response["confidence"], 0.0)
        self.assertIn("Please enter", response["answer"])

    @patch("model.qa_engine.route_question", return_value={})
    def test_missing_retrieval_uses_fallback(self, _route):
        response = process_question("An unknown specialised topic")
        self.assertEqual(response["source"], "System fallback")

    def test_flask_response_contract(self):
        client = app.test_client()
        response = client.post("/ask", json={"question": "What is AI?"})
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        for field in ("answer", "intent", "topic", "language", "confidence", "source", "sources"):
            self.assertIn(field, body)

    def test_malformed_request_is_safe(self):
        client = app.test_client()
        response = client.post("/ask", data="not json", content_type="application/json")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
