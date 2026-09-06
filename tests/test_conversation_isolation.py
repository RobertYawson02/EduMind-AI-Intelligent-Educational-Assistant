import unittest

from app import app


class ConversationIsolationTests(unittest.TestCase):
    def test_browser_sessions_have_separate_histories(self):
        first = app.test_client()
        second = app.test_client()

        response = first.post(
            "/chat",
            json={"question": "What is artificial intelligence?"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(second.get("/conversation-history").get_json()["count"], 0)
        self.assertEqual(first.get("/conversation-history").get_json()["count"], 1)

        first.post("/clear-context")
        self.assertEqual(first.get("/conversation-history").get_json()["count"], 0)
        self.assertEqual(second.get("/conversation-history").get_json()["count"], 0)


if __name__ == "__main__":
    unittest.main()