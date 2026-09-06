"""
Akan Knowledge Expansion Manager
Version 1.0

Responsible for:
    - loading the existing Akan knowledge base
    - loading modular expansion files
    - validating records
    - removing duplicates
    - merging valid records
    - reporting category distribution
    - preserving the existing Akan schema
"""

from __future__ import annotations

import json
from pathlib import Path
from collections import Counter
from typing import Any, Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[3]

BASE_FILE = (
    ROOT
    / "data"
    / "akan"
    / "akan_knowledge_base.json"
)

SOURCE_DIR = (
    ROOT
    / "data"
    / "akan"
    / "sources"
)

OUTPUT_FILE = (
    ROOT
    / "data"
    / "akan"
    / "akan_knowledge_base_expanded.json"
)


REQUIRED_FIELDS = [
    "id",
    "language",
    "type",
    "category",
    "word",
    "english",
    "meaning",
]


# ---------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------

def load_json(path: Path) -> Any:
    """Load JSON safely."""

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
    """Extract records from supported JSON structures."""

    if isinstance(data, list):
        return [
            item
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
                    item
                    for item in value
                    if isinstance(item, dict)
                ]

    return []


def load_base_records() -> List[Dict[str, Any]]:
    """Load the current Akan knowledge base."""

    return extract_records(
        load_json(BASE_FILE)
    )


def load_source_records() -> List[Dict[str, Any]]:
    """Load all modular Akan source files."""

    if not SOURCE_DIR.exists():
        return []

    records = []

    for path in sorted(
        SOURCE_DIR.glob("*.json")
    ):
        data = load_json(path)

        for record in extract_records(data):
            record = dict(record)
            record["_source_file"] = path.name
            records.append(record)

    return records


# ---------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------

def normalize(value: Any) -> str:
    """Normalize text for comparison."""

    if value is None:
        return ""

    return " ".join(
        str(value)
        .strip()
        .lower()
        .split()
    )


def record_pair(
    record: Dict[str, Any],
) -> Tuple[str, str]:
    """Return normalized Akan-English pair."""

    akan = (
        record.get("akan")
        or record.get("twi")
        or record.get("word")
        or record.get("term")
        or ""
    )

    english = (
        record.get("english")
        or record.get("translation")
        or ""
    )

    return (
        normalize(akan),
        normalize(english),
    )


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def validate_record(
    record: Dict[str, Any],
) -> Tuple[bool, List[str]]:
    """Validate one record."""

    errors = []

    for field in REQUIRED_FIELDS:
        value = record.get(field)

        if value is None:
            errors.append(
                f"missing:{field}"
            )
            continue

        if isinstance(value, str) and not value.strip():
            errors.append(
                f"empty:{field}"
            )

    if not record_pair(record)[0]:
        errors.append("missing:akan_word")

    if not record_pair(record)[1]:
        errors.append("missing:english_translation")

    return (
        len(errors) == 0,
        errors,
    )


# ---------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------

def deduplicate_records(
    records: List[Dict[str, Any]],
) -> Tuple[
    List[Dict[str, Any]],
    int,
    int,
]:
    """
    Remove duplicate IDs and duplicate Akan-English pairs.

    Returns:
        unique records
        duplicate ID count
        duplicate pair count
    """

    unique = []

    ids = set()
    pairs = set()

    duplicate_ids = 0
    duplicate_pairs = 0

    for record in records:

        record_id = normalize(
            record.get("id")
        )

        pair = record_pair(record)

        if record_id:
            if record_id in ids:
                duplicate_ids += 1
                continue

        if pair != ("", ""):
            if pair in pairs:
                duplicate_pairs += 1
                continue

        if record_id:
            ids.add(record_id)

        if pair != ("", ""):
            pairs.add(pair)

        unique.append(record)

    return (
        unique,
        duplicate_ids,
        duplicate_pairs,
    )


# ---------------------------------------------------------------------
# Merge
# ---------------------------------------------------------------------

def merge_records(
    base_records: List[Dict[str, Any]],
    source_records: List[Dict[str, Any]],
) -> Tuple[
    List[Dict[str, Any]],
    Dict[str, int],
]:
    """Merge valid source records into the base."""

    combined = []

    base_pairs = set()
    base_ids = set()

    for record in base_records:

        record = dict(record)

        record.pop(
            "_source_file",
            None,
        )

        combined.append(record)

        record_id = normalize(
            record.get("id")
        )

        pair = record_pair(record)

        if record_id:
            base_ids.add(record_id)

        if pair != ("", ""):
            base_pairs.add(pair)

    stats = {
        "source_records": len(source_records),
        "added": 0,
        "duplicate_ids": 0,
        "duplicate_pairs": 0,
        "invalid": 0,
    }

    for record in source_records:

        valid, _ = validate_record(record)

        if not valid:
            stats["invalid"] += 1
            continue

        record = dict(record)

        record.pop(
            "_source_file",
            None,
        )

        record_id = normalize(
            record.get("id")
        )

        pair = record_pair(record)

        if record_id and record_id in base_ids:
            stats["duplicate_ids"] += 1
            continue

        if pair in base_pairs:
            stats["duplicate_pairs"] += 1
            continue

        combined.append(record)

        if record_id:
            base_ids.add(record_id)

        base_pairs.add(pair)

        stats["added"] += 1

    return combined, stats


# ---------------------------------------------------------------------
# Category report
# ---------------------------------------------------------------------

def category_report(
    records: List[Dict[str, Any]],
) -> Counter:
    """Count records by category."""

    counter = Counter()

    for record in records:

        category = (
            record.get("category")
            or record.get("type")
            or "unknown"
        )

        counter[
            normalize(category)
        ] += 1

    return counter


def type_report(
    records: List[Dict[str, Any]],
) -> Counter:
    """Count records by knowledge type."""

    counter = Counter()

    for record in records:

        knowledge_type = (
            record.get("type")
            or "unknown"
        )

        counter[
            normalize(knowledge_type)
        ] += 1

    return counter


# ---------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------

def save_records(
    records: List[Dict[str, Any]],
) -> None:
    """Save the expanded knowledge base."""

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            records,
            file,
            ensure_ascii=False,
            indent=2,
        )


# ---------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------

def print_report(
    base_records: List[Dict[str, Any]],
    source_records: List[Dict[str, Any]],
    merged_records: List[Dict[str, Any]],
    stats: Dict[str, int],
) -> None:

    print()
    print("=" * 70)
    print("AKAN KNOWLEDGE EXPANSION REPORT")
    print("=" * 70)

    print(
        f"Base records:       {len(base_records)}"
    )

    print(
        f"Source records:     {len(source_records)}"
    )

    print(
        f"New records added:  {stats['added']}"
    )

    print(
        f"Duplicate IDs:      {stats['duplicate_ids']}"
    )

    print(
        f"Duplicate pairs:    {stats['duplicate_pairs']}"
    )

    print(
        f"Invalid records:    {stats['invalid']}"
    )

    print(
        f"Final records:      {len(merged_records)}"
    )

    print()
    print("CATEGORY DISTRIBUTION")
    print("-" * 70)

    categories = category_report(
        merged_records
    )

    for category, count in sorted(
        categories.items(),
        key=lambda item: (
            -item[1],
            item[0],
        ),
    ):
        print(
            f"{category:<30} {count:>6}"
        )

    print()
    print("KNOWLEDGE TYPES")
    print("-" * 70)

    types = type_report(
        merged_records
    )

    for knowledge_type, count in sorted(
        types.items(),
        key=lambda item: (
            -item[1],
            item[0],
        ),
    ):
        print(
            f"{knowledge_type:<30} {count:>6}"
        )

    print()
    print("PROGRESS")
    print("-" * 70)

    total = len(merged_records)

    milestones = [
        373,
        1000,
        2000,
        5000,
        10000,
        15000,
    ]

    for milestone in milestones:

        if total >= milestone:
            status = "COMPLETED"
        else:
            status = f"{milestone - total} remaining"

        print(
            f"{milestone:>6} records : {status}"
        )

    print()
    print(
        f"Output: {OUTPUT_FILE}"
    )

    print("=" * 70)
    print()


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> None:

    base_records = load_base_records()

    source_records = load_source_records()

    merged_records, stats = merge_records(
        base_records,
        source_records,
    )

    merged_records, duplicate_ids, duplicate_pairs = (
        deduplicate_records(
            merged_records
        )
    )

    stats["duplicate_ids"] += duplicate_ids
    stats["duplicate_pairs"] += duplicate_pairs

    save_records(
        merged_records
    )

    print_report(
        base_records,
        source_records,
        merged_records,
        stats,
    )


if __name__ == "__main__":
    main()
