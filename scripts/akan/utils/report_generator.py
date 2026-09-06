"""
==============================================================
AKAN REPORT GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate professional build reports for the Akan
    Knowledge Base.

Produces:
    • Console report
    • Report dictionary
    • Timestamp
    • Category statistics
    • Generator statistics
==============================================================
"""

from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Any


# ============================================================
# CATEGORY COUNTS
# ============================================================

def category_counts(records: list[dict]) -> dict[str, int]:
    return dict(
        Counter(
            record.get("category", "unknown")
            for record in records
        )
    )


# ============================================================
# GENERATOR COUNTS
# ============================================================

def generator_counts(records: list[dict]) -> dict[str, int]:
    counter = Counter()

    for record in records:

        record_id = record.get("record_id", "")

        prefix = "-".join(record_id.split("-")[:2])

        counter[prefix] += 1

    return dict(counter)


# ============================================================
# REPORT OBJECT
# ============================================================

def build_report(
    records: list[dict],
    duplicates_removed: int = 0,
    invalid_records: int = 0,
    generator_failures: int = 0,
) -> dict[str, Any]:

    return {
        "version": "3.0",
        "generated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "total_records": len(records),
        "duplicates_removed": duplicates_removed,
        "invalid_records": invalid_records,
        "generator_failures": generator_failures,
        "categories": category_counts(records),
        "generators": generator_counts(records),
    }


# ============================================================
# PRINT REPORT
# ============================================================

def print_report(report: dict[str, Any]) -> None:

    print()
    print("=" * 70)
    print("AKAN KNOWLEDGE BASE REPORT")
    print("=" * 70)

    print(f"Version               : {report['version']}")
    print(f"Generated at          : {report['generated_at']}")
    print(f"Final records         : {report['total_records']:,}")
    print(f"Duplicates removed    : {report['duplicates_removed']:,}")
    print(f"Invalid records       : {report['invalid_records']:,}")
    print(f"Generator failures    : {report['generator_failures']:,}")

    print()
    print("-" * 70)
    print("RECORDS BY CATEGORY")
    print("-" * 70)

    for category, count in sorted(report["categories"].items()):
        print(f"{category:<35} {count:>8}")

    print()
    print("-" * 70)
    print("RECORDS BY GENERATOR")
    print("-" * 70)

    for generator, count in sorted(report["generators"].items()):
        print(f"{generator:<35} {count:>8}")

    print("=" * 70)


__all__ = [
    "category_counts",
    "generator_counts",
    "build_report",
    "print_report",
]
