"""
Large-Scale Akan Knowledge Expansion
Version 1.0

Purpose
-------
Expand the existing Akan knowledge base into a high-coverage retrieval
corpus without inventing unsupported facts.

Design
------
1. Preserve every original knowledge record.
2. Generate meaningful retrieval/QA variants from each original record.
3. Preserve the parent record ID.
4. Add explicit record_role metadata so original knowledge and derived
   retrieval records are distinguishable.
5. Generate variants only when the underlying field actually exists.
6. Deduplicate aggressively.
7. Produce a validation/statistics report.

This is retrieval augmentation, not fake factual expansion.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple


# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[3]

BASE_FILE = (
    ROOT
    / "data"
    / "akan"
    / "akan_knowledge_base.json"
)

OUTPUT_DIR = (
    ROOT
    / "data"
    / "akan"
)

OUTPUT_FILE = (
    OUTPUT_DIR
    / "akan_knowledge_base_scaled.json"
)

REPORT_FILE = (
    OUTPUT_DIR
    / "akan_scale_report.json"
)


# ---------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------

def normalize(value: Any) -> str:
    if value is None:
        return ""

    value = str(value).strip().lower()

    value = re.sub(
        r"\s+",
        " ",
        value,
    )

    return value


def clean_text(value: Any) -> str:
    if value is None:
        return ""

    return str(value).strip()


def as_list(value: Any) -> List[str]:
    if value is None:
        return []

    if isinstance(value, list):
        return [
            clean_text(item)
            for item in value
            if clean_text(item)
        ]

    if isinstance(value, str):
        parts = re.split(
            r"[,;|]",
            value,
        )

        return [
            clean_text(item)
            for item in parts
            if clean_text(item)
        ]

    return [clean_text(value)]


def dedupe_strings(values: Iterable[str]) -> List[str]:
    result = []
    seen = set()

    for value in values:
        value = clean_text(value)

        key = normalize(value)

        if not key or key in seen:
            continue

        seen.add(key)
        result.append(value)

    return result


def record_id(record: Dict[str, Any]) -> str:
    return clean_text(
        record.get("id")
        or record.get("record_id")
    )


def akan_word(record: Dict[str, Any]) -> str:
    return clean_text(
        record.get("akan")
        or record.get("twi")
        or record.get("word")
        or record.get("term")
    )


def english_word(record: Dict[str, Any]) -> str:
    return clean_text(
        record.get("english")
        or record.get("translation")
        or record.get("english_translation")
    )


def meaning(record: Dict[str, Any]) -> str:
    return clean_text(
        record.get("meaning")
        or record.get("definition")
        or record.get("explanation")
        or record.get("description")
    )


def category(record: Dict[str, Any]) -> str:
    return clean_text(
        record.get("category")
        or record.get("knowledge_category")
        or record.get("type")
        or "general"
    )


# ---------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------

def load_records(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(
            f"Knowledge base not found: {path}"
        )

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    if isinstance(data, list):
        return [
            dict(item)
            for item in data
            if isinstance(item, dict)
        ]

    if isinstance(data, dict):
        for key in (
            "records",
            "entries",
            "knowledge",
            "data",
            "items",
        ):
            value = data.get(key)

            if isinstance(value, list):
                return [
                    dict(item)
                    for item in value
                    if isinstance(item, dict)
                ]

    raise ValueError(
        "Unsupported Akan knowledge-base JSON structure."
    )


# ---------------------------------------------------------------------
# Stable derived IDs
# ---------------------------------------------------------------------

def slug(value: str) -> str:
    value = normalize(value)

    value = re.sub(
        r"[^a-z0-9]+",
        "_",
        value,
    )

    return value.strip("_")


def derived_id(
    parent_id: str,
    variant_name: str,
    sequence: int,
) -> str:
    return (
        f"{parent_id}"
        f"__qa_{slug(variant_name)}"
        f"_{sequence:02d}"
    )


# ---------------------------------------------------------------------
# Common field extraction
# ---------------------------------------------------------------------

def get_synonyms(record: Dict[str, Any]) -> List[str]:
    return dedupe_strings(
        as_list(
            record.get("synonyms")
            or record.get("synonym")
        )
    )


def get_antonyms(record: Dict[str, Any]) -> List[str]:
    return dedupe_strings(
        as_list(
            record.get("antonyms")
            or record.get("antonym")
        )
    )


def get_related(record: Dict[str, Any]) -> List[str]:
    return dedupe_strings(
        as_list(
            record.get("related_words")
            or record.get("related_terms")
            or record.get("related")
        )
    )


def get_examples(record: Dict[str, Any]) -> List[str]:
    return dedupe_strings(
        as_list(
            record.get("examples")
            or record.get("example")
            or record.get("sentences")
        )
    )


# ---------------------------------------------------------------------
# Variant builder
# ---------------------------------------------------------------------

def make_variant(
    source: Dict[str, Any],
    parent_id: str,
    variant_name: str,
    question: str,
    answer: str,
    sequence: int,
    intent: str,
) -> Dict[str, Any]:
    """
    Create a retrieval-oriented QA record.

    The underlying source remains explicitly linked.
    """

    base_category = category(source)

    variant_id = derived_id(
        parent_id,
        variant_name,
        sequence,
    )

    akan = akan_word(source)
    english = english_word(source)

    return {
        "id": variant_id,
        "parent_id": parent_id,
        "language": clean_text(
            source.get("language")
            or "Akan"
        ),
        "language_variant": clean_text(
            source.get("language_variant")
            or "Twi"
        ),
        "type": "qa_retrieval",
        "record_role": "retrieval_variant",
        "category": base_category,
        "subtype": variant_name,

        # Search fields
        "word": akan,
        "akan": akan,
        "twi": akan,
        "english": english,
        "translation": english,

        # QA fields
        "question": clean_text(question),
        "answer": clean_text(answer),
        "intent": intent,

        # Preserve supporting evidence
        "meaning": meaning(source),
        "definition": meaning(source),
        "examples": get_examples(source),
        "synonyms": get_synonyms(source),
        "antonyms": get_antonyms(source),
        "related_words": get_related(source),

        "keywords": dedupe_strings(
            [
                akan,
                english,
                category(source),
                variant_name,
                question,
            ]
            + as_list(source.get("keywords"))
        ),

        "source": "akan_retrieval_augmentation",
        "source_parent": source.get("source"),
        "version": "1.0",
        "quality": "derived_from_curated_record",
    }


# ---------------------------------------------------------------------
# Question generation
# ---------------------------------------------------------------------

def generate_variants(
    source: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Generate only questions that can be answered from the source record.
    """

    parent_id = record_id(source)

    if not parent_id:
        return []

    akan = akan_word(source)
    english = english_word(source)
    definition = meaning(source)

    if not akan and not english:
        return []

    variants = []

    # --------------------------------------------------------------
    # 1. English -> Akan
    # --------------------------------------------------------------

    if akan and english:

        questions = [
            (
                "translate_english_to_akan",
                f"What is {english} in Akan?",
            ),
            (
                "translate_english_to_twi",
                f"What is {english} in Twi?",
            ),
            (
                "translate_word_to_akan",
                f"How do you say {english} in Akan?",
            ),
            (
                "translate_word_to_twi",
                f"How do you say {english} in Twi?",
            ),
        ]

        for number, (
            name,
            question,
        ) in enumerate(
            questions,
            start=1,
        ):

            variants.append(
                make_variant(
                    source,
                    parent_id,
                    name,
                    question,
                    akan,
                    number,
                    "translation",
                )
            )

    # --------------------------------------------------------------
    # 2. Akan -> English
    # --------------------------------------------------------------

    if akan and english:

        questions = [
            (
                "translate_akan_to_english",
                f"What does {akan} mean in English?",
            ),
            (
                "translate_twi_to_english",
                f"What is the English meaning of {akan}?",
            ),
            (
                "translate_akan_word",
                f"Translate {akan} into English.",
            ),
        ]

        for number, (
            name,
            question,
        ) in enumerate(
            questions,
            start=10,
        ):

            variants.append(
                make_variant(
                    source,
                    parent_id,
                    name,
                    question,
                    english,
                    number,
                    "translation",
                )
            )

    # --------------------------------------------------------------
    # 3. Meaning
    # --------------------------------------------------------------

    if akan and definition:

        questions = [
            (
                "meaning_of_akan_word",
                f"What does {akan} mean?",
            ),
            (
                "meaning_of_twi_word",
                f"What is the meaning of {akan} in Akan?",
            ),
            (
                "define_akan_word",
                f"Define the Akan word {akan}.",
            ),
            (
                "explain_akan_word",
                f"Explain the meaning of {akan}.",
            ),
        ]

        for number, (
            name,
            question,
        ) in enumerate(
            questions,
            start=20,
        ):

            variants.append(
                make_variant(
                    source,
                    parent_id,
                    name,
                    question,
                    definition,
                    number,
                    "meaning",
                )
            )

    # --------------------------------------------------------------
    # 4. English concept meaning
    # --------------------------------------------------------------

    if english and definition:

        questions = [
            (
                "english_concept_definition",
                f"What is {english}?",
            ),
            (
                "english_concept_meaning",
                f"What does {english} mean?",
            ),
            (
                "english_concept_explanation",
                f"Explain {english}.",
            ),
        ]

        for number, (
            name,
            question,
        ) in enumerate(
            questions,
            start=30,
        ):

            answer = definition

            if akan:
                answer = (
                    f"{definition} "
                    f"In Akan, it is {akan}."
                )

            variants.append(
                make_variant(
                    source,
                    parent_id,
                    name,
                    question,
                    answer,
                    number,
                    "education",
                )
            )

    # --------------------------------------------------------------
    # 5. Examples
    # --------------------------------------------------------------

    examples = get_examples(source)

    if akan and examples:

        for number, example in enumerate(
            examples,
            start=40,
        ):

            variants.append(
                make_variant(
                    source,
                    parent_id,
                    "example_sentence",
                    f"Give me an example using {akan}.",
                    example,
                    number,
                    "example",
                )
            )

    # --------------------------------------------------------------
    # 6. Synonyms
    # --------------------------------------------------------------

    synonyms = get_synonyms(source)

    if akan and synonyms:

        answer = ", ".join(synonyms)

        variants.append(
            make_variant(
                source,
                parent_id,
                "synonyms",
                f"Give me synonyms for {akan}.",
                answer,
                50,
                "synonym",
            )
        )

        variants.append(
            make_variant(
                source,
                parent_id,
                "similar_words",
                f"What words are similar to {akan}?",
                answer,
                51,
                "synonym",
            )
        )

    # --------------------------------------------------------------
    # 7. Antonyms
    # --------------------------------------------------------------

    antonyms = get_antonyms(source)

    if akan and antonyms:

        answer = ", ".join(antonyms)

        variants.append(
            make_variant(
                source,
                parent_id,
                "antonyms",
                f"Give me antonyms for {akan}.",
                answer,
                60,
                "antonym",
            )
        )

        variants.append(
            make_variant(
                source,
                parent_id,
                "opposite_words",
                f"What is the opposite of {akan}?",
                answer,
                61,
                "antonym",
            )
        )

    # --------------------------------------------------------------
    # 8. Related words
    # --------------------------------------------------------------

    related = get_related(source)

    if akan and related:

        answer = ", ".join(related)

        variants.append(
            make_variant(
                source,
                parent_id,
                "related_words",
                f"What words are related to {akan}?",
                answer,
                70,
                "related",
            )
        )

        variants.append(
            make_variant(
                source,
                parent_id,
                "associated_words",
                f"What words are associated with {akan}?",
                answer,
                71,
                "related",
            )
        )

    return variants


# ---------------------------------------------------------------------
# Remove redundant variants
# ---------------------------------------------------------------------

def variant_key(
    record: Dict[str, Any],
) -> Tuple[str, str, str]:
    return (
        normalize(record.get("question")),
        normalize(record.get("answer")),
        normalize(record.get("intent")),
    )


def deduplicate(
    records: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:

    unique = []
    seen_ids: Set[str] = set()
    seen_variants: Set[Tuple[str, str, str]] = set()

    for record in records:

        rid = normalize(
            record.get("id")
        )

        key = variant_key(record)

        if rid and rid in seen_ids:
            continue

        if key in seen_variants:
            continue

        if rid:
            seen_ids.add(rid)

        seen_variants.add(key)

        unique.append(record)

    return unique


# ---------------------------------------------------------------------
# Dataset expansion
# ---------------------------------------------------------------------

def build_scaled_dataset(
    base_records: List[Dict[str, Any]],
) -> Tuple[
    List[Dict[str, Any]],
    Dict[str, Any],
]:

    # Preserve original records.
    originals = []

    for source in base_records:

        original = dict(source)

        original["record_role"] = (
            original.get(
                "record_role"
            )
            or "original_knowledge"
        )

        originals.append(original)

    generated = []

    for source in originals:
        generated.extend(
            generate_variants(source)
        )

    combined = (
        originals
        + generated
    )

    combined = deduplicate(
        combined
    )

    # --------------------------------------------------------------
    # Statistics
    # --------------------------------------------------------------

    role_counter = Counter()
    type_counter = Counter()
    category_counter = Counter()
    intent_counter = Counter()

    for record in combined:

        role_counter[
            record.get(
                "record_role",
                "unknown",
            )
        ] += 1

        type_counter[
            record.get(
                "type",
                "unknown",
            )
        ] += 1

        category_counter[
            category(record)
        ] += 1

        if record.get("intent"):
            intent_counter[
                record["intent"]
            ] += 1

    report = {
        "version": "1.0",
        "base_file": str(BASE_FILE),
        "output_file": str(OUTPUT_FILE),

        "base_records": len(base_records),

        "generated_records_before_deduplication": len(
            generated
        ),

        "final_records": len(combined),

        "increase": (
            len(combined)
            - len(base_records)
        ),

        "multiplication_factor": round(
            len(combined)
            / max(1, len(base_records)),
            2,
        ),

        "roles": dict(
            role_counter
        ),

        "types": dict(
            type_counter
        ),

        "categories": dict(
            category_counter
        ),

        "intents": dict(
            intent_counter
        ),

        "milestones": {
            "373": len(combined) >= 373,
            "1000": len(combined) >= 1000,
            "2000": len(combined) >= 2000,
            "5000": len(combined) >= 5000,
            "10000": len(combined) >= 10000,
            "15000": len(combined) >= 15000,
        },
    }

    return combined, report


# ---------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------

def save_json(
    path: Path,
    data: Any,
) -> None:

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )


# ---------------------------------------------------------------------
# Console report
# ---------------------------------------------------------------------

def print_report(
    report: Dict[str, Any],
) -> None:

    print()
    print("=" * 72)
    print("AKAN LARGE-SCALE EXPANSION")
    print("=" * 72)

    print(
        f"Original records:          "
        f"{report['base_records']}"
    )

    print(
        f"Generated QA records:      "
        f"{report['generated_records_before_deduplication']}"
    )

    print(
        f"Final unique records:      "
        f"{report['final_records']}"
    )

    print(
        f"Net increase:              "
        f"{report['increase']}"
    )

    print(
        f"Expansion factor:          "
        f"{report['multiplication_factor']}x"
    )

    print()
    print("MILESTONES")
    print("-" * 72)

    for milestone, complete in (
        report["milestones"].items()
    ):
        status = (
            "REACHED"
            if complete
            else "NOT YET REACHED"
        )

        print(
            f"{milestone:>6} records : {status}"
        )

    print()
    print("RECORD ROLES")
    print("-" * 72)

    for name, count in sorted(
        report["roles"].items()
    ):
        print(
            f"{name:<35} {count:>7}"
        )

    print()
    print("INTENTS")
    print("-" * 72)

    for name, count in sorted(
        report["intents"].items()
    ):
        print(
            f"{name:<35} {count:>7}"
        )

    print()
    print("CATEGORIES")
    print("-" * 72)

    for name, count in sorted(
        report["categories"].items(),
        key=lambda item: (
            -item[1],
            item[0],
        ),
    ):
        print(
            f"{name:<35} {count:>7}"
        )

    print()
    print(
        f"Output: {OUTPUT_FILE}"
    )

    print(
        f"Report: {REPORT_FILE}"
    )

    print("=" * 72)
    print()


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> None:

    print(
        f"Loading Akan KB: {BASE_FILE}"
    )

    base_records = load_records(
        BASE_FILE
    )

    print(
        f"Loaded {len(base_records)} original records."
    )

    combined, report = build_scaled_dataset(
        base_records
    )

    save_json(
        OUTPUT_FILE,
        combined,
    )

    save_json(
        REPORT_FILE,
        report,
    )

    print_report(
        report
    )


if __name__ == "__main__":
    main()
