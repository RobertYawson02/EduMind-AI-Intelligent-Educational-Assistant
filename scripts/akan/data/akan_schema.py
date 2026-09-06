"""
==============================================================
AKAN KNOWLEDGE RECORD SCHEMA
Version 3.0
==============================================================

Shared record creator and validator for the Akan knowledge base.

All Akan generators should use create_akan_record().
==============================================================
"""

from typing import Any


# ============================================================
# REQUIRED FIELDS
# ============================================================

REQUIRED_FIELDS = [
    "record_id",
    "akan_term",
    "english_term",
    "category",
    "subcategory",
    "definition_akan",
    "definition_english",
    "explanation_akan",
    "examples_akan",
    "examples_english",
    "keywords_akan",
    "keywords_english",
    "question_patterns",
]


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_text(value: Any) -> str:
    """Convert a value to clean text."""

    if value is None:
        return ""

    return str(value).strip()


# ============================================================
# LIST CLEANING
# ============================================================

def clean_list(value: Any) -> list:
    """Convert a value into a clean list of strings."""

    if value is None:
        return []

    if isinstance(value, str):
        value = [value]

    if not isinstance(value, (list, tuple, set)):
        return []

    result = []

    for item in value:
        text = clean_text(item)

        if text:
            result.append(text)

    return result


# ============================================================
# CREATE AKAN RECORD
# ============================================================

def create_akan_record(
    record_id,
    akan_term,
    english_term,
    category,
    subcategory,
    definition_akan,
    definition_english,
    explanation_akan,
    examples_akan=None,
    examples_english=None,
    keywords_akan=None,
    keywords_english=None,
    question_patterns=None,
):
    """
    Create one standardized Akan knowledge record.
    """

    record = {
        "record_id": clean_text(record_id),
        "akan_term": clean_text(akan_term),
        "english_term": clean_text(english_term),
        "category": clean_text(category),
        "subcategory": clean_text(subcategory),
        "definition_akan": clean_text(definition_akan),
        "definition_english": clean_text(definition_english),
        "explanation_akan": clean_text(explanation_akan),
        "examples_akan": clean_list(examples_akan),
        "examples_english": clean_list(examples_english),
        "keywords_akan": clean_list(keywords_akan),
        "keywords_english": clean_list(keywords_english),
        "question_patterns": clean_list(question_patterns),
    }

    validate_akan_record(record)

    return record


# ============================================================
# VALIDATE ONE RECORD
# ============================================================

def validate_akan_record(record):
    """
    Validate one Akan knowledge record.

    Returns True when the record is valid.
    Raises ValueError when the record is invalid.
    """

    if not isinstance(record, dict):
        raise ValueError("Record must be a dictionary.")

    # Check required fields.
    for field in REQUIRED_FIELDS:
        if field not in record:
            raise ValueError(
                "Missing required field: " + field
            )

    # Check required text fields.
    text_fields = [
        "record_id",
        "akan_term",
        "english_term",
        "category",
        "subcategory",
        "definition_akan",
        "definition_english",
        "explanation_akan",
    ]

    for field in text_fields:
        value = record[field]

        if not isinstance(value, str):
            raise ValueError(
                field + " must be a string."
            )

        if not value.strip():
            raise ValueError(
                field + " cannot be empty."
            )

    # Check list fields.
    list_fields = [
        "examples_akan",
        "examples_english",
        "keywords_akan",
        "keywords_english",
        "question_patterns",
    ]

    for field in list_fields:
        value = record[field]

        if not isinstance(value, list):
            raise ValueError(
                field + " must be a list."
            )

        for item in value:
            if not isinstance(item, str):
                raise ValueError(
                    field + " must contain only strings."
                )

            if not item.strip():
                raise ValueError(
                    field + " cannot contain empty strings."
                )

    # Akan and English examples must match.
    if len(record["examples_akan"]) != len(
        record["examples_english"]
    ):
        raise ValueError(
            "examples_akan and examples_english must have "
            "the same number of items."
        )

    # Record ID must use the Akan prefix.
    if not record["record_id"].startswith("AKAN-"):
        raise ValueError(
            "record_id must start with AKAN-."
        )

    return True


# ============================================================
# VALIDATE MANY RECORDS
# ============================================================

def validate_akan_records(records):
    """
    Validate a list of Akan knowledge records.
    """

    if not isinstance(records, list):
        raise ValueError(
            "Records must be provided as a list."
        )

    for record in records:
        validate_akan_record(record)

    return True


# ============================================================
# EXPORTS
# ============================================================

__all__ = [
    "REQUIRED_FIELDS",
    "create_akan_record",
    "validate_akan_record",
    "validate_akan_records",
]