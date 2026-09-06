"""End-to-end runtime validation for the Intelligent Educational Assistant.

Run from the project root after activating the project's virtual environment:
    python scripts/runtime_validation.py
"""
from __future__ import annotations

import importlib
import os
import sys
import io

# Configure UTF-8 output for console
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def check(label, fn):
    try:
        result = fn()
        # Truncate result if it's too long or contains special characters
        result_str = str(result)
        if len(result_str) > 100:
            result_str = result_str[:97] + "..."
        print(f"PASS  {label}: {result_str}")
        return True
    except Exception as exc:
        print(f"FAIL  {label}: {type(exc).__name__}: {exc}")
        return False



def main():
    print("=" * 62)
    print("INTELLIGENT EDUCATIONAL ASSISTANT - RUNTIME VALIDATION")
    print("=" * 62)
    print("PROJECT ROOT:", ROOT)

    dependency_ok = True
    for name in ["flask", "pandas", "sklearn", "ddgs"]:
        dependency_ok &= check(f"dependency {name}", lambda n=name: importlib.import_module(n).__name__)

    checks = []
    checks.append(check("intent engine", lambda: f"intent={importlib.import_module('model.intent_engine').detect_intent('What are the applications of AI?')}"))
    checks.append(check("knowledge base", lambda: f"records={len(importlib.import_module('model.knowledge_engine').knowledge_base)}"))
    checks.append(check("Akan translation", lambda: importlib.import_module('model.akan_engine').format_akan_response(
        importlib.import_module('model.akan_engine').search_akan("Translate water into Twi.")[0],
        "english_to_twi",
        "Translate water into Twi.",
    )))
    checks.append(check("ranking engine", lambda: importlib.import_module('model.ranking_engine').get_top_answers({
        "knowledge": "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence.",
    }, "What is artificial intelligence?", "artificial intelligence", "definition", 1)[0]["score"]))

    def qa_check():
        qa = importlib.import_module("model.qa_engine")
        response = qa.process_question("What is artificial intelligence?")
        if not response.get("answer"):
            raise RuntimeError("QA pipeline returned an empty answer")
        return f"source={response.get('source')}, confidence={response.get('confidence')}"

    checks.append(check("QA pipeline", qa_check))

    def health_check():
        app_module = importlib.import_module("app")
        response = app_module.app.test_client().get("/health")
        if response.status_code != 200:
            raise RuntimeError(f"/health returned HTTP {response.status_code}")
        return f"HTTP {response.status_code}"

    checks.append(check("Flask /health", health_check))

    def api_check():
        app_module = importlib.import_module("app")
        response = app_module.app.test_client().post("/ask", json={"question": "What is artificial intelligence?"})
        if response.status_code != 200:
            raise RuntimeError(f"/ask returned HTTP {response.status_code}")
        body = response.get_json() or {}
        required_fields = {"answer", "intent", "topic", "language", "confidence", "source", "sources"}
        missing = required_fields.difference(body)
        if missing:
            raise RuntimeError(f"missing response fields: {sorted(missing)}")
        return f"HTTP {response.status_code}, intent={body['intent']}, confidence={body['confidence']}"

    checks.append(check("Flask /ask contract", api_check))

    print("=" * 62)
    passed = dependency_ok and all(checks)
    print(f"RESULT: {'PASS' if passed else 'FAIL'}")
    print("=" * 62)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
