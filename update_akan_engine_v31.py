from pathlib import Path
import re


# ==========================================================
# AKAN ENGINE V3.1 PATCHER
# ==========================================================
#
# Fixes:
#   1. Request detection priority
#   2. Translation search priority
#   3. School false-match problem
#   4. Synonym handling
#
# ==========================================================


TARGET = Path("model") / "akan_engine.py"


# ==========================================================
# CHECK TARGET
# ==========================================================

if not TARGET.exists():

    print()
    print("ERROR: Target file was not found:")
    print(TARGET)
    print()
    print("Make sure you are running this script from")
    print("the project root directory.")
    raise SystemExit(1)


# ==========================================================
# LOAD FILE
# ==========================================================

text = TARGET.read_text(
    encoding="utf-8"
)

original_text = text


# ==========================================================
# HELPER FOR SAFE FUNCTION REPLACEMENT
# ==========================================================

def replace_function(
    source,
    function_name,
    new_function,
    next_function
):

    pattern = (
        rf"def {re.escape(function_name)}\(.*?"
        rf"(?=\ndef {re.escape(next_function)}\()"
    )

    match = re.search(
        pattern,
        source,
        flags=re.S
    )

    if not match:

        print(
            f"WARNING: Could not find function: "
            f"{function_name}"
        )

        return source

    return (
        source[:match.start()]
        + new_function.rstrip()
        + "\n\n"
        + source[match.end():]
    )


# ==========================================================
# FIX 1
# REQUEST DETECTION
# ==========================================================

new_detect_request = r'''
def detect_akan_request(question):

    q = normalize_text(
        question
    )

    if not q:

        return "general"

    # ------------------------------------------------------
    # IMPORTANT:
    # Specific request types must be checked BEFORE
    # general explanation/meaning detection.
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Akan explanation
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "explain in twi",
            "explain in akan",
            "explanation in twi",
            "explanation in akan",
            "twi explanation",
            "akan explanation"

        ]
    ):

        return "akan_explanation"

    # ------------------------------------------------------
    # Translation
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "translate",
            "translation",
            "translate into twi",
            "translate into akan",
            "in twi",
            "into twi",
            "in akan",
            "into akan",
            "how do you say"

        ]
    ):

        return "translation"

    # ------------------------------------------------------
    # Synonyms
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "synonym",
            "synonyms",
            "another word for",
            "similar word",
            "similar words"

        ]
    ):

        return "synonym"

    # ------------------------------------------------------
    # Antonyms
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "antonym",
            "antonyms",
            "opposite word",
            "opposite words",
            "opposite meaning"

        ]
    ):

        return "antonym"

    # ------------------------------------------------------
    # Examples
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "example",
            "examples",
            "use it in a sentence",
            "use in a sentence",
            "sentence with",
            "give me a sentence"

        ]
    ):

        return "example"

    # ------------------------------------------------------
    # Related words
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "related word",
            "related words",
            "related vocabulary",
            "words related"

        ]
    ):

        return "related"

    # ------------------------------------------------------
    # Description
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
    # General explanation
    # ------------------------------------------------------

    if any(
        phrase in q
        for phrase in [

            "explain",
            "explanation"

        ]
    ):

        return "explanation"

    # ------------------------------------------------------
    # Meaning
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
'''


text = replace_function(
    text,
    "detect_akan_request",
    new_detect_request,
    "find_target_entry"
)


# ==========================================================
# FIX 2
# KEYWORD SEARCH
# ==========================================================

new_search_keywords = r'''
def search_keywords(question):

    normalized_question = normalize_text(
        question
    )

    if not normalized_question:

        return None

    words = set(
        normalized_question.split()
    )

    best_entry = None
    best_score = 0

    for entry in dictionary:

        score = 0

        akan_term = get_akan_term(
            entry
        )

        english_term = get_english_term(
            entry
        )

        akan_keywords = [
            normalize_text(item)
            for item in get_keywords_akan(entry)
        ]

        english_keywords = [
            normalize_text(item)
            for item in get_keywords_english(entry)
        ]

        candidates = (
            [akan_term, english_term]
            + akan_keywords
            + english_keywords
        )

        for candidate in candidates:

            if not candidate:

                continue

            # ------------------------------------------------
            # Exact complete phrase.
            #
            # Prevents words such as "to" from matching
            # inside unrelated words such as "school".
            # ------------------------------------------------

            padded_question = (
                " "
                + normalized_question
                + " "
            )

            padded_candidate = (
                " "
                + candidate
                + " "
            )

            if padded_candidate in padded_question:

                score += 8

            # ------------------------------------------------
            # Individual word overlap.
            # ------------------------------------------------

            candidate_words = set(
                candidate.split()
            )

            overlap = candidate_words.intersection(
                words
            )

            # Do not allow extremely short words to dominate
            # a search result.
            meaningful_overlap = {

                word
                for word in overlap

                if len(word) >= 3

            }

            score += len(
                meaningful_overlap
            )

        if score > best_score:

            best_score = score
            best_entry = entry

    if best_entry and best_score >= 6:

        return best_entry

    return None
'''


text = replace_function(
    text,
    "search_keywords",
    new_search_keywords,
    "detect_akan_request"
)


# ==========================================================
# FIX 3
# FIND TARGET ENTRY
# ==========================================================

new_find_target = r'''
def find_target_entry(question):

    if not question:

        return None, None

    normalized_question = normalize_text(
        question
    )

    request_type = detect_akan_request(
        question
    )

    # ------------------------------------------------------
    # 1. Question-pattern search
    # ------------------------------------------------------

    result = search_question_patterns(
        question
    )

    if result:

        return result, "question_pattern"

    # ------------------------------------------------------
    # 2. For translation requests:
    #
    # Translation gets priority.
    #
    # We first remove the instruction words and then search
    # the actual requested word.
    # ------------------------------------------------------

    if request_type == "translation":

        translation_search_text = re.sub(
            r"\b(?:translate|translation|into|in|twi|akan|"
            r"please|how|do|you|say)\b",
            " ",
            normalized_question
        )

        translation_search_text = re.sub(
            r"\s+",
            " ",
            translation_search_text
        ).strip()

        # --------------------------------------------------
        # Exact English search FIRST.
        # --------------------------------------------------

        result = english_to_twi(
            translation_search_text
        )

        if result:

            return result, "english_exact"

        # --------------------------------------------------
        # Exact Akan search SECOND.
        # --------------------------------------------------

        result = twi_to_english(
            translation_search_text
        )

        if result:

            return result, "akan_exact"

        # --------------------------------------------------
        # Phrase search.
        # --------------------------------------------------

        result = search_english_phrase(
            translation_search_text
        )

        if result:

            return result, "english_phrase"

        result = search_twi_phrase(
            translation_search_text
        )

        if result:

            return result, "akan_phrase"

    # ------------------------------------------------------
    # 3. Exact Akan term search.
    #
    # This is useful for:
    #
    # What does nsuo mean?
    # Explain nsuo.
    # What is ɔbarima?
    # ------------------------------------------------------

    for entry in sorted(
        dictionary,
        key=lambda item: len(
            get_akan_term(item)
        ),
        reverse=True
    ):

        akan = get_akan_term(
            entry
        )

        if not akan:

            continue

        padded_question = (
            " "
            + normalized_question
            + " "
        )

        padded_akan = (
            " "
            + akan
            + " "
        )

        if padded_akan in padded_question:

            return entry, "akan_phrase"

    # ------------------------------------------------------
    # 4. Exact English search.
    # ------------------------------------------------------

    cleaned_question = clean_question(
        question
    )

    result = english_to_twi(
        cleaned_question
    )

    if result:

        return result, "english_exact"

    # ------------------------------------------------------
    # 5. Exact Akan search after cleaning.
    # ------------------------------------------------------

    result = twi_to_english(
        cleaned_question
    )

    if result:

        return result, "akan_exact"

    # ------------------------------------------------------
    # 6. English phrase search.
    # ------------------------------------------------------

    result = search_english_phrase(
        normalized_question
    )

    if result:

        return result, "english_phrase"

    # ------------------------------------------------------
    # 7. Akan phrase search.
    # ------------------------------------------------------

    result = search_twi_phrase(
        normalized_question
    )

    if result:

        return result, "akan_phrase"

    # ------------------------------------------------------
    # 8. Search multi-word phrases.
    # ------------------------------------------------------

    words = normalized_question.split()

    for size in range(
        min(6, len(words)),
        0,
        -1
    ):

        for index in range(
            len(words) - size + 1
        ):

            phrase = " ".join(
                words[
                    index:index + size
                ]
            )

            result = english_to_twi(
                phrase
            )

            if result:

                return result, "phrase_search"

            result = twi_to_english(
                phrase
            )

            if result:

                return result, "phrase_search"

    # ------------------------------------------------------
    # 9. Keyword search.
    # ------------------------------------------------------

    result = search_keywords(
        question
    )

    if result:

        return result, "keyword_search"

    # ------------------------------------------------------
    # 10. Related-word search.
    # ------------------------------------------------------

    result = related_word_search(
        cleaned_question
    )

    if result:

        return result, "related_word"

    return None, None
'''


text = replace_function(
    text,
    "find_target_entry",
    new_find_target,
    "search_akan"
)


# ==========================================================
# FIX 4
# SYNONYM FORMATTER
# ==========================================================

new_format_synonyms = r'''
def format_synonyms(result):

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

    # ------------------------------------------------------
    # Dedicated synonym fields.
    # ------------------------------------------------------

    english_synonyms = normalize_list(
        get_field(
            result,
            "synonyms",
            []
        )
    )

    akan_synonyms = normalize_list(
        get_field(
            result,
            "akan_synonyms",
            []
        )
    )

    # ------------------------------------------------------
    # Backward compatibility:
    #
    # If the database does not yet contain dedicated
    # synonym fields, use the keyword fields as a fallback.
    # ------------------------------------------------------

    if not english_synonyms:

        english_synonyms = normalize_list(
            get_field(
                result,
                "keywords_english",
                []
            )
        )

    if not akan_synonyms:

        akan_synonyms = normalize_list(
            get_field(
                result,
                "keywords_akan",
                []
            )
        )

    response = [

        "Akan / Twi Synonyms",

        f"Word: {english}",

        f"Akan / Twi: {akan}"

    ]

    if english_synonyms:

        response.append(
            "English Synonyms:\n"
            + "\n".join(
                f"- {item}"
                for item in english_synonyms
            )
        )

    else:

        response.append(
            "English Synonyms: None recorded."
        )

    if akan_synonyms:

        response.append(
            "Akan Synonyms:\n"
            + "\n".join(
                f"- {item}"
                for item in akan_synonyms
            )
        )

    else:

        response.append(
            "Akan Synonyms: None recorded."
        )

    return "\n\n".join(
        response
    )
'''


text = replace_function(
    text,
    "format_synonyms",
    new_format_synonyms,
    "format_antonyms"
)


# ==========================================================
# CREATE BACKUP
# ==========================================================

backup = TARGET.with_name(
    "akan_engine_v30_backup.py"
)

if not backup.exists():

    backup.write_text(
        original_text,
        encoding="utf-8"
    )

    print(
        "Backup created:"
    )

    print(
        backup
    )


# ==========================================================
# SAVE UPDATED ENGINE
# ==========================================================

TARGET.write_text(
    text,
    encoding="utf-8"
)


# ==========================================================
# VERIFY SYNTAX
# ==========================================================

import py_compile

try:

    py_compile.compile(
        str(TARGET),
        doraise=True
    )

except py_compile.PyCompileError as error:

    print()
    print(
        "ERROR: The updated engine contains a syntax error."
    )

    print(error)

    # Restore original
    TARGET.write_text(
        original_text,
        encoding="utf-8"
    )

    print()
    print(
        "Original engine restored."
    )

    raise SystemExit(1)


# ==========================================================
# SUCCESS
# ==========================================================

print()
print(
    "=================================================="
)

print(
    "AKAN ENGINE VERSION 3.1 UPDATE SUCCESSFUL"
)

print(
    "=================================================="
)

print()
print(
    "Fixed:"
)

print(
    "1. Request detection"
)

print(
    "2. Translation search priority"
)

print(
    "3. School false-match problem"
)

print(
    "4. Synonym handling"
)

print()
print(
    "Updated file:"
)

print(
    TARGET
)

print()
print(
    "Backup file:"
)

print(
    backup
)

print()
print(
    "Syntax check: PASSED"
)

print(
    "=================================================="
)