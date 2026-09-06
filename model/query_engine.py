# ==========================================================
#
# QUERY ENGINE
# Intelligent Query Planning and Search Expansion
#
# Stage 3
# Akan/Twi-aware query generation
# Educational query expansion
#
# ==========================================================

import re


# ==========================================================
# AKAN / TWI VOCABULARY SIGNALS
# ==========================================================

AKAN_SPECIAL_CHARACTERS = [
    "ɔ",
    "ɛ",
    "ŋ",
]

# Keep this list focused on reasonably strong Akan/Twi signals.

AKAN_COMMON_WORDS = [
    "nsuo",
    "ɔdɔ",
    "meda ase",
    "akwaaba",
    "maakye",
    "maaha",
    "maadwo",
    "nante yie",
    "wo ho te sɛn",
    "me ho yɛ",
    "asɛm",
    "sukuu",
    "osuani",
    "ɔkyerɛkyerɛni",
    "adesua",
    "abusua",
    "okunu",
    "ɔbaa",
    "ɔbarima",
    "ɔhene",
    "ɔman",
    "asase",
    "mframa",
    "owia",
    "ɔsram",
    "adaka",
    "aduane",
    "ano",
    "ti",
    "nsa",
    "ani",
    "koma",
    "twi",
    "akan",
]


# ==========================================================
# GENERAL STOPWORDS
# ==========================================================

STOPWORDS = {
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
    "can",
    "could",
    "would",
    "does",
    "do",
    "did",
    "i",
    "me",
    "my",
    "please",
    "tell",
    "give",
    "show",
    "explain",
}


# ==========================================================
# AKAN / TWI QUESTION STOPWORDS
# ==========================================================

AKAN_QUESTION_STOPWORDS = {
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
    "can",
    "could",
    "would",
    "does",
    "do",
    "did",
    "please",
    "tell",
    "me",
    "give",
    "show",
    "explain",
    "meaning",
    "definition",
    "define",
    "word",
    "words",
    "twi",
    "akan",
    "english",
    "translation",
    "translate",
    "into",
    "from",
}


# ==========================================================
# QUERY TYPE DETECTION
# ==========================================================

def detect_query_type(question):
    """
    Detect the user's question type.

    Returns:
        translation
        synonym
        antonym
        example
        description
        explanation
        definition
        general
    """

    if not question:
        return "general"

    q = str(question).lower().strip()

    # ------------------------------------------------------
    # Translation
    # ------------------------------------------------------

    translation_patterns = [
        "translate",
        "translation",
        "translate into twi",
        "translate to twi",
        "in twi",
        "into twi",
        "in akan",
        "into akan",
        "how do you say",
    ]

    if any(
        pattern in q
        for pattern in translation_patterns
    ):
        return "translation"

    # ------------------------------------------------------
    # Synonyms
    # ------------------------------------------------------

    synonym_patterns = [
        "synonym",
        "synonyms",
        "similar word",
        "similar words",
        "another word for",
    ]

    if any(
        pattern in q
        for pattern in synonym_patterns
    ):
        return "synonym"

    # ------------------------------------------------------
    # Antonyms
    # ------------------------------------------------------

    antonym_patterns = [
        "antonym",
        "antonyms",
        "opposite",
        "opposite word",
        "opposite meaning",
    ]

    if any(
        pattern in q
        for pattern in antonym_patterns
    ):
        return "antonym"

    # ------------------------------------------------------
    # Example
    # ------------------------------------------------------

    example_patterns = [
        "example",
        "examples",
        "sentence",
        "use it in a sentence",
        "use in a sentence",
        "sentence with",
    ]

    if any(
        pattern in q
        for pattern in example_patterns
    ):
        return "example"

    # ------------------------------------------------------
    # Description
    # ------------------------------------------------------

    description_patterns = [
        "describe",
        "description",
    ]

    if any(
        pattern in q
        for pattern in description_patterns
    ):
        return "description"

    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    explanation_patterns = [
        "explain",
        "explanation",
        "explain simply",
        "how does",
        "why",
    ]

    if any(
        pattern in q
        for pattern in explanation_patterns
    ):
        return "explanation"

    # ------------------------------------------------------
    # Definition / Meaning
    # ------------------------------------------------------

    definition_patterns = [
        "what is",
        "what are",
        "what does",
        "meaning",
        "meaning of",
        "define",
        "definition",
    ]

    if any(
        pattern in q
        for pattern in definition_patterns
    ):
        return "definition"

    return "general"


# ==========================================================
# AKAN / TWI DETECTION
# ==========================================================

def detect_akan(question):
    """
    Detect whether a question is likely related to
    Akan/Twi language.
    """

    if not question:
        return False

    q = str(question).lower().strip()

    # ------------------------------------------------------
    # Special Akan characters
    # ------------------------------------------------------

    if any(
        character in q
        for character in AKAN_SPECIAL_CHARACTERS
    ):
        return True

    # ------------------------------------------------------
    # Explicit language references
    # ------------------------------------------------------

    language_patterns = [
        "in twi",
        "into twi",
        "to twi",
        "twi meaning",
        "twi word",
        "twi words",
        "twi sentence",
        "twi translation",
        "in akan",
        "into akan",
        "to akan",
        "akan meaning",
        "akan word",
        "akan words",
        "akan sentence",
        "akan translation",
    ]

    if any(
        pattern in q
        for pattern in language_patterns
    ):
        return True

    # ------------------------------------------------------
    # Strong Akan/Twi vocabulary
    # ------------------------------------------------------

    words = q.split()

    for phrase in AKAN_COMMON_WORDS:

        if " " in phrase:

            if phrase in q:
                return True

        elif phrase in words:
            return True

    return False


# ==========================================================
# EXTRACT LANGUAGE TARGET
# ==========================================================

def extract_language_target(question):
    """
    Determine the language involved in the question.
    """

    if not question:
        return "unknown"

    q = str(question).lower()

    if (
        "twi" in q
        or "akan" in q
    ):
        return "akan"

    if detect_akan(question):
        return "akan"

    return "english"


# ==========================================================
# NORMALIZE TEXT
# ==========================================================

def normalize_text(text):
    """
    Normalize text while preserving Akan characters.
    """

    if not text:
        return ""

    text = str(text).lower().strip()

    text = re.sub(
        r"[^\w\sɔɛŋ]",
        " ",
        text,
    )

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()


# ==========================================================
# CLEAN QUESTION
# ==========================================================

def clean_question(question):
    """
    Remove common question structures and return
    the meaningful topic words.
    """

    if not question:
        return ""

    q = normalize_text(question)

    remove_patterns = [
        "what is the meaning of",
        "what does this word mean",
        "what does this phrase mean",
        "what does this mean",
        "what is",
        "what are",
        "what does",
        "what do",
        "what did",
        "meaning of",
        "definition of",
        "meaning",
        "mean",
        "define",
        "definition",
        "explain",
        "describe",
        "translation of",
        "translate",
        "in twi",
        "into twi",
        "to twi",
        "in akan",
        "into akan",
        "to akan",
        "twi meaning",
        "akan meaning",
        "please",
        "can you",
        "could you",
        "tell me",
        "give me",
        "show me",
    ]

    for pattern in remove_patterns:

        q = q.replace(
            pattern,
            " ",
        )

    q = re.sub(
        r"\s+",
        " ",
        q,
    )

    return q.strip()


# ==========================================================
# EXTRACT AKAN TARGET
#
# Example:
#
# What is the meaning of nsuo in Twi?
#
# TARGET:
# nsuo
#
# ==========================================================

def extract_akan_target(question):
    """
    Extract the actual Akan/Twi word or phrase
    the user is asking about.
    """

    if not question:
        return ""

    original = str(
        question
    ).lower().strip()

    # ------------------------------------------------------
    # Preserve quoted phrases
    # ------------------------------------------------------

    quoted = re.findall(
        r'"([^"]+)"',
        original,
    )

    if quoted:
        return normalize_text(
            quoted[0]
        )

    quoted = re.findall(
        r"'([^']+)'",
        original,
    )

    if quoted:
        return normalize_text(
            quoted[0]
        )

    # ------------------------------------------------------
    # Normalize
    # ------------------------------------------------------

    q = normalize_text(
        original
    )

    # ------------------------------------------------------
    # Remove common question structures
    # ------------------------------------------------------

    patterns = [
        r"\bwhat is the meaning of\b",
        r"\bwhat is\b",
        r"\bwhat are\b",
        r"\bwhat does\b",
        r"\bwhat do\b",
        r"\bmeaning of\b",
        r"\bmeaning\b",
        r"\bdefine\b",
        r"\bdefinition of\b",
        r"\bdefinition\b",
        r"\bexplain\b",
        r"\bdescribe\b",
        r"\bplease\b",
        r"\bcan you\b",
        r"\bcould you\b",
        r"\btell me\b",
        r"\bgive me\b",
        r"\bshow me\b",
    ]

    for pattern in patterns:

        q = re.sub(
            pattern,
            " ",
            q,
        )

    # ------------------------------------------------------
    # Remove language markers
    # ------------------------------------------------------

    q = re.sub(
        r"\b(in|into|to|from)\s+(twi|akan)\b",
        " ",
        q,
    )

    q = re.sub(
        r"\b(twi|akan)\b",
        " ",
        q,
    )

    # ------------------------------------------------------
    # Remove question words and connectors
    # ------------------------------------------------------

    words = q.split()

    useful_words = []

    for word in words:

        if word in AKAN_QUESTION_STOPWORDS:
            continue

        useful_words.append(
            word
        )

    q = " ".join(
        useful_words
    )

    # ------------------------------------------------------
    # Remove trailing meaning words
    # ------------------------------------------------------

    q = re.sub(
        r"\b(mean|means|meaning)\b",
        " ",
        q,
    )

    q = re.sub(
        r"\s+",
        " ",
        q,
    ).strip()

    # ------------------------------------------------------
    # Prefer known Akan expressions
    # ------------------------------------------------------

    q_words = q.split()

    for phrase in sorted(
        AKAN_COMMON_WORDS,
        key=len,
        reverse=True,
    ):

        phrase_words = phrase.split()

        if len(phrase_words) > len(q_words):
            continue

        normalized_phrase = normalize_text(
            phrase
        )

        normalized_q = normalize_text(
            q
        )

        if normalized_phrase in normalized_q:
            return normalized_phrase

    # ------------------------------------------------------
    # Preserve words containing Akan characters
    # ------------------------------------------------------

    akan_words = []

    for word in q_words:

        if any(
            char in word
            for char in AKAN_SPECIAL_CHARACTERS
        ):
            akan_words.append(
                word
            )

    if akan_words:
        return " ".join(
            akan_words
        )

    # ------------------------------------------------------
    # Return remaining meaningful text
    # ------------------------------------------------------

    return q.strip()


# ==========================================================
# EXTRACT GENERAL TOPIC
# ==========================================================

def extract_topic(question):
    """
    Extract the main topic from a general question.
    """

    if not question:
        return ""

    if detect_akan(question):

        akan_target = extract_akan_target(
            question
        )

        if akan_target:
            return akan_target

    cleaned = clean_question(
        question
    )

    words = cleaned.split()

    useful_words = [
        word
        for word in words
        if word not in STOPWORDS
        and len(word) > 1
    ]

    return " ".join(
        useful_words
    ).strip()


# ==========================================================
# GENERAL EDUCATIONAL QUERY EXPANSION
# ==========================================================

def generate_educational_queries(
    question,
    topic,
    query_type,
):
    """
    Generate multiple educational search queries.
    """

    queries = []

    base = (
        topic
        or question
        or ""
    ).strip()

    if not base:
        return []

    # ------------------------------------------------------
    # Original question
    # ------------------------------------------------------

    if question:
        queries.append(
            str(question).strip()
        )

    # ------------------------------------------------------
    # Definition
    # ------------------------------------------------------

    if query_type == "definition":

        queries.extend([
            f"{base} definition",
            f"{base} explained",
            f"{base} meaning",
            f"{base} educational explanation",
            f"{base} textbook explanation",
            f"{base} lecture notes",
            f"{base} definition textbook",
            f"{base} definition university",
        ])

    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    elif query_type == "explanation":

        queries.extend([
            f"{base} explained",
            f"{base} simple explanation",
            f"{base} educational explanation",
            f"{base} examples",
            f"{base} lecture notes",
            f"{base} textbook",
        ])

    # ------------------------------------------------------
    # Translation
    # ------------------------------------------------------

    elif query_type == "translation":

        queries.extend([
            f"{base} translation",
            f"{base} English meaning",
            f"{base} dictionary",
            f"{base} language meaning",
        ])

    # ------------------------------------------------------
    # Example
    # ------------------------------------------------------

    elif query_type == "example":

        queries.extend([
            f"{base} examples",
            f"{base} example",
            f"{base} practical example",
            f"{base} educational example",
        ])

    # ------------------------------------------------------
    # Synonym
    # ------------------------------------------------------

    elif query_type == "synonym":

        queries.extend([
            f"{base} synonyms",
            f"{base} similar words",
            f"{base} related words",
        ])

    # ------------------------------------------------------
    # Antonym
    # ------------------------------------------------------

    elif query_type == "antonym":

        queries.extend([
            f"{base} antonyms",
            f"{base} opposite",
            f"{base} opposite meaning",
        ])

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    else:

        queries.extend([
            f"{base} explained",
            f"{base} educational",
            f"{base} examples",
            f"{base} textbook explanation",
        ])

    # ------------------------------------------------------
    # Trusted educational sources
    # ------------------------------------------------------

    queries.extend([
        f"{base} site:openstax.org",
        f"{base} site:ocw.mit.edu",
        f"{base} site:edu",
    ])

    return unique_queries(
        queries
    )


# ==========================================================
# AKAN / TWI QUERY EXPANSION
# ==========================================================

def generate_akan_queries(
    question,
    target,
    query_type,
):
    """
    Generate search queries specifically for
    Akan/Twi language retrieval.
    """

    queries = []

    term = (
        target
        or question
        or ""
    ).strip()

    if not term:
        return []

    # ------------------------------------------------------
    # Exact term
    # ------------------------------------------------------

    queries.extend([
        f'"{term}" Twi',
        f'"{term}" Akan',
        f'"{term}" English',
    ])

    # ------------------------------------------------------
    # Definition
    # ------------------------------------------------------

    if query_type == "definition":

        queries.extend([
            f'"{term}" meaning Twi',
            f'"{term}" meaning Akan',
            f'"{term}" English meaning',
            f'"{term}" Twi dictionary',
            f'"{term}" Akan dictionary',
            f'"{term}" definition Twi',
            f'"{term}" definition Akan',
            f'"{term}" explained Twi',
        ])

    # ------------------------------------------------------
    # Translation
    # ------------------------------------------------------

    elif query_type == "translation":

        queries.extend([
            f'"{term}" English translation',
            f'"{term}" Twi translation',
            f'"{term}" Akan translation',
            f'"{term}" English Twi dictionary',
            f'"{term}" Twi English dictionary',
        ])

    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    elif query_type == "explanation":

        queries.extend([
            f'"{term}" explained in Twi',
            f'"{term}" Twi explanation',
            f'"{term}" Akan explanation',
            f'"{term}" meaning and usage Twi',
            f'"{term}" Twi usage',
        ])

    # ------------------------------------------------------
    # Examples
    # ------------------------------------------------------

    elif query_type == "example":

        queries.extend([
            f'"{term}" Twi example',
            f'"{term}" Twi sentence',
            f'"{term}" used in a sentence Twi',
            f'"{term}" Akan sentence',
            f'"{term}" Twi usage example',
        ])

    # ------------------------------------------------------
    # Synonyms
    # ------------------------------------------------------

    elif query_type == "synonym":

        queries.extend([
            f'"{term}" Twi synonyms',
            f'"{term}" Akan synonyms',
            f'"{term}" similar Twi words',
            f'"{term}" related Twi words',
        ])

    # ------------------------------------------------------
    # Antonyms
    # ------------------------------------------------------

    elif query_type == "antonym":

        queries.extend([
            f'"{term}" Twi antonym',
            f'"{term}" Akan antonym',
            f'"{term}" opposite in Twi',
            f'"{term}" opposite meaning Twi',
        ])

    # ------------------------------------------------------
    # Description
    # ------------------------------------------------------

    elif query_type == "description":

        queries.extend([
            f'"{term}" Twi description',
            f'"{term}" Akan description',
            f'"{term}" meaning and description',
            f'"{term}" Twi usage',
        ])

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    else:

        queries.extend([
            f'"{term}" Twi meaning',
            f'"{term}" Akan meaning',
            f'"{term}" Twi usage',
            f'"{term}" Twi example',
            f'"{term}" English meaning',
        ])

    # ------------------------------------------------------
    # External Akan/Twi resources
    # ------------------------------------------------------

    queries.extend([
        f'"{term}" site:learnakandictionary.com',
        f'"{term}" site:ghananlp.org',
        f'"{term}" site:ghananlp.github.io',
        f'"{term}" site:huggingface.co',
    ])

    return unique_queries(
        queries,
        limit=12,
    )


# ==========================================================
# UNIQUE QUERY CLEANER
# ==========================================================

def unique_queries(
    queries,
    limit=12,
):
    """
    Remove duplicate search queries while preserving order.
    """

    cleaned = []
    seen = set()

    if not queries:
        return []

    for query in queries:

        if not query:
            continue

        query = str(
            query
        ).strip()

        if not query:
            continue

        key = query.lower()

        if key in seen:
            continue

        seen.add(
            key
        )

        cleaned.append(
            query
        )

        if len(cleaned) >= limit:
            break

    return cleaned


# ==========================================================
# CREATE QUERY PLAN
# ==========================================================

def create_query_plan(question):
    """
    Create a complete search plan for the router.

    Returns:
        queries
        topic
        query_type
        language
        is_akan
        target
    """

    if not question:

        return {
            "queries": [],
            "topic": "",
            "query_type": "general",
            "language": "unknown",
            "is_akan": False,
            "target": "",
        }

    question = str(
        question
    ).strip()

    if not question:

        return {
            "queries": [],
            "topic": "",
            "query_type": "general",
            "language": "unknown",
            "is_akan": False,
            "target": "",
        }

    # ======================================================
    # LANGUAGE
    # ======================================================

    is_akan = detect_akan(
        question
    )

    language = extract_language_target(
        question
    )

    # ======================================================
    # QUERY TYPE
    # ======================================================

    query_type = detect_query_type(
        question
    )

    # ======================================================
    # TARGET / TOPIC
    # ======================================================

    if is_akan:

        target = extract_akan_target(
            question
        )

        topic = target

    else:

        target = ""

        topic = extract_topic(
            question
        )

    # ======================================================
    # QUERY GENERATION
    # ======================================================

    if is_akan:

        queries = generate_akan_queries(
            question,
            target,
            query_type,
        )

    else:

        queries = generate_educational_queries(
            question,
            topic,
            query_type,
        )

    # ======================================================
    # RESULT
    # ======================================================

    return {
        "queries": queries,
        "topic": topic,
        "query_type": query_type,
        "language": language,
        "is_akan": is_akan,
        "target": target,
    }


# ==========================================================
# TEST QUERY ENGINE
# ==========================================================

def test_query_engine():
    """
    Test the Query Engine using representative questions.
    """

    test_questions = [
        "What is artificial intelligence?",
        "Explain machine learning",
        "What does nsuo mean in Twi?",
        "What is the meaning of ɔdɔ?",
        "Translate water into Twi",
        "Give me an example of nsuo",
        "What are synonyms of ɔdɔ?",
        "What is the opposite of ɔdɔ?",
        'What does "nsuo retɔ" mean?',
        "How do you say I am hungry in Twi?",
    ]

    for question in test_questions:

        print(
            "\n======================================"
        )

        print(
            "QUESTION:",
            question,
        )

        plan = create_query_plan(
            question
        )

        print(
            "LANGUAGE:",
            plan["language"],
        )

        print(
            "AKAN:",
            plan["is_akan"],
        )

        print(
            "TYPE:",
            plan["query_type"],
        )

        print(
            "TOPIC:",
            plan["topic"],
        )

        print(
            "TARGET:",
            plan["target"],
        )

        print(
            "QUERIES:"
        )

        for index, query in enumerate(
            plan["queries"],
            start=1,
        ):

            print(
                f"{index}. {query}"
            )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":
    test_query_engine()


# ==========================================================
# END OF QUERY ENGINE
# ==========================================================