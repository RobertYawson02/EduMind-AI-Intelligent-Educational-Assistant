# ==========================================================
# AKAN / TWI LANGUAGE ENGINE
# Version 3.1
# ==========================================================
#
# Purpose:
#   Intelligent lexical search and response engine for the
#   Version 3.0 Akan knowledge base.
#
# Knowledge base:
#   data/akan/akan_knowledge_base.json
#
# Compatible with:
#   - English -> Akan
#   - Akan -> English
#   - Meaning questions
#   - Definitions
#   - Explanations
#   - Examples
#   - Synonyms
#   - Antonyms
#   - Related words
#   - Category information
#   - Question-pattern matching
#
# Version 3.1 fixes:
#   1. Request detection priority
#   2. Translation target extraction
#   3. Akan phrase false matches
#   4. "school" false match caused by "to"
#   5. Synonym handling
#   6. Related-word handling
#   7. Exact English translation priority
#   8. Akan-specific character detection
#
# ==========================================================

import json
import os
import re
import unicodedata


# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================

DATABASE_FILENAME = "akan_knowledge_base_scaled.json"


# ==========================================================
# LOAD AKAN KNOWLEDGE BASE
# ==========================================================

def load_dictionary():
    """
    Load the Version 3.0 Akan knowledge base.

    Returns:
        list: Akan knowledge records.
    """

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    file_path = os.path.join(
        base_dir,
        "data",
        "akan",
        DATABASE_FILENAME
    )

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if not isinstance(data, list):

            print(
                "WARNING: Akan knowledge base must contain a JSON list."
            )

            return []

        print(
            f"Akan Knowledge Base Loaded: {len(data)} records"
        )

        return data

    except FileNotFoundError:

        print(
            "WARNING: Akan knowledge base not found:"
        )

        print(
            file_path
        )

        return []

    except json.JSONDecodeError as error:

        print(
            "ERROR: Invalid Akan knowledge base JSON:"
        )

        print(
            error
        )

        return []

    except Exception as error:

        print(
            "ERROR: Akan knowledge base loading error:"
        )

        print(
            error
        )

        return []


class LazyDictionary:
    """Lazy list wrapper to defer the large Akan dataset until it is actually used."""

    def __init__(self, loader):
        self.loader = loader
        self._cache = None

    def _load(self):
        if self._cache is None:
            self._cache = self.loader()
        return self._cache

    def __iter__(self):
        return iter(self._load())

    def __len__(self):
        return len(self._load())

    def __getitem__(self, key):
        return self._load()[key]

    def __bool__(self):
        return bool(self._load())

    def __repr__(self):
        return repr(self._load())


# Load database once when module is imported.
dictionary = LazyDictionary(load_dictionary)


# ==========================================================
# TEXT NORMALIZATION
# ==========================================================

def normalize_text(text):
    """
    Normalize text while preserving Akan characters.

    Important Akan characters:
        ɔ
        ɛ
        ŋ
    """

    if text is None:

        return ""

    text = str(text)

    text = unicodedata.normalize(
        "NFC",
        text
    )

    text = text.lower().strip()

    # Normalize quotation marks.
    text = text.replace(
        "’",
        "'"
    )

    text = text.replace(
        "‘",
        "'"
    )

    text = text.replace(
        "“",
        '"'
    )

    text = text.replace(
        "”",
        '"'
    )

    # Keep Unicode word characters and Akan characters.
    text = re.sub(
        r"[^\w\sɔɛŋ]",
        " ",
        text,
        flags=re.UNICODE
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==========================================================
# WORD / PHRASE MATCHING
# ==========================================================

def contains_exact_phrase(text, phrase):
    """
    Match whole words or whole phrases only.

    Prevents:
        to -> school
        to -> words
    """

    text = normalize_text(text)
    phrase = normalize_text(phrase)

    if not text or not phrase:
        return False

    pattern = r"(?<!\w)" + re.escape(phrase) + r"(?!\w)"

    return bool(re.search(pattern, text, flags=re.UNICODE))

# ==========================================================
# CLEAN QUESTION
# ==========================================================

def clean_question(question):
    """
    Remove common question instructions while preserving
    the likely lexical target.
    """

    if not question:

        return ""

    question = normalize_text(
        question
    )

    remove_patterns = [

        "what is",
        "what are",
        "what does",
        "what do",
        "what means",
        "meaning of",
        "meaning",
        "define",
        "definition of",
        "definition",
        "explain",
        "explanation of",
        "translate",
        "translation of",
        "in twi",
        "into twi",
        "in akan",
        "into akan",
        "akan meaning",
        "twi meaning",
        "please",
        "give me",
        "tell me",
        "show me"

    ]

    for pattern in remove_patterns:

        question = re.sub(
            r"(?<!\w)"
            + re.escape(pattern)
            + r"(?!\w)",
            " ",
            question
        )

    question = re.sub(
        r"\s+",
        " ",
        question
    )

    return question.strip()


# ==========================================================
# SAFE FIELD ACCESS
# ==========================================================

def get_field(
    entry,
    field,
    default=""
):
    """
    Safely retrieve a field from a record.
    """

    if not isinstance(
        entry,
        dict
    ):

        return default

    value = entry.get(
        field,
        default
    )

    if value is None:

        return default

    return value


# ==========================================================
# NORMALIZE LIST
# ==========================================================

def normalize_list(value):
    """
    Convert a list field into clean strings.
    """

    if value is None:

        return []

    if isinstance(
        value,
        str
    ):

        value = [value]

    if not isinstance(
        value,
        (list, tuple, set)
    ):

        return []

    return [

        str(item).strip()

        for item in value

        if str(item).strip()

    ]


# ==========================================================
# RECORD SEARCH HELPERS
# ==========================================================

def get_akan_term(entry):

    return normalize_text(
        get_field(
            entry,
            "akan_term"
        )
    )


def get_english_term(entry):

    return normalize_text(
        get_field(
            entry,
            "english_term"
        )
    )


def get_keywords_akan(entry):

    return normalize_list(
        get_field(
            entry,
            "keywords_akan",
            []
        )
    )


def get_keywords_english(entry):

    return normalize_list(
        get_field(
            entry,
            "keywords_english",
            []
        )
    )


def get_question_patterns(entry):

    return normalize_list(
        get_field(
            entry,
            "question_patterns",
            []
        )
    )


def get_synonyms_akan(entry):

    return normalize_list(
        get_field(
            entry,
            "synonyms_akan",
            []
        )
    )


def get_synonyms_english(entry):

    return normalize_list(
        get_field(
            entry,
            "synonyms_english",
            []
        )
    )


def get_antonyms_akan(entry):

    return normalize_list(
        get_field(
            entry,
            "antonyms_akan",
            []
        )
    )


def get_antonyms_english(entry):

    return normalize_list(
        get_field(
            entry,
            "antonyms_english",
            []
        )
    )


# ==========================================================
# EXACT ENGLISH SEARCH
# ==========================================================

def english_to_twi(word):
    """
    Find an Akan record using an exact English term.
    """

    word = normalize_text(
        word
    )

    if not word:

        return None

    for entry in dictionary:

        english = get_english_term(
            entry
        )

        if english == word:

            return entry

    return None


# ==========================================================
# EXACT AKAN SEARCH
# ==========================================================

def twi_to_english(word):
    """
    Find an Akan record using an exact Akan term.
    """

    word = normalize_text(
        word
    )

    if not word:

        return None

    for entry in dictionary:

        akan = get_akan_term(
            entry
        )

        if akan == word:

            return entry

    return None


# ==========================================================
# EXACT AKAN PHRASE SEARCH
# ==========================================================

def search_twi_phrase(text):

    text = normalize_text(
        text
    )

    if not text:

        return None

    # Search longer terms first.
    entries = sorted(
        dictionary,
        key=lambda item: len(
            get_akan_term(item)
        ),
        reverse=True
    )

    for entry in entries:

        akan = get_akan_term(
            entry
        )

        if not akan:

            continue

        if contains_exact_phrase(
            text,
            akan
        ):

            return entry

    return None


# ==========================================================
# EXACT ENGLISH PHRASE SEARCH
# ==========================================================

def search_english_phrase(text):

    text = normalize_text(
        text
    )

    if not text:

        return None

    entries = sorted(
        dictionary,
        key=lambda item: len(
            get_english_term(item)
        ),
        reverse=True
    )

    for entry in entries:

        english = get_english_term(
            entry
        )

        if not english:

            continue

        if contains_exact_phrase(
            text,
            english
        ):

            return entry

    return None


# ==========================================================
# SEARCH QUESTION PATTERNS
# ==========================================================

def search_question_patterns(question):

    normalized_question = normalize_text(
        question
    )

    if not normalized_question:

        return None

    for entry in dictionary:

        patterns = get_question_patterns(
            entry
        )

        for pattern in patterns:

            normalized_pattern = normalize_text(
                pattern
            )

            if not normalized_pattern:

                continue

            if contains_exact_phrase(
                normalized_question,
                normalized_pattern
            ):

                return entry

    return None


# ==========================================================
# SEARCH SYNONYMS
# ==========================================================

def search_synonyms(question):

    normalized_question = normalize_text(
        question
    )

    if not normalized_question:

        return None

    for entry in dictionary:

        synonyms_english = [
            normalize_text(item)
            for item in get_synonyms_english(entry)
        ]

        synonyms_akan = [
            normalize_text(item)
            for item in get_synonyms_akan(entry)
        ]

        candidates = (
            synonyms_english
            + synonyms_akan
        )

        for candidate in candidates:

            if not candidate:

                continue

            if contains_exact_phrase(
                normalized_question,
                candidate
            ):

                return entry

    return None


# ==========================================================
# SEARCH ANTONYMS
# ==========================================================

def search_antonyms(question):

    normalized_question = normalize_text(
        question
    )

    if not normalized_question:

        return None

    for entry in dictionary:

        antonyms_english = [
            normalize_text(item)
            for item in get_antonyms_english(entry)
        ]

        antonyms_akan = [
            normalize_text(item)
            for item in get_antonyms_akan(entry)
        ]

        candidates = (
            antonyms_english
            + antonyms_akan
        )

        for candidate in candidates:

            if not candidate:

                continue

            if contains_exact_phrase(
                normalized_question,
                candidate
            ):

                return entry

    return None


# ==========================================================
# RELATED KEYWORD SEARCH
# ==========================================================

def related_word_search(word):

    word = normalize_text(
        word
    )

    if not word:

        return None

    for entry in dictionary:

        akan_keywords = [
            normalize_text(item)
            for item in get_keywords_akan(entry)
        ]

        english_keywords = [
            normalize_text(item)
            for item in get_keywords_english(entry)
        ]

        all_keywords = (
            akan_keywords
            + english_keywords
        )

        for keyword in all_keywords:

            if contains_exact_phrase(
                word,
                keyword
            ):

                return entry

    return None


# ==========================================================
# SEARCH KEYWORDS
# ==========================================================

def search_keywords(question):

    q = normalize_text(question)

    words = set(q.split())

    best = None
    score = 0

    for entry in dictionary:

        current = 0

        akan = get_akan_term(entry)
        english = get_english_term(entry)

        candidates = [
            (akan, 12),
            (english, 12)
        ]

        for k in get_keywords_akan(entry):
            candidates.append((normalize_text(k), 4))

        for k in get_keywords_english(entry):
            candidates.append((normalize_text(k), 4))

        for candidate, weight in candidates:

            if not candidate:
                continue

            if contains_exact_phrase(q, candidate):
                current += weight

            overlap = len(set(candidate.split()) & words)

            current += overlap

        if current > score:

            score = current
            best = entry

    return best if score > 0 else None


# ==========================================================
# EXTRACT TRANSLATION TARGET
# ==========================================================

def extract_translation_target(question):

    q = normalize_text(question)

    patterns = [

        r"translate\s+(.+?)\s+into\s+(?:twi|akan)",
        r"translate\s+(.+?)\s+in\s+(?:twi|akan)",
        r"how\s+do\s+you\s+say\s+(.+?)\s+in\s+(?:twi|akan)",
        r"what\s+is\s+the\s+(?:twi|akan)\s+word\s+for\s+(.+)",
        r"(.+?)\s+in\s+(?:twi|akan)"

    ]

    for pattern in patterns:

        m = re.search(pattern, q)

        if m:
            return m.group(1).strip()

    return clean_question(question)


# ==========================================================
# EXTRACT LEXICAL TARGET
# ==========================================================

def extract_lexical_target(question):

    q = normalize_text(question)

    patterns = [

        r"what\s+does\s+(.+?)\s+mean",

        r"meaning\s+of\s+(.+)",

        r"define\s+(.+)",

        r"explain\s+(.+?)(?:\s+in\s+(?:twi|akan))?$",

        r"describe\s+(.+)",

        r"synonyms?\s+of\s+(.+)",

        r"antonyms?\s+of\s+(.+)",

        r"related\s+words?\s+(?:to|for)\s+(.+)",

        r"what\s+words?\s+are\s+related\s+to\s+(.+)",

        r"what\s+is\s+(.+)"

    ]

    for pattern in patterns:

        m = re.search(pattern, q)

        if m:

            target = m.group(1)

            target = re.sub(r"[?.!,]+$", "", target)

            return target.strip()

    return clean_question(question)

# ==========================================================
# DETECT AKAN REQUEST TYPE
# ==========================================================

def detect_akan_request(question):

    q = normalize_text(question)

    if not q:
        return "general"

    if q.startswith("explain"):

        if " in twi" in q or " in akan" in q:
            return "akan_explanation"

        return "explanation"

    if any(x in q for x in [
        "synonym",
        "synonyms",
        "another word"
    ]):
        return "synonym"

    if any(x in q for x in [
        "antonym",
        "opposite"
    ]):
        return "antonym"

    if any(x in q for x in [
        "example",
        "sentence with"
    ]):
        return "example"

    if any(x in q for x in [
        "related words",
        "related vocabulary",
        "words are related"
    ]):
        return "related"

    if q.startswith("describe"):
        return "description"

    if any(x in q for x in [
        "translate",
        "translation",
        "how do you say",
        "word for",
        " into twi",
        " into akan",
        " in twi",
        " in akan"
    ]):
        return "translation"

    if any(x in q for x in [
        "what does",
        "meaning",
        "what is",
        "define"
    ]):
        return "meaning"

    return "general"

    # ------------------------------------------------------
    # 5. Related words
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "related word",
            "related words",
            "words related",
            "related vocabulary"

        ]
    ):

        return "related"

    # ------------------------------------------------------
    # 6. Description
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "describe",
            "description"

        ]
    ):

        return "description"

    # ------------------------------------------------------
    # 7. Translation
    #
    # Checked AFTER explanation, synonym, antonym etc.
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "translate",
            "translation",
            "in twi",
            "into twi",
            "in akan",
            "into akan",
            "how do you say"

        ]
    ):

        return "translation"

    # ------------------------------------------------------
    # 8. Meaning
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "meaning",
            "what does",
            "what is",
            "define",
            "definition"

        ]
    ):

        return "meaning"

    return "general"


# ==========================================================
# FIND TARGET ENTRY
# ==========================================================

def find_target_entry(question):

    request = detect_akan_request(question)

    if request == "translation":

        target = extract_translation_target(question)

        for fn, mode in [

            (english_to_twi, "translation_english_exact"),

            (twi_to_english, "translation_akan_exact"),

            (search_english_phrase, "translation_english_phrase"),

            (search_twi_phrase, "translation_akan_phrase"),

            (search_keywords, "translation_keyword")

        ]:

            result = fn(target)

            if result:
                return result, mode

        return None, None

    target = extract_lexical_target(question)

    for fn, mode in [

        (search_question_patterns, "question_pattern"),

        (english_to_twi, "english_exact"),

        (twi_to_english, "akan_exact"),

        (search_english_phrase, "english_phrase"),

        (search_twi_phrase, "akan_phrase"),

        (search_keywords, "keyword")

    ]:

        result = fn(target if fn != search_question_patterns else question)

        if result:
            return result, mode

    return None, None

    # ======================================================
    # SYNONYMS
    # ======================================================

    if request_type == "synonym":

        target = extract_lexical_target(
            question
        )

        # First find the actual word being asked about.
        result = english_to_twi(
            target
        )

        if result:

            return result, "synonym_english_exact"

        result = twi_to_english(
            target
        )

        if result:

            return result, "synonym_akan_exact"

        result = search_english_phrase(
            target
        )

        if result:

            return result, "synonym_english_phrase"

        result = search_twi_phrase(
            target
        )

        if result:

            return result, "synonym_akan_phrase"

        result = search_keywords(
            target
        )

        if result:

            return result, "synonym_keyword"

        result = search_synonyms(
            question
        )

        if result:

            return result, "synonym_match"

        return None, None

    # ======================================================
    # ANTONYMS
    # ======================================================

    if request_type == "antonym":

        target = extract_lexical_target(
            question
        )

        result = english_to_twi(
            target
        )

        if result:

            return result, "antonym_english_exact"

        result = twi_to_english(
            target
        )

        if result:

            return result, "antonym_akan_exact"

        result = search_english_phrase(
            target
        )

        if result:

            return result, "antonym_english_phrase"

        result = search_twi_phrase(
            target
        )

        if result:

            return result, "antonym_akan_phrase"

        result = search_keywords(
            target
        )

        if result:

            return result, "antonym_keyword"

        result = search_antonyms(
            question
        )

        if result:

            return result, "antonym_match"

        return None, None

    # ======================================================
    # EXAMPLES
    # ======================================================

    if request_type == "example":

        target = extract_lexical_target(
            question
        )

        result = english_to_twi(
            target
        )

        if result:

            return result, "example_english_exact"

        result = twi_to_english(
            target
        )

        if result:

            return result, "example_akan_exact"

        result = search_english_phrase(
            target
        )

        if result:

            return result, "example_english_phrase"

        result = search_twi_phrase(
            target
        )

        if result:

            return result, "example_akan_phrase"

        result = search_keywords(
            target
        )

        if result:

            return result, "example_keyword"

        return None, None

    # ======================================================
    # RELATED WORDS
    # ======================================================

    if request_type == "related":

        target = extract_lexical_target(
            question
        )

        # Exact English first.
        result = english_to_twi(
            target
        )

        if result:

            return result, "related_english_exact"

        # Exact Akan.
        result = twi_to_english(
            target
        )

        if result:

            return result, "related_akan_exact"

        # English phrase.
        result = search_english_phrase(
            target
        )

        if result:

            return result, "related_english_phrase"

        # Keywords.
        result = related_word_search(
            target
        )

        if result:

            return result, "related_keyword"

        # General keyword fallback.
        result = search_keywords(
            target
        )

        if result:

            return result, "related_general_keyword"

        return None, None

    # ======================================================
    # DESCRIPTION
    # ======================================================

    if request_type == "description":

        target = extract_lexical_target(
            question
        )

        result = english_to_twi(
            target
        )

        if result:

            return result, "description_english_exact"

        result = twi_to_english(
            target
        )

        if result:

            return result, "description_akan_exact"

        result = search_english_phrase(
            target
        )

        if result:

            return result, "description_english_phrase"

        result = search_twi_phrase(
            target
        )

        if result:

            return result, "description_akan_phrase"

        return None, None

    # ======================================================
    # MEANING
    # ======================================================

    if request_type == "meaning":

        target = extract_lexical_target(
            question
        )

        # Exact English.
        result = english_to_twi(
            target
        )

        if result:

            return result, "meaning_english_exact"

        # Exact Akan.
        result = twi_to_english(
            target
        )

        if result:

            return result, "meaning_akan_exact"

        # English phrase.
        result = search_english_phrase(
            target
        )

        if result:

            return result, "meaning_english_phrase"

        # Akan phrase.
        result = search_twi_phrase(
            target
        )

        if result:

            return result, "meaning_akan_phrase"

        # Keywords.
        result = search_keywords(
            target
        )

        if result:

            return result, "meaning_keyword"

        return None, None

    # ======================================================
    # AKAN EXPLANATION
    # ======================================================

    if request_type == "akan_explanation":

        target = extract_lexical_target(
            question
        )

        result = english_to_twi(
            target
        )

        if result:

            return result, "akan_explanation_english_exact"

        result = twi_to_english(
            target
        )

        if result:

            return result, "akan_explanation_akan_exact"

        result = search_english_phrase(
            target
        )

        if result:

            return result, "akan_explanation_english_phrase"

        result = search_twi_phrase(
            target
        )

        if result:

            return result, "akan_explanation_akan_phrase"

        return None, None

    # ======================================================
    # GENERAL SEARCH
    # ======================================================

    # 1. Question patterns.
    result = search_question_patterns(
        question
    )

    if result:

        return result, "question_pattern"

    # 2. Exact English.
    cleaned = clean_question(
        question
    )

    result = english_to_twi(
        cleaned
    )

    if result:

        return result, "english_exact"

    # 3. Exact Akan.
    result = twi_to_english(
        cleaned
    )

    if result:

        return result, "akan_exact"

    # 4. English phrase.
    result = search_english_phrase(
        normalized_question
    )

    if result:

        return result, "english_phrase"

    # 5. Akan phrase using safe word boundaries.
    result = search_twi_phrase(
        normalized_question
    )

    if result:

        return result, "akan_phrase"

    # 6. Keyword search.
    result = search_keywords(
        question
    )

    if result:

        return result, "keyword_search"

    return None, None


# ==========================================================
# SMART AKAN SEARCH
# ==========================================================

def search_akan(question):
    """
    Public search function.

    Returns:
        tuple:
            (record, search_mode)
    """

    if not question:

        return None, None

    print(
        "Akan Search:",
        question
    )

    result, mode = find_target_entry(
        question
    )

    if result:
        public_mode = mode
        if mode in {"translation_english_exact", "english_exact"}:
            public_mode = "english_to_twi"
        elif mode in {"translation_akan_exact", "akan_exact"}:
            public_mode = "twi_to_english"
        elif mode in {"translation_english_phrase", "english_phrase"}:
            public_mode = "english_to_twi_phrase"
        elif mode in {"translation_akan_phrase", "akan_phrase"}:
            public_mode = "twi_to_english_phrase"
        elif mode in {"translation_keyword", "keyword_search", "keyword"}:
            public_mode = "keyword_search"
        return result, public_mode

    print(
        "WARNING: No Akan lexical match found."
    )

    return None, None


# ==========================================================
# DETECT AKAN-RELATED QUESTION
# ==========================================================

def is_akan_related_question(question):
    """
    Determine whether a question is related to Akan/Twi
    vocabulary.
    """

    normalized = normalize_text(
        question
    )

    if not normalized:

        return False

    # Explicit Akan/Twi request.
    if re.search(
        r"(?<!\w)(?:akan|twi)(?!\w)",
        normalized
    ):

        return True

    # Detect actual Akan-specific characters.
    if any(
        character in normalized
        for character in (
            "ɔ",
            "ɛ",
            "ŋ"
        )
    ):

        return True

    # Search for known Akan terms safely.
    for entry in dictionary:

        akan = get_akan_term(
            entry
        )

        if not akan:

            continue

        if contains_exact_phrase(
            normalized,
            akan
        ):

            return True

    # Translation requests.
    if any(
        phrase in normalized
        for phrase in [

            "translate",
            "translation",
            "into twi",
            "in twi",
            "into akan",
            "in akan"

        ]
    ):

        return True

    return False


# ==========================================================
# FORMAT TRANSLATION RESPONSE
# ==========================================================

def format_translation(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    definition_akan = get_field(
        result,
        "definition_akan",
        ""
    )

    return (
        "Akan / Twi Translation\n\n"
        f"English: {english}\n"
        f"Akan / Twi: {akan}"
        + (
            f"\n\nAkan Definition: {definition_akan}"
            if definition_akan
            else ""
        )
    )


# ==========================================================
# FORMAT MEANING RESPONSE
# ==========================================================

def format_meaning(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    definition_akan = get_field(
        result,
        "definition_akan",
        ""
    )

    definition_english = get_field(
        result,
        "definition_english",
        ""
    )

    category = get_field(
        result,
        "category",
        ""
    )

    subcategory = get_field(
        result,
        "subcategory",
        ""
    )

    response = [

        "Akan / Twi",

        f"English: {english}",

        f"Akan / Twi: {akan}"

    ]

    if definition_english:

        response.append(
            f"English Definition: {definition_english}"
        )

    if definition_akan:

        response.append(
            f"Akan Definition: {definition_akan}"
        )

    if category:

        response.append(
            f"Category: {category}"
        )

    if subcategory:

        response.append(
            f"Subcategory: {subcategory}"
        )

    return "\n\n".join(
        response
    )


# ==========================================================
# FORMAT EXPLANATION
# ==========================================================

def format_explanation(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    explanation_english = get_field(
        result,
        "definition_english",
        ""
    )

    explanation_akan = get_field(
        result,
        "explanation_akan",
        ""
    )

    response = [

        "Akan / Twi Explanation",

        f"English: {english}",

        f"Akan / Twi: {akan}"

    ]

    if explanation_english:

        response.append(
            f"English Explanation: {explanation_english}"
        )

    if explanation_akan:

        response.append(
            f"Akan Explanation: {explanation_akan}"
        )

    return "\n\n".join(
        response
    )


# ==========================================================
# FORMAT AKAN EXPLANATION
# ==========================================================

def format_akan_explanation(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    explanation_akan = get_field(
        result,
        "explanation_akan",
        ""
    )

    response = [

        "Akan / Twi Explanation",

        f"English: {english}",

        f"Akan / Twi: {akan}"

    ]

    if explanation_akan:

        response.append(
            f"Explanation: {explanation_akan}"
        )

    else:

        response.append(
            "No Akan explanation is currently recorded."
        )

    return "\n\n".join(
        response
    )


# ==========================================================
# FORMAT EXAMPLES
# ==========================================================

def format_example(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    akan_examples = normalize_list(
        get_field(
            result,
            "examples_akan",
            []
        )
    )

    english_examples = normalize_list(
        get_field(
            result,
            "examples_english",
            []
        )
    )

    response = [

        "Akan / Twi Example Usage",

        f"Word: {english}",

        f"Akan / Twi: {akan}"

    ]

    if english_examples:

        response.append(
            "English Examples:\n"
            + "\n".join(
                f"- {example}"
                for example in english_examples
            )
        )

    if akan_examples:

        response.append(
            "Akan Examples:\n"
            + "\n".join(
                f"- {example}"
                for example in akan_examples
            )
        )

    return "\n\n".join(
        response
    )


# ==========================================================
# FORMAT SYNONYMS
# ==========================================================

def format_synonyms(result):

    english = get_field(result, "english_term")
    akan = get_field(result, "akan_term")

    syn_en = get_synonyms_english(result)
    syn_ak = get_synonyms_akan(result)

    lines = [

        "Akan / Twi Synonyms",

        "",

        f"English: {english}",

        f"Akan: {akan}"

    ]

    if syn_en:
        lines.append("")
        lines.append("English Synonyms: " + ", ".join(syn_en))

    if syn_ak:
        lines.append("Akan Synonyms: " + ", ".join(syn_ak))

    if not syn_en and not syn_ak:
        lines.append("")
        lines.append("No dedicated synonyms are currently stored for this word.")

    return "\n".join(lines)


# ==========================================================
# FORMAT ANTONYMS
# ==========================================================

def format_antonyms(result):

    english = get_field(result, "english_term")
    akan = get_field(result, "akan_term")

    ant_en = get_antonyms_english(result)
    ant_ak = get_antonyms_akan(result)

    lines = [

        "Akan / Twi Antonyms",

        "",

        f"English: {english}",

        f"Akan: {akan}"

    ]

    if ant_en:
        lines.append("")
        lines.append("English Antonyms: " + ", ".join(ant_en))

    if ant_ak:
        lines.append("Akan Antonyms: " + ", ".join(ant_ak))

    if not ant_en and not ant_ak:
        lines.append("")
        lines.append("No dedicated antonyms are currently stored for this word.")

    return "\n".join(lines)

# ==========================================================
# FORMAT RELATED WORDS
# ==========================================================

def format_related(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    keywords_akan = normalize_list(
        get_field(
            result,
            "keywords_akan",
            []
        )
    )

    keywords_english = normalize_list(
        get_field(
            result,
            "keywords_english",
            []
        )
    )

    response = [

        "Related Akan / Twi Vocabulary",

        f"Word: {english}",

        f"Akan / Twi: {akan}"

    ]

    if keywords_akan:

        response.append(
            "Related Akan Keywords: "
            + ", ".join(
                keywords_akan
            )
        )

    if keywords_english:

        response.append(
            "Related English Keywords: "
            + ", ".join(
                keywords_english
            )
        )

    return "\n\n".join(
        response
    )


# ==========================================================
# FORMAT DESCRIPTION
# ==========================================================

def format_description(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    definition_english = get_field(
        result,
        "definition_english",
        ""
    )

    definition_akan = get_field(
        result,
        "definition_akan",
        ""
    )

    return (
        "Akan / Twi Description\n\n"
        f"English: {english}\n"
        f"Akan / Twi: {akan}\n\n"
        f"English: "
        f"{definition_english or 'No description recorded.'}\n\n"
        f"Akan: "
        f"{definition_akan or 'No Akan description recorded.'}"
    )


# ==========================================================
# FORMAT GENERAL RESPONSE
# ==========================================================

def format_general(result):

    english = get_field(
        result,
        "english_term",
        "N/A"
    )

    akan = get_field(
        result,
        "akan_term",
        "N/A"
    )

    definition_english = get_field(
        result,
        "definition_english",
        ""
    )

    definition_akan = get_field(
        result,
        "definition_akan",
        ""
    )

    explanation_akan = get_field(
        result,
        "explanation_akan",
        ""
    )

    examples_akan = normalize_list(
        get_field(
            result,
            "examples_akan",
            []
        )
    )

    examples_english = normalize_list(
        get_field(
            result,
            "examples_english",
            []
        )
    )

    keywords_akan = normalize_list(
        get_field(
            result,
            "keywords_akan",
            []
        )
    )

    keywords_english = normalize_list(
        get_field(
            result,
            "keywords_english",
            []
        )
    )

    category = get_field(
        result,
        "category",
        ""
    )

    subcategory = get_field(
        result,
        "subcategory",
        ""
    )

    response = [

        "Akan / Twi Vocabulary",

        f"English: {english}",

        f"Akan / Twi: {akan}"

    ]

    if definition_english:

        response.append(
            f"English Definition: {definition_english}"
        )

    if definition_akan:

        response.append(
            f"Akan Definition: {definition_akan}"
        )

    if explanation_akan:

        response.append(
            f"Akan Explanation: {explanation_akan}"
        )

    if examples_english:

        response.append(
            "English Examples:\n"
            + "\n".join(
                f"- {example}"
                for example in examples_english
            )
        )

    if examples_akan:

        response.append(
            "Akan Examples:\n"
            + "\n".join(
                f"- {example}"
                for example in examples_akan
            )
        )

    if keywords_english:

        response.append(
            "English Keywords: "
            + ", ".join(
                keywords_english
            )
        )

    if keywords_akan:

        response.append(
            "Akan Keywords: "
            + ", ".join(
                keywords_akan
            )
        )

    if category:

        response.append(
            f"Category: {category}"
        )

    if subcategory:

        response.append(
            f"Subcategory: {subcategory}"
        )

    return "\n\n".join(
        response
    )


# ==========================================================
# MAIN RESPONSE FORMATTER
# ==========================================================

def format_akan_response(
    result,
    mode=None,
    question=""
):
    """
    Convert an Akan record into a human-readable response.
    """

    if not result:

        return None

    request_type = detect_akan_request(
        question
    )

    if request_type == "translation":

        return format_translation(
            result
        )

    if request_type == "synonym":

        return format_synonyms(
            result
        )

    if request_type == "antonym":

        return format_antonyms(
            result
        )

    if request_type == "example":

        return format_example(
            result
        )

    if request_type == "related":

        return format_related(
            result
        )

    if request_type == "description":

        return format_description(
            result
        )

    if request_type == "akan_explanation":

        return format_akan_explanation(
            result
        )

    if request_type == "explanation":

        return format_explanation(
            result
        )

    if request_type == "meaning":

        return format_meaning(
            result
        )

    return format_general(
        result
    )


# ==========================================================
# DICTIONARY STATISTICS
# ==========================================================

def dictionary_statistics():
    """
    Return statistics about the Akan database.
    """

    total = len(
        dictionary
    )

    akan_entries = 0
    english_entries = 0
    akan_definitions = 0
    english_definitions = 0
    explanations = 0
    akan_examples = 0
    english_examples = 0
    keywords_akan = 0
    keywords_english = 0
    question_patterns = 0
    synonyms_akan = 0
    synonyms_english = 0
    antonyms_akan = 0
    antonyms_english = 0

    categories = {}

    for entry in dictionary:

        if get_field(
            entry,
            "akan_term"
        ):

            akan_entries += 1

        if get_field(
            entry,
            "english_term"
        ):

            english_entries += 1

        if get_field(
            entry,
            "definition_akan"
        ):

            akan_definitions += 1

        if get_field(
            entry,
            "definition_english"
        ):

            english_definitions += 1

        if get_field(
            entry,
            "explanation_akan"
        ):

            explanations += 1

        if normalize_list(
            get_field(
                entry,
                "examples_akan",
                []
            )
        ):

            akan_examples += 1

        if normalize_list(
            get_field(
                entry,
                "examples_english",
                []
            )
        ):

            english_examples += 1

        if normalize_list(
            get_field(
                entry,
                "keywords_akan",
                []
            )
        ):

            keywords_akan += 1

        if normalize_list(
            get_field(
                entry,
                "keywords_english",
                []
            )
        ):

            keywords_english += 1

        if normalize_list(
            get_field(
                entry,
                "question_patterns",
                []
            )
        ):

            question_patterns += 1

        if get_synonyms_akan(
            entry
        ):

            synonyms_akan += 1

        if get_synonyms_english(
            entry
        ):

            synonyms_english += 1

        if get_antonyms_akan(
            entry
        ):

            antonyms_akan += 1

        if get_antonyms_english(
            entry
        ):

            antonyms_english += 1

        category = get_field(
            entry,
            "subcategory",
            "unknown"
        )

        categories[category] = (
            categories.get(
                category,
                0
            )
            + 1
        )

    return {

        "total_entries":
            total,

        "akan_entries":
            akan_entries,

        "english_entries":
            english_entries,

        "akan_definitions":
            akan_definitions,

        "english_definitions":
            english_definitions,

        "akan_explanations":
            explanations,

        "records_with_akan_examples":
            akan_examples,

        "records_with_english_examples":
            english_examples,

        "records_with_akan_keywords":
            keywords_akan,

        "records_with_english_keywords":
            keywords_english,

        "records_with_question_patterns":
            question_patterns,

        "records_with_akan_synonyms":
            synonyms_akan,

        "records_with_english_synonyms":
            synonyms_english,

        "records_with_akan_antonyms":
            antonyms_akan,

        "records_with_english_antonyms":
            antonyms_english,

        "categories":
            categories

    }


# ==========================================================
# TEST AKAN ENGINE
# ==========================================================

def test_akan_engine():

    print(
        "\n=================================================="
    )

    print(
        "AKAN ENGINE VERSION 3.1 TEST"
    )

    print(
        "=================================================="
    )

    print(
        "\nDictionary Statistics:"
    )

    stats = dictionary_statistics()

    for key, value in stats.items():

        print(
            f"{key}: {value}"
        )

    questions = [

        "What is water?",

        "What does nsuo mean?",

        "Explain nsuo.",

        "Explain nsuo in Twi.",

        "Translate water into Twi.",

        "Translate computer into Twi.",

        "How do you say water in Twi?",

        "What is the Twi word for school?",

        "Give me an example of water.",

        "What are synonyms of water?",

        "What are antonyms of love?",

        "What words are related to school?",

        "Describe love.",

        "What is ɔbarima?",

        "What does akokɔ mean?",

        "What is nsuo in English?",

        "Translate nsuo into English."

    ]

    for question in questions:

        print(
            "\n--------------------------------------------------"
        )

        print(
            "Question:",
            question
        )

        print(
            "Detected request type:",
            detect_akan_request(
                question
            )
        )

        if detect_akan_request(
            question
        ) == "translation":

            print(
                "Translation target:",
                extract_translation_target(
                    question
                )
            )

        result, mode = search_akan(
            question
        )

        if result:

            print(
                "Search mode:",
                mode
            )

            print(
                format_akan_response(
                    result,
                    mode,
                    question
                )
            )

        else:

            print(
                "No result found."
            )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_akan_engine()