"""
==============================================================
AKAN DUPLICATE CHECKER
Version 3.0
==============================================================

Purpose:
    Detect duplicate records before they enter the Akan
    knowledge base.

Checks:
    • Duplicate record_id
    • Duplicate Akan term
    • Duplicate English term
    • Duplicate Akan + English pair

This utility is shared across the Akan project.
==============================================================
"""

from __future__ import annotations

from collections import defaultdict


# ============================================================
# NORMALIZATION
# ============================================================

def normalize_text(value: str) -> str:
    """
    Normalize text for comparison.
    """

    return str(value).strip().lower()


# ============================================================
# DUPLICATE RECORD IDs
# ============================================================

def duplicate_record_ids(records):
    """
    Return duplicate record IDs.
    """

    seen = set()

    duplicates = []

    for record in records:

        record_id = record.get("record_id", "")

        if record_id in seen:

            duplicates.append(record_id)

        else:

            seen.add(record_id)

    return duplicates


# ============================================================
# DUPLICATE AKAN TERMS
# ============================================================

def duplicate_akan_terms(records):
    """
    Return duplicate Akan terms.
    """

    seen = {}

    duplicates = []

    for record in records:

        term = normalize_text(
            record.get("akan_term", "")
        )

        if not term:

            continue

        if term in seen:

            duplicates.append(term)

        else:

            seen[term] = record.get("record_id")

    return duplicates


# ============================================================
# DUPLICATE ENGLISH TERMS
# ============================================================

def duplicate_english_terms(records):
    """
    Return duplicate English terms.
    """

    seen = {}

    duplicates = []

    for record in records:

        term = normalize_text(
            record.get("english_term", "")
        )

        if not term:

            continue

        if term in seen:

            duplicates.append(term)

        else:

            seen[term] = record.get("record_id")

    return duplicates


# ============================================================
# DUPLICATE TERM PAIRS
# ============================================================

def duplicate_term_pairs(records):
    """
    Return duplicate Akan-English pairs.
    """

    seen = {}

    duplicates = []

    for record in records:

        pair = (
            normalize_text(
                record.get("akan_term", "")
            ),
            normalize_text(
                record.get("english_term", "")
            ),
        )

        if pair in seen:

            duplicates.append(pair)

        else:

            seen[pair] = record.get("record_id")

    return duplicates


# ============================================================
# CATEGORY SUMMARY
# ============================================================

def category_summary(records):
    """
    Count records per category.
    """

    summary = defaultdict(int)

    for record in records:

        summary[
            record.get("category", "unknown")
        ] += 1

    return dict(summary)


# ============================================================
# COMPLETE REPORT
# ============================================================

def duplicate_report(records):
    """
    Return a full duplicate report.
    """

    return {
        "total_records": len(records),
        "duplicate_record_ids": duplicate_record_ids(records),
        "duplicate_akan_terms": duplicate_akan_terms(records),
        "duplicate_english_terms": duplicate_english_terms(records),
        "duplicate_term_pairs": duplicate_term_pairs(records),
        "category_summary": category_summary(records),
    }


__all__ = [
    "normalize_text",
    "duplicate_record_ids",
    "duplicate_akan_terms",
    "duplicate_english_terms",
    "duplicate_term_pairs",
    "category_summary",
    "duplicate_report",
]
