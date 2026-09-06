# ==========================================================
# QA ENGINE
# Main Intelligent Assistant Controller
# ==========================================================

from model.intent_engine import (
    detect_intent,
    extract_topic
)

from model.response_engine import (
    create_response
)

from model.conversation_engine import (
    save_conversation,
    resolve_topic
)

from model.router_engine import (
    route_question
)

from model.ranking_engine import (
    combine_ranked_answers
)

from model.ranking_engine import get_top_answers
from model.answer_synthesis_engine import synthesize_answer

import contextlib
import io
import re


# ==========================================================
# LANGUAGE DETECTION
# ==========================================================

def detect_language(question):
    """
    Detect whether the user's question is in
    English or Akan/Twi.
    """

    if not question:
        return "english"

    q = question.lower().strip()

    # ------------------------------------------------------
    # Detect Akan special characters
    # ------------------------------------------------------

    if "ɔ" in q or "ɛ" in q:
        return "akan"

    # ------------------------------------------------------
    # Common Akan words and expressions
    # ------------------------------------------------------

    akan_words = [
        "nsuo",
        "ɔdɔ",
        "meda ase",
        "maakye",
        "maaha",
        "maadwo",
        "akwaaba",
        "nante yie",
        "wo ho te sɛn",
        "me ho yɛ",
        "yɛn",
        "asɛm",
        "sukuu",
        "akan",
        "twi"
    ]

    words = q.split()

    score = 0

    for phrase in akan_words:

        # Multi-word Akan expression
        if " " in phrase:

            if phrase in q:
                score += 2

        # Single Akan word
        else:

            if phrase in words:
                score += 1

    if score >= 1:
        return "akan"

    return "english"


# ==========================================================
# MAIN QUESTION ANSWERING PROCESS
# ==========================================================

def _legacy_get_answer(question):
    """
    Main question-answering pipeline.

    Flow:

        User Question
              ↓
        Language Detection
              ↓
        Intent Detection
              ↓
        Topic Extraction
              ↓
        Conversation Memory
              ↓
        Router Engine
              ↓
        Knowledge Engines
              ↓
        Ranking Engine
              ↓
        Response Engine
              ↓
        Final Answer
    """

    # ------------------------------------------------------
    # Validate question
    # ------------------------------------------------------

    if not question or not str(question).strip():

        return (
            create_response(
                answer="Please enter a question.",
                source="⚠️ System",
                intent="general",
                language="english"
            ),
            "⚠️ Empty Question"
        )

    question = str(question).strip()

    print("\n===================================")
    print("USER:", question)

    # ======================================================
    # 1. LANGUAGE DETECTION
    # ======================================================

    language = detect_language(
        question
    )

    # ======================================================
    # 2. INTENT DETECTION
    # ======================================================

    intent = detect_intent(
        question
    )

    # ======================================================
    # 3. TOPIC EXTRACTION
    # ======================================================

    topic = extract_topic(
        question
    )

    # ======================================================
    # 4. CONVERSATION MEMORY
    # ======================================================

    previous_topic = resolve_topic(
        question
    )

    if previous_topic:

        print(
            "💬 Previous Topic:",
            previous_topic
        )

        topic = previous_topic

    # ======================================================
    # DISPLAY ANALYSIS
    # ======================================================

    print(
        "Language:",
        language
    )

    print(
        "Intent:",
        intent
    )

    print(
        "Topic:",
        topic
    )

    # ======================================================
    # 5. ROUTER ENGINE
    #
    # The current router_engine.py defines:
    #
    #     route_question(question, topic=None)
    #
    # Therefore, we pass only:
    #
    #     question
    #     topic
    #
    # Intent is already detected here and can be used by
    # the ranking/response stages.
    # ======================================================

    try:

        results = route_question(
            question,
            topic
        )

    except Exception as e:

        print(
            "⚠️ Router Engine Error:",
            e
        )

        results = None

    # ======================================================
    # DISPLAY ENGINE RESULTS
    # ======================================================

    if results:

        print(
            "Engine Results:",
            results.keys()
        )

    else:

        print(
            "Engine Results: None"
        )

    # ======================================================
    # 6. RANKING ENGINE
    #
    # The ranking engine receives:
    #
    #     results
    #     original question
    #
    # This allows it to evaluate:
    #
    #     - Question relevance
    #     - Examination relevance
    #     - Educational relevance
    #     - Answer quality
    #     - Conciseness
    #     - Source quality
    # ======================================================

    final_answer = combine_ranked_answers(
        results,
        question
    )

    # ======================================================
    # 7. SAVE CONVERSATION
    # ======================================================

    save_conversation(
        question,
        topic,
        intent,
        language
    )

    # ======================================================
    # 8. RESPONSE GENERATION
    # ======================================================

    if final_answer:

        return (
            create_response(
                answer=final_answer,
                source="🧠 Ranked Multi-Engine Assistant",
                intent=intent,
                language=language
            ),
            "🧠 Intelligent Router"
        )

    # ======================================================
    # NO ANSWER
    # ======================================================

    return (
        create_response(
            answer=(
                "Sorry, I could not find enough "
                "reliable information to answer "
                "your question."
            ),
            source="⚠️ System",
            intent=intent,
            language=language
        ),
        "⚠️ No Answer"
    )


# ==========================================================
# INTEGRATED QA PIPELINE
# ==========================================================

def _source_label(source):
    labels = {
        "knowledge": "Local Educational Knowledge Base",
        "akan": "Akan / Twi Lexical Knowledge Base",
        "ghana_qa": "Ghana-QA Dataset",
        "ghana_qa_sample": "Curated Ghanaian QA Sample",
        "web": "Web source",
        "educational_web": "Educational web source",
    }
    return labels.get(
        source,
        str(source or "Unknown source").replace("_", " ").title(),
    )


def process_question(question):
    """Coordinate language, intent, context, retrieval, ranking, and synthesis."""
    question = str(question or "").strip()

    if not question:
        return {
            "answer": "Please enter a question.",
            "intent": "general",
            "topic": "",
            "language": "unknown",
            "confidence": 0.0,
            "source": "System",
            "sources": [],
        }

    language = detect_language(question)
    intent = detect_intent(question)

    # Conversational greetings should not trigger retrieval or web search.
    normalized_conversation = re.sub(r"[^a-z0-9\s]", "", question.lower()).strip()

    if intent == "general" and normalized_conversation in {
        "hello", "hi", "hey", "good morning", "good afternoon",
        "good evening", "good night", "how are you",
    }:
        answer = "Hello! I’m your Intelligent Educational Assistant. How can I help you with your studies today?"
        try:
            save_conversation(question, "", intent, language)
        except Exception:
            pass
        return {
            "answer": answer,
            "intent": intent,
            "topic": "",
            "language": language,
            "confidence": 1.0,
            "source": "Conversation",
            "sources": ["Conversation"],
        }
    topic = resolve_topic(question) or extract_topic(question)

    try:
        # Older engines contain useful interactive diagnostic output, including
        # emoji.  On Windows consoles configured with cp1252 that output can
        # raise UnicodeEncodeError and incorrectly make retrieval look like it
        # failed.  The coordinator is a programmatic API, so keep that output
        # out of stdout while preserving the engines' normal behaviour.
        with contextlib.redirect_stdout(io.StringIO()):
            results = route_question(question, topic, intent)
        topic = results.get("topic") or topic
        ranked_answers = get_top_answers(
            results,
            question=question,
            topic=topic,
            intent=intent,
            limit=3,
        )
    except Exception:
        ranked_answers = []

    if not ranked_answers:
        response = {
            "answer": (
                "I could not find enough reliable information to answer that "
                "question. Please rephrase it or provide a more specific topic."
            ),
            "intent": intent,
            "topic": topic,
            "language": language,
            "confidence": 0.0,
            "source": "System fallback",
            "sources": [],
        }
    else:
        synthesis = synthesize_answer(
            question=question,
            intent=intent,
            topic=topic,
            ranked_answers=ranked_answers,
            language=language,
        )
        answer = synthesis.get("answer")

        # A lexical translation is already a precise, structured answer.  It
        # must win over a general local-knowledge match for the same word.
        if intent == "translation":
            akan_candidate = next(
                (item for item in ranked_answers if item.get("source") == "akan"),
                None,
            )
            if akan_candidate:
                answer = akan_candidate.get("answer")
                ranked_answers = [akan_candidate] + [
                    item for item in ranked_answers if item is not akan_candidate
                ]

        source_names = []
        for candidate in ranked_answers:
            label = _source_label(candidate.get("source"))
            if label not in source_names:
                source_names.append(label)

        response = {
            "answer": answer or ranked_answers[0].get("answer"),
            "intent": intent,
            "topic": topic,
            "language": language,
            "confidence": synthesis.get("confidence", 0.0),
            "source": source_names[0] if source_names else "Unknown source",
            "sources": source_names,
        }

    try:
        save_conversation(question, topic, intent, language)
    except Exception:
        pass

    return response


def get_answer(question):
    """Backward-compatible tuple API for existing callers."""
    response = process_question(question)
    return response["answer"], response["source"]


# ==========================================================
# END OF QA ENGINE
# ==========================================================
# ==========================================================
# END-TO-END QA ENGINE TEST
# ==========================================================

def test_qa_engine():

    test_questions = [

        "What is artificial intelligence?",

        "What is machine learning?",

        "What is Flask?",

        "What is Python?",

        "What does nsuo mean?",

        "Translate water into Twi.",

        "What are the applications of artificial intelligence?",

        "Hello",

        "How are you?"

    ]

    print("\n")
    print("==========================================================")
    print("🧠 QA ENGINE END-TO-END TEST")
    print("==========================================================")

    for question in test_questions:

        print("\n")
        print("----------------------------------------------------------")
        print("QUESTION:", question)
        print("----------------------------------------------------------")

        try:

            answer, source = get_answer(
                question
            )

            print("\nSOURCE:")
            print(source)

            print("\nANSWER:")
            print(answer)

        except Exception as e:

            print("\n❌ QA ENGINE ERROR:")
            print(e)


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_qa_engine()
