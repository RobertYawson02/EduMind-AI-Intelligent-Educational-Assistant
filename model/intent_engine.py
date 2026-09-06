# ==========================================================
# INTENT ENGINE
# Intelligent Educational Question Understanding
# ==========================================================

import re


# ==========================================================
# HELPER: MATCH WHOLE WORD OR PHRASE
# ==========================================================

def contains_phrase(text, phrase):
    """
    Safely checks whether a complete word or phrase
    exists in the supplied text.

    This prevents short patterns such as:
        "why"
        "is"
        "do"

    from accidentally matching inside other words.
    """

    if not text or not phrase:
        return False

    text = str(text).lower().strip()
    phrase = str(phrase).lower().strip()

    pattern = r"\b" + re.escape(phrase) + r"\b"

    return re.search(
        pattern,
        text
    ) is not None


# ==========================================================
# INTENT DETECTION
# ==========================================================

def detect_intent(question):

    # ------------------------------------------------------
    # Empty question
    # ------------------------------------------------------

    if not question or not str(question).strip():

        return "general"

    q = str(question).lower().strip()


    # ======================================================
    # GREETINGS / CONVERSATIONAL QUESTIONS
    # ======================================================

    greeting_patterns = [

        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "good night",
        "how are you",
        "how are things",
        "how is it going",
        "how's it going",
        "whats up",
        "what's up"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in greeting_patterns
    ):

        return "general"


    # ======================================================
    # TRANSLATION
    # ======================================================

    translation_patterns = [

        "translate",
        "translate this",
        "translate to twi",
        "translate into twi",
        "translate in twi",
        "into twi",
        "in twi",
        "in akan",
        "into akan"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in translation_patterns
    ):

        return "translation"


    # ======================================================
    # MEANING
    # ======================================================

    meaning_patterns = [

        "what does this mean",
        "what does",
        "what is the meaning",
        "meaning of",
        "means",
        "meaning",
        "twi meaning",
        "akan meaning"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in meaning_patterns
    ):

        return "meaning"


    # ======================================================
    # DISADVANTAGES
    # ======================================================

    disadvantage_patterns = [

        "disadvantages",
        "limitations",
        "drawbacks",
        "demerits",
        "weaknesses",
        "negative effects",
        "problems with",
        "challenges of"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in disadvantage_patterns
    ):

        return "disadvantages"


    # ======================================================
    # APPLICATIONS / USES
    # ======================================================

    application_patterns = [

        "applications of",
        "application of",
        "uses of",
        "use of",
        "where is it used",
        "where are they used",
        "where is it applied",
        "where are they applied"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in application_patterns
    ):

        return "applications"

    # Natural application questions such as "Where is AI used?" do not
    # always contain the literal phrase "uses of".
    if (
        (contains_phrase(q, "where is") or contains_phrase(q, "where are")
         or contains_phrase(q, "where can"))
        and (contains_phrase(q, "used") or contains_phrase(q, "applied")
             or contains_phrase(q, "implemented"))
    ):

        return "applications"


    # ======================================================
    # ADVANTAGES
    # ======================================================

    advantage_patterns = [

        "advantages",
        "benefits",
        "importance",
        "merits",
        "strengths",
        "positive effects",
        "why is it important"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in advantage_patterns
    ):

        return "advantages"


    # ======================================================
    # EXAMPLES
    # ======================================================

    example_patterns = [

        "give an example",
        "give examples",
        "example of",
        "examples of",
        "provide an example",
        "provide examples",
        "give me an example",
        "give me examples"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in example_patterns
    ):

        return "examples"


    # ======================================================
    # LIST / ENUMERATION
    # ======================================================

    list_patterns = [

        "list",
        "mention",
        "state",
        "name",
        "identify",
        "give five",
        "give four",
        "give three",
        "give two",
        "give some",
        "what are the types",
        "types of",
        "kinds of",
        "characteristics of",
        "features of",
        "components of",
        "functions of"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in list_patterns
    ):

        return "list"


    # ======================================================
    # PROCESS / PROCEDURE
    # ======================================================

    process_patterns = [

        "step by step",
        "steps",
        "procedure",
        "process of",
        "how to",
        "how do i",
        "how can i",
        "method of",
        "methods of",
        "stages of"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in process_patterns
    ):

        return "process"


    # ======================================================
    # CAUSES
    # ======================================================

    cause_patterns = [

        "causes of",
        "cause of",
        "what causes",
        "why does",
        "why do",
        "reasons for",
        "reason for"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in cause_patterns
    ):

        return "causes"


    # ======================================================
    # EFFECTS
    # ======================================================

    effect_patterns = [

        "effects of",
        "effect of",
        "impact of",
        "influence of",
        "consequences of",
        "results of"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in effect_patterns
    ):

        return "effects"


    # ======================================================
    # SUMMARY / REVISION
    # ======================================================

    summary_patterns = [

        "summarize",
        "summarise",
        "summary of",
        "give me a summary",
        "brief summary",
        "short summary",
        "summarise this",
        "summarize this",
        "in summary",
        "briefly explain",
        "explain briefly"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in summary_patterns
    ):

        return "summary"


    # ======================================================
    # EXAMINATION / REVISION
    # ======================================================

    exam_patterns = [

        "exam question",
        "examination question",
        "exam questions",
        "past question",
        "past questions",
        "likely exam question",
        "possible exam question",
        "revision question",
        "revision questions",
        "test question",
        "quiz question",
        "prepare me for an exam",
        "help me prepare for exam",
        "what should i know for exam",
        "exam preparation"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in exam_patterns
    ):

        return "exam"


    # ======================================================
    # CALCULATION
    # ======================================================

    calculation_patterns = [

        "calculate",
        "solve",
        "find the value",
        "work out",
        "compute",
        "equation",
        "formula",
        "how much",
        "how many"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in calculation_patterns
    ):

        return "calculation"


    # ======================================================
    # COMPARISON
    # ======================================================

    comparison_patterns = [

        "difference between",
        "differences between",
        "differentiate between",
        "differentiate",
        "compare",
        "comparison between",
        "distinguish between",
        "distinguish",
        "versus",
        "vs"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in comparison_patterns
    ):

        return "comparison"


    # ------------------------------------------------------
    # Special handling for "how is / how are"
    #
    # Do not automatically classify every question containing
    # "how is" or "how are" as a comparison.
    # ------------------------------------------------------

    if (
        contains_phrase(q, "how is")
        or contains_phrase(q, "how are")
    ):

        comparison_indicators = [

            "different",
            "difference",
            "similar",
            "same",
            "compared",
            "versus",
            "vs",
            "distinguish"

        ]

        if any(
            contains_phrase(q, indicator)
            for indicator in comparison_indicators
        ):

            return "comparison"


    # ======================================================
    # DEFINITION
    # ======================================================

    definition_patterns = [

        "what is meant by",
        "what are meant by",
        "what is",
        "what are",
        "define",
        "definition of",
        "define the term"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in definition_patterns
    ):

        return "definition"


    # ======================================================
    # EXPLANATION
    # ======================================================

    explanation_patterns = [

        "explain",
        "describe",
        "tell me about",
        "how does",
        "how do",
        "why",
        "elaborate on",
        "give details about",
        "discuss"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in explanation_patterns
    ):

        return "explanation"


    # ======================================================
    # EDUCATIONAL / STUDY
    # ======================================================

    education_patterns = [

        "lesson",
        "study",
        "learn",
        "school",
        "student",
        "course",
        "subject",
        "topic",
        "revision",
        "teach me",
        "help me understand"

    ]

    if any(
        contains_phrase(q, pattern)
        for pattern in education_patterns
    ):

        return "education"


    # ======================================================
    # GENERAL
    # ======================================================

    return "general"


# ==========================================================
# TOPIC EXTRACTION
# ==========================================================

def extract_topic(question):

    if not question or not str(question).strip():

        return ""

    q = str(question).lower().strip()


    # ======================================================
    # REMOVE COMMON QUESTION PHRASES
    # ======================================================

    remove_phrases = [

        # Definitions
        "what is meant by",
        "what are meant by",
        "what is",
        "what are",
        "what was",
        "what were",

        "define the term",
        "definition of",
        "define",

        # Meaning
        "what does this mean",
        "what does",
        "meaning of",

        # Explanation
        "explain",
        "describe",
        "tell me about",
        "discuss",
        "elaborate on",

        # Translation
        "translate this",
        "translate to twi",
        "translate into twi",
        "translate in twi",
        "translate",
        "into twi",
        "in twi",
        "into akan",
        "in akan",
        "akan meaning",
        "twi meaning",

        # Examples
        "give examples of",
        "give an example of",
        "give me examples",
        "give me an example",
        "examples of",
        "example of",

        # Applications
        "applications of the",
        "applications of",
        "application of the",
        "application of",
        "uses of the",
        "uses of",
        "use of the",
        "use of",

        # Advantages
        "advantages of the",
        "advantages of",
        "benefits of",
        "importance of",
        "merits of",

        # Disadvantages
        "disadvantages of the",
        "disadvantages of",
        "limitations of",
        "drawbacks of",

        # Lists
        "types of",
        "kinds of",
        "categories of",
        "characteristics of",
        "features of",
        "components of",
        "functions of",

        # Causes
        "causes of",
        "cause of",

        # Effects
        "effects of",
        "effect of",
        "impact of",
        "influence of",

        # Processes
        "steps in",
        "steps of",
        "process of",
        "procedure for",

        # Comparisons
        "difference between",
        "differences between",
        "differentiate between",
        "comparison between",
        "compare",

        # Lists / commands
        "list",
        "mention",
        "state",
        "identify",

        # Summary
        "summarize",
        "summarise",
        "summary of",
        "briefly explain",

        # Examination
        "exam question",
        "examination question",
        "past question",
        "revision question"

    ]


    # ======================================================
    # REMOVE PHRASES SAFELY
    # ======================================================

    for phrase in sorted(
        remove_phrases,
        key=len,
        reverse=True
    ):

        pattern = r"\b" + re.escape(phrase) + r"\b"

        q = re.sub(
            pattern,
            " ",
            q
        )


    # ======================================================
    # REMOVE COMMON CONVERSATIONAL PHRASES
    # ======================================================

    conversational_phrases = [

        "i want to know",
        "i want to understand",
        "in simple terms",
        "in simple words",
        "can you",
        "could you",
        "would you",
        "help me",
        "tell me",
        "give me",
        "show me",
        "teach me",
        "please",
        "simply",
        "briefly",
        "for me",
        "about"

    ]


    for phrase in sorted(
        conversational_phrases,
        key=len,
        reverse=True
    ):

        pattern = r"\b" + re.escape(phrase) + r"\b"

        q = re.sub(
            pattern,
            " ",
            q
        )


    # ======================================================
    # REMOVE QUESTION STRUCTURE WORDS
    # ======================================================

    structure_words = {

        "mean",
        "means",
        "meaning",

        "work",
        "works",
        "working",
        "used",
        "applied",
        "implemented",

        "explain",
        "explained",
        "explanation",

        "brief",
        "briefly",

        "calculate",
        "calculation",

        "please"

    }


    words = q.split()


    cleaned_structure = [

        word

        for word in words

        if word.strip(".,?!:;()[]{}\"'") not in structure_words

    ]


    q = " ".join(
        cleaned_structure
    )


    # ======================================================
    # REMOVE PUNCTUATION
    # ======================================================

    q = re.sub(
        r"[^\w\sɔɛ]",
        " ",
        q
    )


    # ======================================================
    # REMOVE UNNECESSARY WORDS
    # ======================================================

    unnecessary_words = {

        "the",
        "a",
        "an",
        "of",
        "is",
        "are",
        "was",
        "were",
        "do",
        "does",
        "did",
        "how",
        "why",
        "what",
        "which",
        "who",
        "where",
        "when",
        "can",
        "could",
        "would",
        "should",
        "i",
        "me",
        "my",
        "we",
        "you",
        "your",
        "please"

    }


    words = q.split()


    cleaned_words = [

        word

        for word in words

        if word not in unnecessary_words

    ]


    # ======================================================
    # RETURN CLEAN TOPIC
    # ======================================================

    topic = " ".join(
        cleaned_words
    )


    return topic.strip()


# ==========================================================
# TEST INTENT ENGINE
# ==========================================================

def test_intent_engine():

    print(
        "\n=========================================="
    )

    print(
        "🧠 INTENT ENGINE TEST"
    )

    print(
        "=========================================="
    )


    test_questions = [

        # Definition
        "What is artificial intelligence?",

        # Meaning
        "What does machine learning mean?",

        # Advantages
        "What are the advantages of artificial intelligence?",

        # Applications
        "What are the applications of artificial intelligence?",

        "Where is artificial intelligence used?",

        # Disadvantages
        "What are the disadvantages of social media?",

        # Examples
        "What are examples of machine learning?",

        "Give me examples of databases.",

        # Lists
        "List the types of computer networks.",

        # Causes
        "What are the causes of climate change?",

        # Effects
        "What are the effects of pollution?",

        # Explanation
        "Explain how machine learning works.",

        # Process
        "How do I install Python?",

        # Comparison
        "What is the difference between AI and ML?",

        "How are AI and ML different?",

        # Calculation
        "Calculate the area of a circle.",

        # Translation
        "Translate water into Twi.",

        # Akan meaning
        "What does nsuo mean in Twi?",

        # Summary
        "Summarize artificial intelligence.",

        "Give me a brief summary of networking.",

        # Education
        "Teach me about databases.",

        # Examination
        "Prepare me for an exam.",

        # Greetings
        "Hello",

        "Hi",

        "How are you?",

        "Good morning"

    ]


    for question in test_questions:

        intent = detect_intent(
            question
        )

        topic = extract_topic(
            question
        )

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

        print(
            "Topic:",
            topic
        )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_intent_engine()


# ==========================================================
# END OF INTENT ENGINE
# ==========================================================