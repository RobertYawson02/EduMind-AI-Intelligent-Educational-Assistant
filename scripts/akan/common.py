"""
==============================================================
AKAN COMMON KNOWLEDGE UTILITIES
Version 3.0
==============================================================

Shared utilities for the Akan/Twi knowledge subsystem.

The Akan subsystem is designed to support:

    - General Akan questions
    - Akan language questions
    - Akan educational questions
    - Akan culture and history
    - Akan vocabulary
    - Akan-English translation
    - Subject-specific academic knowledge in Akan

This module does NOT perform translation by itself.
It provides the common data and processing structures used
by the Akan generators and retrieval system.
==============================================================
"""

from __future__ import annotations

import re
import unicodedata
from typing import Any


# ============================================================
# VERSION
# ============================================================

AKAN_VERSION = "3.0"


# ============================================================
# SUPPORTED LANGUAGES
# ============================================================

AKAN_LANGUAGE_CODES = {
    "akan": "ak",
    "twi": "tw",
    "english": "en",
}


# ============================================================
# AKAN DOMAINS
# ============================================================

AKAN_DOMAINS = [
    "Akan Language",
    "Akan General Knowledge",
    "Akan Culture",
    "Akan History",
    "Akan Education",
    "Akan Proverbs",
    "Akan Vocabulary",
    "Akan Literature",
    "Akan Society",
    "Akan Traditions",
    "Akan Religion and Belief",
    "Akan Geography",
    "Akan Science Education",
    "Akan Mathematics Education",
    "Akan Computer Science Education",
    "Akan Technology Education",
    "Akan Business Education",
    "Akan Health Education",
    "Akan Translation",
]


# ============================================================
# KNOWLEDGE INTENTS
# ============================================================

AKAN_INTENTS = [
    "definition",
    "meaning",
    "explanation",
    "examples",
    "uses",
    "applications",
    "importance",
    "characteristics",
    "types",
    "functions",
    "components",
    "principles",
    "benefits",
    "limitations",
    "advantages",
    "disadvantages",
    "history",
    "process",
    "steps",
    "comparison",
    "difference",
    "causes",
    "effects",
    "significance",
    "cultural_context",
    "language_usage",
    "translation",
    "proverb_meaning",
    "exam_question",
    "revision",
]


# ============================================================
# QUESTION INTENTS
# ============================================================

QUESTION_INTENTS = {
    "definition",
    "meaning",
    "explanation",
    "examples",
    "comparison",
    "difference",
    "translation",
    "history",
    "culture",
    "education",
    "general_question",
}


# ============================================================
# STOP WORDS
# ============================================================

AKAN_STOP_WORDS = {
    "na",
    "ne",
    "yɛ",
    "ye",
    "de",
    "no",
    "mu",
    "ho",
    "so",
    "ma",
    "me",
    "wo",
    "mo",
    "ɔ",
    "a",
    "an",
    "the",
    "is",
    "are",
    "what",
    "how",
    "why",
    "who",
    "where",
    "when",
    "which",
    "this",
    "that",
}


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text: Any) -> str:
    """
    Normalize Akan/Twi or English text while preserving
    meaningful Akan characters such as:

        ɔ
        ɛ
        Ɛ
        Ɔ

    The function removes unnecessary whitespace and Unicode
    inconsistencies without stripping Akan characters.
    """

    if text is None:
        return ""

    text = str(text)

    text = unicodedata.normalize(
        "NFC",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# LOWERCASE NORMALIZATION
# ============================================================

def normalize_for_search(text: Any) -> str:
    """
    Normalize text for search and matching.
    """

    text = normalize_text(text)

    return text.casefold()


# ============================================================
# TOKENIZATION
# ============================================================

def tokenize(text: Any) -> list[str]:
    """
    Tokenize Akan/Twi or English text.

    Akan characters are preserved.
    """

    text = normalize_for_search(text)

    tokens = re.findall(
        r"[a-zA-ZÀ-ÖØ-öø-ÿƐɛƆɔ0-9+#.-]+",
        text
    )

    return tokens


# ============================================================
# KEYWORD GENERATION
# ============================================================

def make_keywords(
    topic: str,
    category: str,
    aliases: list[str] | None = None,
) -> list[str]:
    """
    Generate searchable keywords for Akan knowledge records.
    """

    topic = normalize_text(topic)
    category = normalize_text(category)

    aliases = aliases or []

    keywords: list[str] = []

    # Full topic
    if topic:
        keywords.append(
            normalize_for_search(topic)
        )

    # Category
    if category:
        keywords.append(
            normalize_for_search(category)
        )

    # Aliases
    for alias in aliases:

        alias = normalize_text(alias)

        if alias:
            keywords.append(
                normalize_for_search(alias)
            )

    # Individual words
    for word in tokenize(topic):

        if word in AKAN_STOP_WORDS:
            continue

        if len(word) > 1:
            keywords.append(word)

    # Search-oriented phrases
    search_phrases = [
        "meaning",
        "definition",
        "explanation",
        "examples",
        "uses",
        "importance",
        "types",
        "history",
        "culture",
        "education",
        "translation",
        "Akan",
        "Twi",
    ]

    for phrase in search_phrases:

        keywords.append(
            f"{normalize_for_search(topic)} {phrase}"
        )

    # Remove duplicates while preserving order
    unique_keywords = []
    seen = set()

    for keyword in keywords:

        keyword = normalize_for_search(keyword)

        if not keyword:
            continue

        if keyword in seen:
            continue

        seen.add(keyword)
        unique_keywords.append(keyword)

    return unique_keywords[:50]


# ============================================================
# DEFAULT EXAMPLES
# ============================================================

def default_examples(topic: str) -> list[str]:
    """
    Generate safe baseline examples.
    """

    topic = normalize_text(topic)

    return [
        f"{topic} wɔ sukuu mu",
        f"{topic} wɔ asetena mu",
        f"{topic} wɔ Akan amammerɛ mu",
        f"{topic} wɔ nnɛyi wiase mu",
        f"{topic} ho nhwɛso",
    ]


# ============================================================
# BASE ANSWER GENERATOR
# ============================================================

def generate_answer(
    topic: str,
    category: str,
    intent: str,
) -> str:
    """
    Generate a baseline answer structure.

    Important:
        This is a structural fallback.
        Subject-specific Akan generators should provide
        more accurate content wherever possible.
    """

    topic = normalize_text(topic)
    category = normalize_text(category)
    intent = normalize_text(intent)

    templates = {

        "definition":
            f"{topic} yɛ adwene anaa asɛm a ɛho hia wɔ {category} mu.",

        "meaning":
            f"{topic} kyerɛ adwene anaa nkyerɛase bi a ɛwɔ {category} mu.",

        "explanation":
            f"{topic} boa ma yɛte nsɛm ne nnyinasosɛm a ɛfa {category} ho ase.",

        "examples":
            f"{topic} ho nhwɛso betumi aba wɔ sukuu, asetena, adwuma ne da biara asetena mu.",

        "uses":
            f"Wɔde {topic} yɛ nneɛma ahorow a ɛfa {category} ho.",

        "applications":
            f"Wobetumi de {topic} ayɛ adwuma wɔ sukuu, nhwehwɛmu, adwuma ne asetena mu.",

        "importance":
            f"{topic} ho hia efisɛ ɛboa ma yɛte {category} mu nsɛm ase na yɛde nimdeɛ no di dwuma.",

        "characteristics":
            f"{topic} wɔ su ahorow a ɛboa ma yɛhunu ne sɛnea ɛyɛ soronko wɔ nneɛma foforo ho.",

        "types":
            f"{topic} betumi anya ahorow anaa nkyekyɛmu a egyina ne dwumadi ne ne nhyehyɛe so.",

        "history":
            f"{topic} wɔ abakɔsɛm a ɛkyerɛ sɛnea ɛbae, sɛnea ɛyɛɛ nsakrae ne sɛnea wɔde di dwuma nnɛ.",

        "comparison":
            f"Yɛbɛtumi de {topic} atoto nsɛm foforo ho denam wɔn nkyerɛase, wɔn su ne wɔn dwumadi a yɛhwɛ so.",

        "difference":
            f"Nsonsonoe a ɛda {topic} ne adwene foforo ntam gyina wɔn nkyerɛase, wɔn su ne wɔn dwumadi so.",

        "translation":
            f"{topic} nkyerɛase gyina nsɛm no mu ntease ne baabi a wɔde asɛm no redi dwuma so.",

        "proverb_meaning":
            f"Akyerɛde a ɛwɔ {topic} mu betumi ama yɛanya afotu, nyansa ne asetena mu nkyerɛkyerɛ.",

        "exam_question":
            f"Nsɛmmisa: Kyerɛkyerɛ {topic} mu, ma ne nkyerɛase, na fa nhwɛso ma.",

        "revision":
            f"Ntotoeɛ: Kae {topic} nkyerɛase, ne su, ne dwumadi ne nhwɛso ahorow.",
    }

    return templates.get(
        intent,
        templates["definition"]
    )


# ============================================================
# BUILD RECORD
# ============================================================

def build_record(
    topic: str,
    category: str,
    intent: str,
    answer: str | None = None,
    examples: list[str] | None = None,
    aliases: list[str] | None = None,
    language: str = "ak",
    education_level: str = "university",
    difficulty: str = "intermediate",
    source: str | None = None,
) -> dict:
    """
    Build one standardized Akan knowledge record.
    """

    topic = normalize_text(topic)
    category = normalize_text(category)
    intent = normalize_text(intent)

    if answer is None:

        answer = generate_answer(
            topic,
            category,
            intent
        )

    if examples is None:

        examples = default_examples(
            topic
        )

    record = {
        "topic": (
            f"{topic} - "
            f"{intent.replace('_', ' ').title()}"
        ),

        "keywords": make_keywords(
            topic,
            category,
            aliases
        ),

        "definition": (
            f"{intent.replace('_', ' ').title()} "
            f"of {topic}"
        ),

        "explanation": normalize_text(
            answer
        ),

        "examples": [
            normalize_text(example)
            for example in examples
            if normalize_text(example)
        ],

        "category": category,

        "intent": intent,

        "language": language,

        "education_level": education_level,

        "difficulty": difficulty,
    }

    if source:

        record["source"] = normalize_text(
            source
        )

    return record


# ============================================================
# BUILD KNOWLEDGE FAMILY
# ============================================================

def build_knowledge_family(
    topic: str,
    category: str,
    aliases: list[str] | None = None,
    language: str = "ak",
    education_level: str = "university",
    difficulty: str = "intermediate",
    intents: list[str] | None = None,
) -> list[dict]:
    """
    Generate multiple knowledge records for one Akan concept.
    """

    records = []

    selected_intents = (
        intents
        if intents is not None
        else AKAN_INTENTS
    )

    for intent in selected_intents:

        records.append(
            build_record(
                topic=topic,
                category=category,
                intent=intent,
                aliases=aliases,
                language=language,
                education_level=education_level,
                difficulty=difficulty,
            )
        )

    return records


# ============================================================
# VALIDATION
# ============================================================

def validate_record(record: dict) -> bool:
    """
    Validate an Akan knowledge record.
    """

    required = {
        "topic",
        "keywords",
        "definition",
        "explanation",
        "examples",
        "category",
        "intent",
        "language",
        "education_level",
        "difficulty",
    }

    if not isinstance(record, dict):
        return False

    if not required.issubset(
        record.keys()
    ):
        return False

    if not isinstance(
        record["topic"],
        str
    ) or not record["topic"].strip():

        return False

    if not isinstance(
        record["keywords"],
        list
    ) or not record["keywords"]:

        return False

    if not isinstance(
        record["definition"],
        str
    ):

        return False

    if not isinstance(
        record["explanation"],
        str
    ) or not record["explanation"].strip():

        return False

    if not isinstance(
        record["examples"],
        list
    ):

        return False

    if not isinstance(
        record["category"],
        str
    ) or not record["category"].strip():

        return False

    if not isinstance(
        record["intent"],
        str
    ) or not record["intent"].strip():

        return False

    if record["language"] not in {
        "ak",
        "tw",
        "en",
    }:

        return False

    return True


# ============================================================
# DUPLICATE KEY
# ============================================================

def record_key(record: dict) -> str:
    """
    Generate a stable duplicate key.
    """

    return "|".join([
        normalize_for_search(
            record.get("language", "")
        ),

        normalize_for_search(
            record.get("category", "")
        ),

        normalize_for_search(
            record.get("topic", "")
        ),

        normalize_for_search(
            record.get("intent", "")
        ),
    ])
