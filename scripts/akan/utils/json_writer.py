"""
==============================================================
AKAN JSON WRITER
Version 3.0
==============================================================

Purpose:
    Standardized JSON writer for the Akan knowledge project.

Responsibilities:
    • Save UTF-8 JSON.
    • Pretty-print with indentation.
    • Automatically create missing folders.
    • Read existing JSON safely.
    • Provide reusable file utilities.

Used by:
    - build_akan_knowledge.py
    - future merge tools
    - export utilities
==============================================================
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# ============================================================
# ENSURE DIRECTORY EXISTS
# ============================================================

def ensure_directory(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


# ============================================================
# WRITE JSON
# ============================================================

def write_json(
    data: Any,
    output_file: str | Path,
    indent: int = 4,
) -> Path:
    """
    Write JSON using UTF-8 encoding.
    """

    output_file = Path(output_file)

    ensure_directory(output_file.parent)

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=indent,
        )

    return output_file


# ============================================================
# READ JSON
# ============================================================

def read_json(
    input_file: str | Path,
):
    """
    Safely read a JSON file.
    """

    input_file = Path(input_file)

    if not input_file.exists():

        return None

    with input_file.open(
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


# ============================================================
# APPEND RECORDS
# ============================================================

def append_records(
    output_file: str | Path,
    new_records: list[dict],
):
    """
    Append records to an existing JSON list.
    """

    existing = read_json(output_file)

    if existing is None:

        existing = []

    if not isinstance(existing, list):

        raise ValueError(
            "Existing JSON is not a list."
        )

    existing.extend(new_records)

    write_json(
        existing,
        output_file,
    )

    return len(existing)


# ============================================================
# EXPORTS
# ============================================================

__all__ = [
    "ensure_directory",
    "write_json",
    "read_json",
    "append_records",
]
