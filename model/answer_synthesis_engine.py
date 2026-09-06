# ==========================================================
#
# ANSWER SYNTHESIS ENGINE
#
# Intelligent Educational Answer Construction System
#
# ==========================================================
#
# Responsibilities:
#
# 1. Receive ranked answers from the Ranking Engine.
# 2. Extract useful evidence from strong answers.
# 3. Remove repetitive information.
# 4. Preserve important information.
# 5. Adapt the response to the detected intent.
# 6. Produce a coherent educational answer.
# 7. Estimate synthesis confidence.
# 8. Provide a safe fallback when evidence is weak.
#
# Designed to work with:
#
#     Intent Engine
#            ↓
#     Conversation Engine
#            ↓
#     Retrieval Engines
#            ↓
#     Ranking Engine
#            ↓
#     Answer Synthesis Engine
#            ↓
#     Final Response
#
# ==========================================================

import re
from collections import Counter

# ==========================================================
# OPTIONAL TF-IDF / COSINE SIMILARITY
# ==========================================================

try:

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    TFIDF_AVAILABLE = True

except ImportError:

    TFIDF_AVAILABLE = False

    print(
        "⚠️ scikit-learn is not available."
    )

    print(
        "⚠️ Sentence similarity fallback will be used."
    )


# ==========================================================
# CONFIGURATION
# ==========================================================

MAX_EVIDENCE_ITEMS = 5

MAX_SENTENCES = 8

SIMILARITY_THRESHOLD = 0.72

MIN_CONFIDENCE = 0.35

HIGH_CONFIDENCE = 0.75


# ==========================================================
# INTENTS THAT BENEFIT FROM LIST STRUCTURE
# ==========================================================

LIST_INTENTS = {

    "advantages",
    "disadvantages",
    "applications",
    "examples",
    "list",
    "causes",
    "effects",
    "process",
    "exam",

}


# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_text(text):
    """
    Clean and normalize text.
    """

    if text is None:

        return ""

    text = str(text)

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==========================================================
# NORMALIZE SENTENCE
# ==========================================================

def normalize_sentence(sentence):
    """
    Normalize a sentence for comparison.
    """

    sentence = clean_text(
        sentence
    )

    sentence = sentence.lower()

    sentence = re.sub(
        r"[^\w\s]",
        "",
        sentence
    )

    return sentence.strip()


# ==========================================================
# SPLIT SENTENCES
# ==========================================================

def split_sentences(text):
    """
    Split text into reasonably clean sentences.
    """

    text = clean_text(
        text
    )

    if not text:

        return []

    # ------------------------------------------------------
    # Handle common educational separators.
    # ------------------------------------------------------

    text = re.sub(
        r"\s*[\r\n]+\s*",
        ". ",
        text
    )

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    cleaned = []

    for sentence in sentences:

        sentence = clean_text(
            sentence
        )

        if not sentence:

            continue

        if len(sentence) < 8:

            continue

        cleaned.append(
            sentence
        )

    return cleaned


# ==========================================================
# FALLBACK WORD SIMILARITY
# ==========================================================

def word_similarity(text_a, text_b):
    """
    Calculates simple Jaccard word similarity.

    Used when scikit-learn is unavailable.
    """

    a = set(
        normalize_sentence(text_a).split()
    )

    b = set(
        normalize_sentence(text_b).split()
    )

    if not a or not b:

        return 0.0

    intersection = len(
        a.intersection(b)
    )

    union = len(
        a.union(b)
    )

    if union == 0:

        return 0.0

    return intersection / union


# ==========================================================
# SENTENCE SIMILARITY
# ==========================================================

def calculate_sentence_similarity(
    sentence_a,
    sentence_b
):
    """
    Calculate semantic similarity between
    two sentences using TF-IDF/cosine similarity.

    Falls back to word similarity when
    scikit-learn is unavailable.
    """

    sentence_a = clean_text(
        sentence_a
    )

    sentence_b = clean_text(
        sentence_b
    )

    if not sentence_a or not sentence_b:

        return 0.0

    if (
        normalize_sentence(sentence_a)
        ==
        normalize_sentence(sentence_b)
    ):

        return 1.0

    # ------------------------------------------------------
    # TF-IDF similarity
    # ------------------------------------------------------

    if TFIDF_AVAILABLE:

        try:

            vectorizer = TfidfVectorizer(
                lowercase=True,
                stop_words="english"
            )

            matrix = vectorizer.fit_transform(
                [
                    sentence_a,
                    sentence_b
                ]
            )

            similarity = cosine_similarity(
                matrix[0:1],
                matrix[1:2]
            )[0][0]

            return float(
                similarity
            )

        except Exception:

            pass

    # ------------------------------------------------------
    # Fallback
    # ------------------------------------------------------

    return word_similarity(
        sentence_a,
        sentence_b
    )


# ==========================================================
# REMOVE DUPLICATE SENTENCES
# ==========================================================

def remove_duplicate_sentences(
    sentences,
    threshold=SIMILARITY_THRESHOLD
):
    """
    Removes sentences that communicate
    substantially the same information.

    The first occurrence is retained.
    """

    if not sentences:

        return []

    unique_sentences = []

    for sentence in sentences:

        sentence = clean_text(
            sentence
        )

        if not sentence:

            continue

        duplicate = False

        for existing in unique_sentences:

            similarity = calculate_sentence_similarity(
                sentence,
                existing
            )

            if similarity >= threshold:

                duplicate = True

                break

        if not duplicate:

            unique_sentences.append(
                sentence
            )

    return unique_sentences


# ==========================================================
# EXTRACT QUESTION KEYWORDS
# ==========================================================

def extract_question_keywords(
    question
):
    """
    Extract important words from the question.
    """

    if not question:

        return []

    question = normalize_sentence(
        question
    )

    stopwords = {

        "what",
        "is",
        "are",
        "the",
        "a",
        "an",
        "of",
        "to",
        "in",
        "on",
        "for",
        "and",
        "or",
        "how",
        "why",
        "does",
        "do",
        "did",
        "can",
        "could",
        "would",
        "should",
        "i",
        "me",
        "my",
        "you",
        "your",
        "please",
        "tell",
        "about",
        "give",
        "explain",
        "describe",
        "what",
        "are",
        "is",

    }

    words = question.split()

    keywords = []

    for word in words:

        if word in stopwords:

            continue

        if len(word) <= 2:

            continue

        keywords.append(
            word
        )

    return keywords


# ==========================================================
# SENTENCE QUESTION RELEVANCE
# ==========================================================

def calculate_sentence_relevance(
    question,
    sentence
):
    """
    Measures how strongly a sentence relates
    to the user's question.
    """

    if not question or not sentence:

        return 0.0

    keywords = extract_question_keywords(
        question
    )

    if not keywords:

        return 0.0

    sentence_lower = sentence.lower()

    matches = 0

    for keyword in keywords:

        if re.search(
            r"\b"
            + re.escape(keyword)
            + r"\b",
            sentence_lower
        ):

            matches += 1

    return (
        matches
        /
        len(keywords)
    )


# ==========================================================
# SOURCE WEIGHT
# ==========================================================

def get_source_weight(
    source
):
    """
    Assigns a small additional weight based
    on the reliability of the source.
    """

    source = str(
        source or ""
    ).lower()

    weights = {

        "knowledge": 1.00,

        "akan": 0.95,

        "educational_web": 0.90,

        "web": 0.75,

    }

    return weights.get(
        source,
        0.60
    )


# ==========================================================
# PREPARE EVIDENCE
# ==========================================================

def prepare_evidence(
    ranked_answers,
    question=""
):
    """
    Extract useful sentences from ranked answers.

    Expected input:

        [
            {
                "source": "...",
                "answer": "...",
                "score": 76
            }
        ]
    """

    if not ranked_answers:

        return []

    evidence = []

    # ------------------------------------------------------
    # Accept a single dictionary as well.
    # ------------------------------------------------------

    if isinstance(
        ranked_answers,
        dict
    ):

        ranked_answers = [
            ranked_answers
        ]

    # ------------------------------------------------------
    # Process ranked answers.
    # ------------------------------------------------------

    for rank_index, item in enumerate(
        ranked_answers
    ):

        if not isinstance(
            item,
            dict
        ):

            continue

        answer = clean_text(
            item.get(
                "answer",
                ""
            )
        )

        if not answer:

            continue

        source = item.get(
            "source",
            "unknown"
        )

        score = item.get(
            "score",
            0
        )

        try:

            score = float(
                score
            )

        except (
            TypeError,
            ValueError
        ):

            score = 0

        sentences = split_sentences(
            answer
        )

        for sentence_index, sentence in enumerate(
            sentences
        ):

            relevance = calculate_sentence_relevance(
                question,
                sentence
            )

            evidence_score = (
                score
                * 0.60
                +
                relevance
                * 20
                +
                get_source_weight(source)
                * 5
            )

            evidence.append({

                "sentence":
                    sentence,

                "source":
                    source,

                "score":
                    evidence_score,

                "original_score":
                    score,

                "relevance":
                    relevance,

                "rank":
                    rank_index,

                "sentence_index":
                    sentence_index,

            })

    # ------------------------------------------------------
    # Sort strongest evidence first.
    # ------------------------------------------------------

    evidence.sort(
        key=lambda item: item.get(
            "score",
            0
        ),
        reverse=True
    )

    # ------------------------------------------------------
    # Remove duplicate information.
    # ------------------------------------------------------

    selected = []

    for item in evidence:

        sentence = item.get(
            "sentence",
            ""
        )

        duplicate = False

        for existing in selected:

            similarity = calculate_sentence_similarity(
                sentence,
                existing["sentence"]
            )

            if similarity >= SIMILARITY_THRESHOLD:

                duplicate = True

                break

        if duplicate:

            continue

        selected.append(
            item
        )

        if len(selected) >= MAX_EVIDENCE_ITEMS:

            break

    return selected


# ==========================================================
# GET EVIDENCE SENTENCES
# ==========================================================

def get_evidence_sentences(
    ranked_answers,
    question=""
):
    """
    Convenience function returning only
    the selected evidence sentences.
    """

    evidence = prepare_evidence(
        ranked_answers,
        question
    )

    return [
        item["sentence"]
        for item in evidence
    ]


# ==========================================================
# BUILD INTRODUCTION
# ==========================================================

def build_introduction(
    topic,
    intent
):
    """
    Creates a short introduction according
    to the detected intent.
    """

    topic = clean_text(
        topic
    )

    if not topic:

        return ""

    if intent in {
        "definition",
        "meaning"
    }:

        return (
            f"{topic.capitalize()} refers to "
        )

    if intent == "explanation":

        return (
            f"{topic.capitalize()} can be understood "
            f"as follows: "
        )

    if intent == "summary":

        return (
            f"In summary, {topic} "
        )

    return ""


# ==========================================================
# ENSURE SENTENCE PUNCTUATION
# ==========================================================

def ensure_punctuation(
    sentence
):
    """
    Ensures a sentence ends with punctuation.
    """

    sentence = clean_text(
        sentence
    )

    if not sentence:

        return ""

    if sentence.endswith(
        (".", "!", "?")
    ):

        return sentence

    return (
        sentence
        + "."
    )


# ==========================================================
# FORMAT LIST ITEMS
# ==========================================================

def format_list_items(
    sentences
):
    """
    Formats evidence as numbered educational points.
    """

    formatted = []

    for index, sentence in enumerate(
        sentences,
        start=1
    ):

        sentence = ensure_punctuation(
            sentence
        )

        formatted.append(
            f"{index}. {sentence}"
        )

    return formatted


# ==========================================================
# SYNTHESIZE DEFINITION
# ==========================================================

def synthesize_definition(
    evidence,
    topic
):
    """
    Build a definition-style answer.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    if not sentences:

        return None

    # ------------------------------------------------------
    # Prefer the strongest definition-like sentence.
    # ------------------------------------------------------

    best = sentences[0]

    result = ensure_punctuation(
        best
    )

    # Add one supporting sentence when useful.
    # ------------------------------------------------------

    if len(sentences) > 1:

        supporting = sentences[1]

        if calculate_sentence_similarity(
            best,
            supporting
        ) < 0.65:

            result += " " + ensure_punctuation(
                supporting
            )

    return result


# ==========================================================
# SYNTHESIZE EXPLANATION
# ==========================================================

def synthesize_explanation(
    evidence,
    topic
):
    """
    Build a coherent explanation.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :MAX_SENTENCES
    ]

    return " ".join(
        ensure_punctuation(sentence)
        for sentence in sentences
    )


# ==========================================================
# SYNTHESIZE LIST
# ==========================================================

def synthesize_list(
    evidence,
    topic,
    intent
):
    """
    Build a numbered answer for list-oriented intents.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :MAX_SENTENCES
    ]

    return "\n".join(
        format_list_items(
            sentences
        )
    )


# ==========================================================
# SYNTHESIZE PROCESS
# ==========================================================

def synthesize_process(
    evidence,
    topic
):
    """
    Build a process/procedure answer.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :MAX_SENTENCES
    ]

    return "\n".join(
        format_list_items(
            sentences
        )
    )


# ==========================================================
# SYNTHESIZE COMPARISON
# ==========================================================

def synthesize_comparison(
    evidence,
    topic
):
    """
    Build a comparison answer.

    The evidence is preserved rather than
    inventing unsupported differences.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :MAX_SENTENCES
    ]

    return "\n".join(
        format_list_items(
            sentences
        )
    )


# ==========================================================
# SYNTHESIZE SUMMARY
# ==========================================================

def synthesize_summary(
    evidence,
    topic
):
    """
    Produce a concise summary from strong evidence.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :4
    ]

    return " ".join(
        ensure_punctuation(sentence)
        for sentence in sentences
    )


# ==========================================================
# SYNTHESIZE EXAM ANSWER
# ==========================================================

def synthesize_exam_answer(
    evidence,
    topic,
    intent
):
    """
    Produces a structured examination-oriented answer.

    It does not invent facts. It reorganizes
    retrieved evidence into a clearer format.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :MAX_SENTENCES
    ]

    answer = []

    if sentences:

        answer.append(
            "Key points:"
        )

        answer.extend(
            format_list_items(
                sentences
            )
        )

    return "\n".join(
        answer
    )


# ==========================================================
# SYNTHESIZE GENERAL
# ==========================================================

def synthesize_general(
    evidence,
    topic
):
    """
    General-purpose evidence synthesis.
    """

    if not evidence:

        return None

    sentences = [
        item["sentence"]
        for item in evidence
    ]

    sentences = remove_duplicate_sentences(
        sentences
    )

    sentences = sentences[
        :MAX_SENTENCES
    ]

    return " ".join(
        ensure_punctuation(sentence)
        for sentence in sentences
    )


# ==========================================================
# CALCULATE CONFIDENCE
# ==========================================================

def calculate_confidence(
    ranked_answers,
    evidence,
    question="",
    intent="general"
):
    """Return an interpretable 0-1 confidence estimate.

    The ranking engine now produces a normalized 0-100 score. Confidence
    therefore uses the top candidate, the margin over the runner-up, evidence
    relevance, and agreement between sources rather than treating raw score
    values as probabilities.
    """
    if not ranked_answers or not evidence:
        return 0.0
    if isinstance(ranked_answers, dict):
        ranked_answers = [ranked_answers]

    scores = []
    sources = set()
    for item in ranked_answers:
        if not isinstance(item, dict):
            continue
        try:
            scores.append(float(item.get("score", 0)))
        except (TypeError, ValueError):
            pass

    top_score = min(100.0, max(0.0, max(scores) if scores else 0.0)) / 100.0
    second_score = scores[1] if len(scores) > 1 else 0.0
    margin = min(1.0, max(0.0, ((scores[0] - second_score) / 25.0))) if scores else 0.0

    relevance_values = []
    for item in evidence:
        try:
            relevance_values.append(float(item.get("relevance", 0)))
        except (TypeError, ValueError):
            pass
        if item.get("source"):
            sources.add(str(item.get("source")))

    relevance = sum(relevance_values) / len(relevance_values) if relevance_values else 0.0
    diversity = min(1.0, len(sources) / 3.0)
    evidence_strength = min(1.0, len(evidence) / 4.0)

    confidence = (
        top_score * 0.45
        + margin * 0.20
        + relevance * 0.20
        + diversity * 0.10
        + evidence_strength * 0.05
    )

    # Exact lexical translation from the Akan engine is deterministic and
    # should not be reported as uncertain when the candidate is present.
    if intent == "translation" and ranked_answers and ranked_answers[0].get("source") == "akan":
        confidence = max(confidence, 0.95)

    return round(min(1.0, max(0.0, confidence)), 2)


# ==========================================================
# SOURCE SUMMARY
# ==========================================================

def build_source_summary(
    evidence
):
    """
    Returns the sources that contributed
    to the synthesized answer.
    """

    sources = []

    for item in evidence:

        source = item.get(
            "source"
        )

        if not source:

            continue

        source = str(
            source
        )

        if source not in sources:

            sources.append(
                source
            )

    return sources


# ==========================================================
# MAIN SYNTHESIS FUNCTION
# ==========================================================

def synthesize_answer(
    question,
    intent="general",
    topic="",
    ranked_answers=None,
    language="english"
):
    """
    Main Answer Synthesis Engine.

    Parameters:

        question:
            Original user question.

        intent:
            Detected intent.

        topic:
            Extracted topic.

        ranked_answers:
            Results from Ranking Engine.

        language:
            Current response language.

    Returns:

        {
            "answer": str,
            "confidence": float,
            "sources": list,
            "intent": str,
            "topic": str,
            "language": str
        }
    """

    question = clean_text(
        question
    )

    topic = clean_text(
        topic
    )

    intent = clean_text(
        intent
    ).lower()

    language = clean_text(
        language
    ).lower()

    # ------------------------------------------------------
    # Validate input
    # ------------------------------------------------------

    if not question:

        return {

            "answer":
                "Please provide a question.",

            "confidence":
                0.0,

            "sources":
                [],

            "intent":
                intent,

            "topic":
                topic,

            "language":
                language,

        }

    if not ranked_answers:

        return {

            "answer":
                None,

            "confidence":
                0.0,

            "sources":
                [],

            "intent":
                intent,

            "topic":
                topic,

            "language":
                language,

        }

    # ------------------------------------------------------
    # Prepare evidence
    # ------------------------------------------------------

    evidence = prepare_evidence(
        ranked_answers,
        question
    )

    # ------------------------------------------------------
    # No useful evidence
    # ------------------------------------------------------

    if not evidence:

        return {

            "answer":
                None,

            "confidence":
                0.0,

            "sources":
                [],

            "intent":
                intent,

            "topic":
                topic,

            "language":
                language,

        }

    # ======================================================
    # SELECT SYNTHESIS STRATEGY
    # ======================================================

    answer = None

    # ------------------------------------------------------
    # Translation
    # ------------------------------------------------------

    if intent == "translation":
        # Translation candidates are normally already formatted by the Akan
        # engine. Preserve the highest-ranked lexical answer instead of
        # paraphrasing it and risking a changed translation.
        answer = ranked_answers[0].get("answer") if ranked_answers else None

    # ------------------------------------------------------
    # Definition
    # ------------------------------------------------------

    if intent in {
        "definition",
        "meaning"
    }:

        answer = synthesize_definition(
            evidence,
            topic
        )

    # ------------------------------------------------------
    # Lists
    # ------------------------------------------------------

    elif intent in LIST_INTENTS:

        if intent == "process":

            answer = synthesize_process(
                evidence,
                topic
            )

        elif intent == "comparison":

            answer = synthesize_comparison(
                evidence,
                topic
            )

        else:

            answer = synthesize_list(
                evidence,
                topic,
                intent
            )

    # ------------------------------------------------------
    # Comparison
    # ------------------------------------------------------

    elif intent == "comparison":

        answer = synthesize_comparison(
            evidence,
            topic
        )

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    elif intent == "summary":

        answer = synthesize_summary(
            evidence,
            topic
        )

    # ------------------------------------------------------
    # Examination
    # ------------------------------------------------------

    elif intent == "exam":

        answer = synthesize_exam_answer(
            evidence,
            topic,
            intent
        )

    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    elif intent == "explanation":

        answer = synthesize_explanation(
            evidence,
            topic
        )

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    else:

        answer = synthesize_general(
            evidence,
            topic
        )

    # ------------------------------------------------------
    # Safety fallback
    # ------------------------------------------------------

    if not answer:

        answer = synthesize_general(
            evidence,
            topic
        )

    # ------------------------------------------------------
    # Calculate confidence
    # ------------------------------------------------------

    confidence = calculate_confidence(
        ranked_answers,
        evidence,
        question,
        intent
    )

    # ------------------------------------------------------
    # Source information
    # ------------------------------------------------------

    sources = build_source_summary(
        evidence
    )

    # ------------------------------------------------------
    # Final result
    # ------------------------------------------------------

    return {

        "answer":
            clean_text(answer),

        "confidence":
            confidence,

        "sources":
            sources,

        "intent":
            intent,

        "topic":
            topic,

        "language":
            language,

    }


# ==========================================================
# SIMPLE ANSWER HELPER
# ==========================================================

def get_synthesized_text(
    question,
    intent,
    topic,
    ranked_answers,
    language="english"
):
    """
    Convenience function returning only the
    final synthesized answer.
    """

    result = synthesize_answer(
        question=question,
        intent=intent,
        topic=topic,
        ranked_answers=ranked_answers,
        language=language
    )

    return result.get(
        "answer"
    )


# ==========================================================
# TEST DATA
# ==========================================================

def build_test_results():
    """
    Creates controlled test data for the
    Answer Synthesis Engine.
    """

    return [

        {
            "source":
                "knowledge",

            "score":
                76,

            "answer":
                (
                    "Artificial intelligence has many "
                    "applications. It is used in healthcare "
                    "for disease detection, in education "
                    "for personalized learning, in banking "
                    "for fraud detection, in transportation "
                    "for navigation and autonomous systems, "
                    "and in customer service through chatbots."
                ),
        },

        {
            "source":
                "web",

            "score":
                65,

            "answer":
                (
                    "Artificial intelligence is used in "
                    "healthcare, banking, education, "
                    "transportation and customer service."
                ),
        },

        {
            "source":
                "educational_web",

            "score":
                51,

            "answer":
                (
                    "AI applications include healthcare, "
                    "education, finance, transportation "
                    "and customer service."
                ),
        },

    ]


# ==========================================================
# TEST ANSWER SYNTHESIS
# ==========================================================

def test_answer_synthesis_engine():
    """
    Tests the synthesis engine against
    several educational intents.
    """

    print(
        "\n=========================================="
    )

    print(
        "🧠 ANSWER SYNTHESIS ENGINE TEST"
    )

    print(
        "=========================================="
    )

    results = build_test_results()

    test_questions = [

        (
            "What are the applications "
            "of artificial intelligence?",
            "applications",
            "artificial intelligence"
        ),

        (
            "What is artificial intelligence?",
            "definition",
            "artificial intelligence"
        ),

        (
            "Explain artificial intelligence.",
            "explanation",
            "artificial intelligence"
        ),

        (
            "Summarize artificial intelligence.",
            "summary",
            "artificial intelligence"
        ),

        (
            "List applications of artificial intelligence.",
            "list",
            "artificial intelligence"
        ),

        (
            "Prepare me for an exam on artificial intelligence.",
            "exam",
            "artificial intelligence"
        ),

    ]

    for question, intent, topic in test_questions:

        print(
            "\n------------------------------------------"
        )

        print(
            "Question:",
            question
        )

        print(
            "Intent:",
            intent
        )

        result = synthesize_answer(

            question=
                question,

            intent=
                intent,

            topic=
                topic,

            ranked_answers=
                results,

            language=
                "english"

        )

        print(
            "\nSYNTHESIZED ANSWER:"
        )

        print(
            result.get(
                "answer"
            )
        )

        print(
            "\nCONFIDENCE:",
            result.get(
                "confidence"
            )
        )

        print(
            "SOURCES:",
            result.get(
                "sources"
            )
        )

    print(
        "\n=========================================="
    )

    print(
        "✅ ANSWER SYNTHESIS TEST COMPLETE"
    )

    print(
        "=========================================="
    )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_answer_synthesis_engine()


# ==========================================================
# END OF ANSWER SYNTHESIS ENGINE
# ==========================================================