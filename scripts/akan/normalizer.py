"""
==============================================================
AKAN / TWI TEXT NORMALIZER
Version 3.0
==============================================================

Normalizes Akan/Twi and English text for:

    - Search
    - Retrieval
    - Question processing
    - Lexicon matching
    - Knowledge-base lookup
    - Translation support

Important:
    Akan characters such as ɔ and ɛ must be preserved.
==============================================================
"""

from __future__ import annotations

import re
import unicodedata


# ============================================================
# VERSION
# ============================================================

NORMALIZER_VERSION = "3.0"


# ============================================================
# AKAN CHARACTERS
# ============================================================

AKAN_CHARACTERS = {
    "ɔ",
    "Ɔ",
    "ɛ",
    "Ɛ",
}


# ============================================================
# UNICODE NORMALIZATION
# ============================================================

def normalize_unicode(text: str) -> str:
    """
    Normalize Unicode representation while preserving Akan
    characters and accents.
    """

    if text is None:
        return ""

    return unicodedata.normalize(
        "NFC",
        str(text)
    )


# ============================================================
# WHITESPACE NORMALIZATION
# ============================================================

def normalize_whitespace(text: str) -> str:
    """
    Replace repeated whitespace with a single space.
    """

    return re.sub(
        r"\s+",
        " ",
        text
    ).strip()


# ============================================================
# PUNCTUATION NORMALIZATION
# ============================================================

def normalize_punctuation(text: str) -> str:
    """
    Normalize common punctuation while retaining punctuation
    that may help identify a question.
    """

    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
    }

    for old, new in replacements.items():
        text = text.replace(
            old,
            new
        )

    return text


# ============================================================
# BASIC NORMALIZATION
# ============================================================

def normalize_text(text: str) -> str:
    """
    Perform safe general normalization.

    This function does NOT lowercase the text.
    """

    if text is None:
        return ""

    text = normalize_unicode(
        text
    )

    text = normalize_punctuation(
        text
    )

    text = normalize_whitespace(
        text
    )

    return text


# ============================================================
# SEARCH NORMALIZATION
# ============================================================

def normalize_for_search(text: str) -> str:
    """
    Normalize text for retrieval and search.

    Casefolding is used instead of lower() so that Unicode
    characters are handled more consistently.
    """

    text = normalize_text(
        text
    )

    return text.casefold()


# ============================================================
# REMOVE SEARCH PUNCTUATION
# ============================================================

def remove_search_punctuation(text: str) -> str:
    """
    Remove punctuation that normally does not contribute to
    semantic retrieval.

    Question marks and apostrophes are handled safely.
    """

    text = normalize_for_search(
        text
    )

    text = re.sub(
        r"[^\w\sɔɛƆƐ+#.-]",
        " ",
        text,
        flags=re.UNICODE
    )

    return normalize_whitespace(
        text
    )


# ============================================================
# TOKENIZATION
# ============================================================

def tokenize(text: str) -> list[str]:
    """
    Convert normalized text into searchable tokens.

    Akan-specific characters are preserved.
    """

    text = remove_search_punctuation(
        text
    )

    return re.findall(
        r"[A-Za-zÀ-ÖØ-öø-ÿƆɔƐɛ0-9+#.-]+",
        text,
        flags=re.UNICODE
    )


# ============================================================
# NORMALIZED TOKENS
# ============================================================

def normalized_tokens(
    text: str
) -> list[str]:
    """
    Return unique normalized tokens while preserving order.
    """

    tokens = tokenize(
        text
    )

    result = []
    seen = set()

    for token in tokens:

        token = token.casefold()

        if not token:
            continue

        if token in seen:
            continue

        seen.add(token)

        result.append(
            token
        )

    return result


# ============================================================
# QUESTION NORMALIZATION
# ============================================================

def normalize_question(
    question: str
) -> str:
    """
    Normalize a user question while preserving its meaning.
    """

    question = normalize_text(
        question
    )

    if not question:
        return ""

    # Ensure a clean terminal question mark when the input
    # already appears to be a question.
    if (
        question.endswith("?")
        or re.match(
            r"^(what|why|how|who|where|when|which|can|does|do|is|are)\b",
            question,
            flags=re.IGNORECASE
        )
    ):
        question = question.rstrip(
            " ?"
        ) + "?"

    return question


# ============================================================
# COLLAPSE REPEATED CHARACTERS
# ============================================================

def reduce_repeated_characters(
    text: str
) -> str:
    """
    Reduce accidental repeated characters.

    Example:

        "heelloo" -> "helo"

    This is deliberately conservative and should not be used
    as a linguistic correction system.
    """

    text = normalize_text(
        text
    )

    return re.sub(
        r"(.)\1{2,}",
        r"\1",
        text,
        flags=re.UNICODE
    )


# ============================================================
# NORMALIZATION PIPELINE
# ============================================================

def normalize_pipeline(
    text: str,
    for_search: bool = False
) -> str:
    """
    Run the complete normalization pipeline.
    """

    text = normalize_text(
        text
    )

    text = reduce_repeated_characters(
        text
    )

    if for_search:

        text = remove_search_punctuation(
            text
        )

    return text


# ============================================================
# COMPARISON
# ============================================================

def normalized_equal(
    first: str,
    second: str
) -> bool:
    """
    Compare two pieces of text after safe normalization.
    """

    return (
        normalize_for_search(first)
        ==
        normalize_for_search(second)
    )


# ============================================================
# EMPTY CHECK
# ============================================================

def is_empty(text: str) -> bool:
    """
    Determine whether normalized text is empty.
    """

    return not bool(
        normalize_text(text)
    )


# ============================================================
# EXPORT
# ============================================================

__all__ = [
    "NORMALIZER_VERSION",
    "AKAN_CHARACTERS",
    "normalize_unicode",
    "normalize_whitespace",
    "normalize_punctuation",
    "normalize_text",
    "normalize_for_search",
    "remove_search_punctuation",
    "tokenize",
    "normalized_tokens",
    "normalize_question",
    "reduce_repeated_characters",
    "normalize_pipeline",
    "normalized_equal",
    "is_empty",
]
