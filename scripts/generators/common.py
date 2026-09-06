"""
==============================================================
COMMON KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Shared educational knowledge-generation utilities.

All subject generators use this module.

This module is designed to support both:
    - New Version 3 generators using intent=
    - Older generators using variation=

The generated records remain compatible with the
Intelligent Educational Assistant retrieval architecture.
"""

from __future__ import annotations

import re


# ============================================================
# KNOWLEDGE FAMILIES
# ============================================================

KNOWLEDGE_FAMILY = [
    "definition",
    "meaning",
    "explanation",
    "examples",
    "applications",
    "advantages",
    "disadvantages",
    "importance",
    "characteristics",
    "types",
    "uses",
    "functions",
    "components",
    "principles",
    "benefits",
    "limitations",
    "challenges",
    "history",
    "process",
    "steps",
    "comparison",
    "difference",
    "real_world_examples",
    "exam_question",
    "revision",
]


# ============================================================
# STOP WORDS
# ============================================================

STOP_WORDS = {
    "what",
    "is",
    "are",
    "the",
    "a",
    "an",
    "of",
    "and",
    "or",
    "to",
    "in",
    "on",
    "for",
    "with",
    "by",
    "from",
    "how",
    "why",
    "does",
    "do",
    "can",
    "could",
    "would",
    "should",
    "this",
    "that",
    "these",
    "those",
    "about",
    "give",
    "me",
    "please",
    "tell",
    "explain",
    "define",
}


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize(text: str) -> str:
    """
    Normalize whitespace and convert input to a clean string.
    """

    if text is None:
        return ""

    return re.sub(
        r"\s+",
        " ",
        str(text)
    ).strip()


# ============================================================
# KEYWORD GENERATION
# ============================================================

def make_keywords(
    topic: str,
    category: str,
    aliases: list[str] | None = None
) -> list[str]:
    """
    Generate searchable keywords for a knowledge record.
    """

    topic = normalize(topic)
    category = normalize(category)

    aliases = aliases or []

    keywords = []

    # Full topic
    if topic:
        keywords.append(topic.lower())

    # Category
    if category:
        keywords.append(category.lower())

    # Aliases
    for alias in aliases:

        alias = normalize(alias)

        if alias:
            keywords.append(alias.lower())

    # Individual topic words
    words = re.findall(
        r"[A-Za-z0-9+#.-]+",
        topic.lower()
    )

    for word in words:

        if (
            word not in STOP_WORDS
            and len(word) > 1
        ):
            keywords.append(word)

    # Educational search phrases
    phrases = [
        "definition",
        "meaning",
        "explanation",
        "examples",
        "applications",
        "uses",
        "advantages",
        "disadvantages",
        "importance",
        "characteristics",
        "types",
        "functions",
        "components",
        "principles",
        "benefits",
        "limitations",
        "challenges",
        "comparison",
        "difference",
        "exam question",
        "revision",
    ]

    for phrase in phrases:

        if topic:

            keywords.append(
                f"{topic.lower()} {phrase}"
            )

    # Remove duplicates
    unique = []
    seen = set()

    for keyword in keywords:

        keyword = normalize(
            keyword
        ).lower()

        if not keyword:
            continue

        if keyword in seen:
            continue

        seen.add(keyword)
        unique.append(keyword)

    return unique[:40]


# ============================================================
# DEFAULT EXAMPLES
# ============================================================

def default_examples(
    topic: str
) -> list[str]:
    """
    Produce general educational examples.
    """

    topic = normalize(topic)

    return [
        f"{topic} in education",
        f"{topic} in industry",
        f"{topic} in research",
        f"{topic} in business",
        f"{topic} in everyday life",
    ]


# ============================================================
# EDUCATIONAL ANSWER GENERATOR
# ============================================================

def generate_answer(
    topic: str,
    category: str,
    intent: str,
    variation: str | None = None
) -> str:
    """
    Generate a baseline educational explanation.

    variation is supported for backward compatibility with
    older generator modules.
    """

    topic = normalize(topic)
    category = normalize(category)
    intent = normalize(intent)

    templates = {

        "definition":
            f"{topic} is an important concept studied in {category}.",

        "meaning":
            f"{topic} refers to a concept, method, system, or area of study within {category.lower()}.",

        "explanation":
            f"{topic} helps learners understand important principles and practical ideas within {category.lower()}.",

        "examples":
            f"Examples of {topic} can be found in education, research, industry, business, and everyday applications.",

        "applications":
            f"{topic} can be applied in education, research, industry, business, healthcare, communication, and technology depending on its context.",

        "advantages":
            f"The advantages of {topic} may include improved efficiency, accuracy, productivity, organization, and problem solving.",

        "disadvantages":
            f"Possible disadvantages or limitations of {topic} may include cost, complexity, resource requirements, maintenance, and implementation challenges.",

        "importance":
            f"{topic} is important because it helps learners understand concepts, solve problems, develop practical skills, and make informed decisions.",

        "characteristics":
            f"The characteristics of {topic} describe its major features, properties, structure, behaviour, and distinguishing qualities.",

        "types":
            f"{topic} may have different types or classifications depending on its purpose, structure, method, or application.",

        "uses":
            f"{topic} is used to solve problems, improve processes, support learning, and achieve practical or academic objectives.",

        "functions":
            f"The functions of {topic} describe the tasks, roles, or purposes it performs within its field.",

        "components":
            f"{topic} may consist of several components that work together to achieve a specific purpose.",

        "principles":
            f"The principles of {topic} describe the fundamental rules and ideas that explain how it works or is applied.",

        "benefits":
            f"The benefits of {topic} may include improved knowledge, efficiency, productivity, innovation, accuracy, and decision-making.",

        "limitations":
            f"{topic} has limitations that should be considered when selecting, implementing, or applying it in practical situations.",

        "challenges":
            f"Common challenges involving {topic} may include technical difficulties, limited resources, security concerns, complexity, and maintenance requirements.",

        "history":
            f"The history of {topic} describes how the concept, technology, method, or field developed and changed over time.",

        "process":
            f"The process involving {topic} consists of stages or activities that work together to achieve a desired outcome.",

        "steps":
            f"Learning {topic} involves understanding its definition, principles, characteristics, applications, examples, and practical use.",

        "comparison":
            f"{topic} can be compared with related concepts by examining their definitions, purposes, characteristics, strengths, limitations, and applications.",

        "difference":
            f"The difference between {topic} and related concepts can be identified by examining their purpose, structure, characteristics, and applications.",

        "real_world_examples":
            f"Real-world applications of {topic} can be observed in education, business, research, industry, healthcare, government, and technology.",

        "exam_question":
            f"Examination Question: Define {topic}, explain its importance, describe two characteristics, and state two practical applications.",

        "revision":
            f"Revision Note: Remember the definition, meaning, characteristics, types, applications, advantages, limitations, and practical examples of {topic}.",
    }

    answer = templates.get(
        intent,
        templates["definition"]
    )

    # --------------------------------------------------------
    # Backward-compatible variation support
    # --------------------------------------------------------

    if variation:

        variation = normalize(
            variation
        )

        if variation:

            answer = (
                f"{answer} "
                f"Additional context: {variation}"
            )

    return answer


# ============================================================
# BUILD RECORD
# ============================================================

def build_record(
    topic: str,
    category: str,
    intent: str | None = None,
    answer: str | None = None,
    examples: list[str] | None = None,
    aliases: list[str] | None = None,
    education_level: str = "university",
    difficulty: str = "intermediate",
    variation: str | None = None,
) -> dict:
    """
    Build one standardized educational record.

    Compatibility:
        intent=
            Used by Version 3 generators.

        variation=
            Supported for older generators.

    If intent is omitted, the record defaults to "definition".
    """

    topic = normalize(topic)
    category = normalize(category)

    # --------------------------------------------------------
    # Backward compatibility
    # --------------------------------------------------------

    if intent is None:

        intent = "definition"

    intent = normalize(intent)

    # --------------------------------------------------------
    # Generate answer
    # --------------------------------------------------------

    if answer is None:

        answer = generate_answer(
            topic=topic,
            category=category,
            intent=intent,
            variation=variation
        )

    else:

        answer = normalize(answer)

        if variation:

            variation = normalize(
                variation
            )

            if variation:

                answer = (
                    f"{answer} "
                    f"Additional context: {variation}"
                )

    # --------------------------------------------------------
    # Examples
    # --------------------------------------------------------

    if examples is None:

        examples = default_examples(
            topic
        )

    # --------------------------------------------------------
    # Standard record
    # --------------------------------------------------------

    return {
        "topic":
            f"{topic} - "
            f"{intent.replace('_', ' ').title()}",

        "keywords":
            make_keywords(
                topic,
                category,
                aliases
            ),

        "definition":
            f"{intent.replace('_', ' ').title()} of {topic}",

        "explanation":
            normalize(answer),

        "examples": [
            normalize(example)
            for example in examples
            if normalize(example)
        ],

        "category":
            category,

        "intent":
            intent,

        "education_level":
            education_level,

        "difficulty":
            difficulty,
    }


# ============================================================
# BUILD COMPLETE KNOWLEDGE FAMILY
# ============================================================

def build_knowledge_family(
    topic: str,
    category: str,
    aliases: list[str] | None = None,
    education_level: str = "university",
    difficulty: str = "intermediate",
) -> list[dict]:
    """
    Generate a complete educational knowledge family
    for one concept.
    """

    records = []

    for intent in KNOWLEDGE_FAMILY:

        records.append(
            build_record(
                topic=topic,
                category=category,
                intent=intent,
                aliases=aliases,
                education_level=education_level,
                difficulty=difficulty,
            )
        )

    return records


# ============================================================
# VALIDATION
# ============================================================

def validate_record(
    record: dict
) -> bool:
    """
    Validate the standardized knowledge record.
    """

    required = {
        "topic",
        "keywords",
        "definition",
        "explanation",
        "examples",
        "category",
        "intent",
        "education_level",
        "difficulty",
    }

    if not isinstance(record, dict):
        return False

    if not required.issubset(
        record
    ):
        return False

    if not isinstance(
        record["topic"],
        str
    ):
        return False

    if not record["topic"].strip():
        return False

    if not isinstance(
        record["keywords"],
        list
    ):
        return False

    if not record["keywords"]:
        return False

    if not isinstance(
        record["examples"],
        list
    ):
        return False

    if not isinstance(
        record["explanation"],
        str
    ):
        return False

    if not record["explanation"].strip():
        return False

    if not isinstance(
        record["category"],
        str
    ):
        return False

    if not record["category"].strip():
        return False

    if not isinstance(
        record["intent"],
        str
    ):
        return False

    if not record["intent"].strip():
        return False

    return True


# ============================================================
# DUPLICATE KEY
# ============================================================

def record_key(
    record: dict
) -> str:
    """
    Generate a stable duplicate key.
    """

    return "|".join([
        normalize(
            record.get(
                "category",
                ""
            )
        ).lower(),

        normalize(
            record.get(
                "topic",
                ""
            )
        ).lower(),

        normalize(
            record.get(
                "intent",
                ""
            )
        ).lower(),
    ])
