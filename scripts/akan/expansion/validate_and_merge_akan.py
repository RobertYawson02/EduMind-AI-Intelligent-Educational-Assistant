"""
Akan Validation + Intelligent Merger
Version 1.1

Backward-compatible with V3.0 Akan records.

Important safeguards:
- Never loses the curated foundation.
- Legacy records are normalized rather than rejected merely because
  newer fields are absent.
- Curated records always have highest authority.
- External records cannot overwrite curated records.
- Duplicate IDs/questions/pairs are rejected.
- Invalid records are quarantined.
- Weak but structurally valid external records go to review.
- The process ABORTS if the final corpus would contain fewer curated
  records than the input foundation.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple


ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = ROOT / "data" / "akan"
SOURCE_DIR = DATA_DIR / "sources"

CURATED_FILE = DATA_DIR / "akan_knowledge_base.json"
SCALED_FILE = DATA_DIR / "akan_knowledge_base_scaled.json"
EXTERNAL_FILE = SOURCE_DIR / "ghana_qa_twi_import.json"

MERGED_FILE = DATA_DIR / "akan_knowledge_base_validated.json"
QUARANTINE_FILE = DATA_DIR / "akan_quarantine.json"
REVIEW_FILE = DATA_DIR / "akan_review_queue.json"
REPORT_FILE = DATA_DIR / "akan_validation_report.json"


# ---------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------

def clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize(value: Any) -> str:
    value = clean(value).lower()
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_question(value: Any) -> str:
    value = normalize(value)
    value = re.sub(r"[?!.,;:]+$", "", value)
    return value.strip()


def as_list(value: Any) -> List[str]:

    if value is None:
        return []

    if isinstance(value, list):
        values = value

    elif isinstance(value, str):
        values = re.split(r"[,;|]", value)

    else:
        values = [value]

    output = []
    seen = set()

    for item in values:

        text = clean(item)

        if not text:
            continue

        key = normalize(text)

        if key in seen:
            continue

        seen.add(key)
        output.append(text)

    return output


def text_tokens(value: Any) -> List[str]:
    return re.findall(
        r"[\wÀ-ÖØ-öø-ÿƐɛƆɔ]+",
        normalize(value),
        flags=re.UNICODE,
    )


# ---------------------------------------------------------------------
# JSON loading
# ---------------------------------------------------------------------

def load_json(path: Path) -> Any:

    if not path.exists():
        return None

    try:
        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except (
        OSError,
        json.JSONDecodeError,
    ):
        return None


def extract_records(data: Any) -> List[Dict[str, Any]]:

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

    return []


def load_records(path: Path) -> List[Dict[str, Any]]:
    return extract_records(
        load_json(path)
    )


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
# Flexible schema access
# ---------------------------------------------------------------------

def first(
    record: Dict[str, Any],
    *fields: str,
) -> str:

    for field in fields:

        value = record.get(field)

        if value is None:
            continue

        value = clean(value)

        if value:
            return value

    return ""


def get_id(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "id",
        "record_id",
        "entry_id",
    )


def get_akan(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "akan",
        "twi",
        "word",
        "term",
        "akan_word",
        "twi_word",
    )


def get_english(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "english",
        "translation",
        "english_translation",
        "english_word",
    )


def get_question(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "question",
        "query",
        "prompt",
    )


def get_answer(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "answer",
        "response",
        "output",
    )


def get_meaning(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "meaning",
        "definition",
        "explanation",
        "description",
        "gloss",
    )


def get_category(
    record: Dict[str, Any],
) -> str:

    return (
        first(
            record,
            "category",
            "knowledge_category",
            "domain",
            "subject",
            "type",
        )
        or "general"
    )


def get_intent(
    record: Dict[str, Any],
) -> str:

    return first(
        record,
        "intent",
        "question_type",
    )


# ---------------------------------------------------------------------
# Source classification
# ---------------------------------------------------------------------

def source_class(
    record: Dict[str, Any],
) -> str:

    role = normalize(
        record.get("record_role")
    )

    source = normalize(
        record.get("source")
    )

    if role in {
        "curated",
        "curated_knowledge",
        "original_knowledge",
    }:
        return "curated"

    if role == "retrieval_variant":
        return "retrieval_variant"

    if role == "external_qa":
        return "external_qa"

    if "ghana-qa" in source:
        return "external_qa"

    if normalize(
        record.get("source_dataset")
    ) == "ghananlpcommunity/ghana-qa":
        return "external_qa"

    return "other"


# ---------------------------------------------------------------------
# Normalized legacy records
# ---------------------------------------------------------------------

def normalize_record(
    record: Dict[str, Any],
    classification: str,
) -> Dict[str, Any]:

    output = dict(record)

    rid = get_id(output)

    # Preserve existing ID.
    if not rid:

        seed = "|".join(
            [
                get_akan(output),
                get_english(output),
                get_question(output),
                get_answer(output),
            ]
        )

        digest = hashlib.sha256(
            normalize(seed).encode("utf-8")
        ).hexdigest()[:20]

        rid = f"akan_normalized_{digest}"

    output["id"] = rid

    # Fill legacy-compatible fields.
    akan = get_akan(output)
    english = get_english(output)
    meaning = get_meaning(output)

    output["akan"] = akan
    output["twi"] = (
        clean(output.get("twi"))
        or akan
    )

    output["word"] = (
        clean(output.get("word"))
        or akan
    )

    output["english"] = english
    output["translation"] = (
        clean(output.get("translation"))
        or english
    )

    output["meaning"] = (
        clean(output.get("meaning"))
        or meaning
    )

    output["definition"] = (
        clean(output.get("definition"))
        or meaning
    )

    output["language"] = (
        clean(output.get("language"))
        or "Akan"
    )

    output["language_variant"] = (
        clean(output.get("language_variant"))
        or "Twi"
    )

    output["category"] = get_category(
        output
    )

    output["source_class"] = classification

    # Normalize supporting fields.
    for field in (
        "keywords",
        "examples",
        "synonyms",
        "antonyms",
        "related_words",
        "related_terms",
    ):

        if field in output:
            output[field] = as_list(
                output[field]
            )

    if not output.get("type"):
        if classification == "external_qa":
            output["type"] = "qa_retrieval"
        elif get_question(output) and get_answer(output):
            output["type"] = "qa_retrieval"
        else:
            output["type"] = "vocabulary"

    if not output.get("record_role"):
        if classification == "curated":
            output["record_role"] = "original_knowledge"
        elif classification == "external_qa":
            output["record_role"] = "external_qa"
        else:
            output["record_role"] = "retrieval_variant"

    output["validation_status"] = "validated"

    return output


# ---------------------------------------------------------------------
# Structural validation
# ---------------------------------------------------------------------

def validate_record(
    record: Dict[str, Any],
) -> Tuple[
    bool,
    List[str],
]:

    errors = []

    rid = get_id(record)

    if not rid:
        errors.append("missing_id")

    classification = source_class(
        record
    )

    # --------------------------------------------------------------
    # Curated / legacy knowledge
    # --------------------------------------------------------------

    if classification in {
        "curated",
        "retrieval_variant",
        "other",
    }:

        has_vocabulary_content = bool(
            get_akan(record)
            and (
                get_english(record)
                or get_meaning(record)
            )
        )

        has_qa_content = bool(
            get_question(record)
            and get_answer(record)
        )

        has_generic_content = bool(
            get_akan(record)
            or get_english(record)
            or get_meaning(record)
            or get_answer(record)
        )

        if not (
            has_vocabulary_content
            or has_qa_content
            or has_generic_content
        ):
            errors.append(
                "no_usable_knowledge_content"
            )

    # --------------------------------------------------------------
    # External QA
    # --------------------------------------------------------------

    elif classification == "external_qa":

        question = get_question(record)
        answer = get_answer(record)

        if len(question) < 5:
            errors.append(
                "question_too_short"
            )

        if len(answer) < 2:
            errors.append(
                "answer_too_short"
            )

    return (
        len(errors) == 0,
        errors,
    )


# ---------------------------------------------------------------------
# Fingerprints
# ---------------------------------------------------------------------

def pair_key(
    record: Dict[str, Any],
) -> str:

    akan = normalize(
        get_akan(record)
    )

    english = normalize(
        get_english(record)
    )

    if not akan or not english:
        return ""

    return f"{akan}||{english}"


def question_key(
    record: Dict[str, Any],
) -> str:

    return normalize_question(
        get_question(record)
    )


# ---------------------------------------------------------------------
# Quality scoring
# ---------------------------------------------------------------------

def quality_score(
    record: Dict[str, Any],
) -> float:

    classification = source_class(
        record
    )

    score = 0.0

    if classification == "curated":
        score += 60

    elif classification == "retrieval_variant":
        score += 45

    elif classification == "external_qa":
        score += 30

    else:
        score += 20

    if get_akan(record):
        score += 8

    if get_english(record):
        score += 8

    if get_meaning(record):
        score += 8

    if get_question(record):
        score += 4

    if get_answer(record):
        score += 6

    if as_list(
        record.get("examples")
    ):
        score += 2

    if as_list(
        record.get("synonyms")
    ):
        score += 1

    if as_list(
        record.get("antonyms")
    ):
        score += 1

    if as_list(
        record.get("related_words")
    ):
        score += 1

    return min(
        100,
        score,
    )


# ---------------------------------------------------------------------
# Intelligent merge
# ---------------------------------------------------------------------

def merge_sources(
    curated: List[Dict[str, Any]],
    scaled: List[Dict[str, Any]],
    external: List[Dict[str, Any]],
) -> Tuple[
    List[Dict[str, Any]],
    List[Dict[str, Any]],
    List[Dict[str, Any]],
    Dict[str, int],
]:

    merged = []
    quarantine = []
    review = []

    stats = Counter()

    ids: Set[str] = set()
    pairs: Set[str] = set()
    questions: Set[str] = set()

    # --------------------------------------------------------------
    # Helper
    # --------------------------------------------------------------

    def accept(
        record: Dict[str, Any],
        classification: str,
    ) -> None:

        normalized = normalize_record(
            record,
            classification,
        )

        rid = normalize(
            normalized["id"]
        )

        pair = pair_key(
            normalized
        )

        question = question_key(
            normalized
        )

        if rid in ids:

            stats["duplicate_id"] += 1
            return

        if pair and pair in pairs:

            stats["duplicate_pair"] += 1
            return

        if question and question in questions:

            stats["duplicate_question"] += 1
            return

        score = quality_score(
            normalized
        )

        normalized["quality_score"] = round(
            score,
            2,
        )

        normalized["quality_label"] = (
            "high"
            if score >= 80
            else "good"
            if score >= 60
            else "review"
        )

        merged.append(
            normalized
        )

        ids.add(rid)

        if pair:
            pairs.add(pair)

        if question:
            questions.add(question)

    # --------------------------------------------------------------
    # Curated ALWAYS FIRST.
    # --------------------------------------------------------------

    for record in curated:

        stats["curated_total"] += 1

        valid, errors = validate_record(
            record
        )

        if not valid:

            bad = dict(record)

            bad["_validation_errors"] = errors
            bad["_source_class"] = "curated"

            quarantine.append(bad)

            stats["curated_invalid"] += 1
            continue

        accept(
            record,
            "curated",
        )

        stats["curated_accepted"] += 1

    # --------------------------------------------------------------
    # Scaled
    # --------------------------------------------------------------

    for record in scaled:

        stats["scaled_total"] += 1

        valid, errors = validate_record(
            record
        )

        if not valid:

            bad = dict(record)

            bad["_validation_errors"] = errors
            bad["_source_class"] = source_class(
                record
            )

            quarantine.append(bad)

            stats["scaled_invalid"] += 1
            continue

        classification = source_class(
            record
        )

        pair = pair_key(record)

        question = question_key(record)
        rid = normalize(
            get_id(record)
        )

        if (
            rid in ids
            or (pair and pair in pairs)
            or (question and question in questions)
        ):

            stats["scaled_excluded"] += 1
            continue

        accept(
            record,
            classification,
        )

        stats["scaled_accepted"] += 1

    # --------------------------------------------------------------
    # External QA
    # --------------------------------------------------------------

    for record in external:

        stats["external_total"] += 1

        valid, errors = validate_record(
            record
        )

        if not valid:

            bad = dict(record)

            bad["_validation_errors"] = errors
            bad["_source_class"] = "external_qa"

            quarantine.append(bad)

            stats["external_invalid"] += 1
            continue

        answer = get_answer(record)

        # Keep exceptionally short external
        # responses visible for review.
        if len(
            text_tokens(answer)
        ) < 3:

            flagged = dict(record)

            flagged["_review_reasons"] = [
                "very_short_external_answer"
            ]

            review.append(flagged)

            stats["external_review"] += 1
            continue

        rid = normalize(
            get_id(record)
        )

        pair = pair_key(record)

        question = question_key(
            record
        )

        if (
            rid in ids
            or (pair and pair in pairs)
            or (question and question in questions)
        ):

            stats["external_excluded"] += 1
            continue

        accept(
            record,
            "external_qa",
        )

        stats["external_accepted"] += 1

    stats["final_records"] = len(
        merged
    )

    stats["quarantine_records"] = len(
        quarantine
    )

    stats["review_records"] = len(
        review
    )

    return (
        merged,
        quarantine,
        review,
        dict(stats),
    )


# ---------------------------------------------------------------------
# Distribution
# ---------------------------------------------------------------------

def distributions(
    records: List[Dict[str, Any]],
) -> Dict[str, Dict[str, int]]:

    categories = Counter()
    types = Counter()
    roles = Counter()
    sources = Counter()
    intents = Counter()

    for record in records:

        categories[
            get_category(record)
        ] += 1

        types[
            first(
                record,
                "type",
            )
            or "unknown"
        ] += 1

        roles[
            first(
                record,
                "record_role",
            )
            or "unknown"
        ] += 1

        source = first(
            record,
            "source",
        )

        if source:
            sources[source] += 1

        intent = get_intent(record)

        if intent:
            intents[intent] += 1

    return {
        "categories": dict(categories),
        "types": dict(types),
        "record_roles": dict(roles),
        "sources": dict(sources),
        "intents": dict(intents),
    }


# ---------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------

def build_report(
    curated: List[Dict[str, Any]],
    scaled: List[Dict[str, Any]],
    external: List[Dict[str, Any]],
    merged: List[Dict[str, Any]],
    quarantine: List[Dict[str, Any]],
    review: List[Dict[str, Any]],
    stats: Dict[str, int],
) -> Dict[str, Any]:

    # Critical safeguard.
    if len(merged) < len(curated):
        raise RuntimeError(
            "ABORTED: final validated corpus is smaller "
            "than the curated foundation. No production "
            "corpus should be written."
        )

    return {
        "version": "1.1",

        "input_counts": {
            "curated": len(curated),
            "scaled": len(scaled),
            "external": len(external),
        },

        "output_counts": {
            "validated": len(merged),
            "review": len(review),
            "quarantine": len(quarantine),
        },

        "growth": {
            "base": len(curated),
            "final": len(merged),
            "increase": (
                len(merged)
                - len(curated)
            ),
            "factor": round(
                len(merged)
                / max(
                    1,
                    len(curated),
                ),
                3,
            ),
        },

        "milestones": {
            "373": len(merged) >= 373,
            "1000": len(merged) >= 1000,
            "2000": len(merged) >= 2000,
            "5000": len(merged) >= 5000,
            "10000": len(merged) >= 10000,
            "15000": len(merged) >= 15000,
            "20000": len(merged) >= 20000,
        },

        "statistics": stats,

        "distribution": distributions(
            merged
        ),
    }


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> None:

    print()
    print("=" * 78)
    print("AKAN VALIDATION + INTELLIGENT MERGER V1.1")
    print("=" * 78)

    curated = load_records(
        CURATED_FILE
    )

    scaled = load_records(
        SCALED_FILE
    )

    external = load_records(
        EXTERNAL_FILE
    )

    print()
    print(
        f"Curated source:  {len(curated):,}"
    )

    print(
        f"Scaled source:   {len(scaled):,}"
    )

    print(
        f"External source: {len(external):,}"
    )

    if not curated:
        raise RuntimeError(
            "Curated Akan knowledge base is empty."
        )

    (
        merged,
        quarantine,
        review,
        stats,
    ) = merge_sources(
        curated,
        scaled,
        external,
    )

    report = build_report(
        curated,
        scaled,
        external,
        merged,
        quarantine,
        review,
        stats,
    )

    save_json(
        MERGED_FILE,
        merged,
    )

    save_json(
        QUARANTINE_FILE,
        quarantine,
    )

    save_json(
        REVIEW_FILE,
        review,
    )

    save_json(
        REPORT_FILE,
        report,
    )

    print()
    print("=" * 78)
    print("MERGE RESULT")
    print("=" * 78)

    print(
        f"Curated accepted:   "
        f"{stats.get('curated_accepted', 0):,}"
    )

    print(
        f"Scaled accepted:    "
        f"{stats.get('scaled_accepted', 0):,}"
    )

    print(
        f"External accepted:  "
        f"{stats.get('external_accepted', 0):,}"
    )

    print(
        f"Duplicates removed: "
        f"{(
            stats.get('duplicate_id', 0)
            + stats.get('duplicate_pair', 0)
            + stats.get('duplicate_question', 0)
        ):,}"
    )

    print(
        f"Review:             "
        f"{len(review):,}"
    )

    print(
        f"Quarantine:         "
        f"{len(quarantine):,}"
    )

    print(
        f"FINAL CORPUS:       "
        f"{len(merged):,}"
    )

    print()
    print("MILESTONES")
    print("-" * 78)

    for milestone, reached in (
        report["milestones"].items()
    ):

        print(
            f"{int(milestone):>6,}: "
            f"{'REACHED' if reached else 'not reached'}"
        )

    print()
    print(
        f"Validated KB: {MERGED_FILE}"
    )

    print(
        f"Report:       {REPORT_FILE}"
    )

    print("=" * 78)


if __name__ == "__main__":
    main()
