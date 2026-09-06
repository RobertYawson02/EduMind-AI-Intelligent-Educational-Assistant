"""
==============================================================
AKAN KNOWLEDGE BASE BUILDER
Version 3.0
==============================================================

Purpose:
    Build the complete Akan knowledge base from the
    registered Akan knowledge generators.

The builder:

    1. Loads the Akan knowledge generators.
    2. Generates structured Akan records.
    3. Validates records using akan_schema.py.
    4. Detects duplicate record IDs.
    5. Combines all records.
    6. Saves the final knowledge base as JSON.

Output:
    data/akan/akan_knowledge_base.json

Schema:
    scripts/akan/data/akan_schema.py

==============================================================
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# IMPORT SCHEMA
# ============================================================

from scripts.akan.data.akan_schema import validate_akan_records


# ============================================================
# OUTPUT
# ============================================================

OUTPUT_DIR = PROJECT_ROOT / "data" / "akan"

OUTPUT_FILE = OUTPUT_DIR / "akan_knowledge_base.json"


# ============================================================
# GENERATOR MODULES
# ============================================================

GENERATOR_MODULES = [
    "scripts.akan.generators.culture_generator",
    "scripts.akan.generators.vocabulary_generator",
]


# ============================================================
# LOAD GENERATORS
# ============================================================

def load_generators():
    """
    Load all registered Akan knowledge generators.

    Each generator must provide:

        generate() -> list[dict]
    """

    generators = []

    for module_name in GENERATOR_MODULES:

        try:

            module = __import__(
                module_name,
                fromlist=["generate"],
            )

            generate_function = getattr(
                module,
                "generate",
            )

            generators.append(
                (
                    module_name,
                    generate_function,
                )
            )

            print(
                f"[OK] Loaded generator: {module_name}"
            )

        except ImportError as error:

            print(
                f"[WARNING] Could not import "
                f"{module_name}: {error}"
            )

        except AttributeError:

            print(
                f"[WARNING] Generator module does not "
                f"contain generate(): {module_name}"
            )

    return generators


# ============================================================
# GENERATE ALL RECORDS
# ============================================================

def generate_all_records():
    """
    Run every registered Akan generator.
    """

    generators = load_generators()

    if not generators:

        raise RuntimeError(
            "No Akan knowledge generators were loaded."
        )

    all_records = []

    for module_name, generate_function in generators:

        print()
        print(
            f"[INFO] Generating records from: "
            f"{module_name}"
        )

        records = generate_function()

        if not isinstance(records, list):

            raise ValueError(
                f"{module_name}.generate() must return a list."
            )

        print(
            f"[OK] Generated {len(records)} records."
        )

        all_records.extend(records)

    return all_records


# ============================================================
# CHECK DUPLICATE RECORD IDS
# ============================================================

def check_duplicate_record_ids(records):
    """
    Check for duplicate record IDs.

    Duplicate IDs are treated as an error because every
    knowledge record must have a unique identifier.
    """

    seen_ids = set()

    duplicate_ids = set()

    for record in records:

        record_id = record.get("record_id")

        if record_id in seen_ids:

            duplicate_ids.add(record_id)

        else:

            seen_ids.add(record_id)

    if duplicate_ids:

        duplicate_text = ", ".join(
            sorted(duplicate_ids)
        )

        raise ValueError(
            "Duplicate record IDs found: "
            + duplicate_text
        )

    print(
        "[OK] No duplicate record IDs found."
    )


# ============================================================
# VALIDATE RECORDS
# ============================================================

def validate_records(records):
    """
    Validate all records against akan_schema.py.
    """

    print()
    print(
        f"[INFO] Validating {len(records)} records..."
    )

    validate_akan_records(
        records
    )

    print(
        "[OK] All records passed Akan schema validation."
    )


# ============================================================
# SAVE KNOWLEDGE BASE
# ============================================================

def save_knowledge_base(records):
    """
    Save the final knowledge base to JSON.
    """

    OUTPUT_DIR.mkdir(
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
            indent=4,
        )

    print()
    print(
        "[OK] Knowledge base saved:"
    )

    print(
        f"     {OUTPUT_FILE}"
    )


# ============================================================
# BUILD
# ============================================================

def build():
    """
    Execute the complete Akan knowledge-base build process.
    """

    print()
    print("=" * 62)
    print("AKAN KNOWLEDGE BASE BUILDER")
    print("Version 3.0")
    print("=" * 62)

    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    print()
    print("[STEP 1] Generating Akan knowledge...")

    records = generate_all_records()

    print()
    print(
        f"[INFO] Total records generated: {len(records)}"
    )

    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    print()
    print("[STEP 2] Checking record IDs...")

    check_duplicate_record_ids(
        records
    )

    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    print()
    print("[STEP 3] Validating records...")

    validate_records(
        records
    )

    # --------------------------------------------------------
    # STEP 4
    # --------------------------------------------------------

    print()
    print("[STEP 4] Saving knowledge base...")

    save_knowledge_base(
        records
    )

    # --------------------------------------------------------
    # COMPLETE
    # --------------------------------------------------------

    print()
    print("=" * 62)
    print("AKAN KNOWLEDGE BASE BUILD COMPLETED")
    print("=" * 62)
    print()
    print(
        f"Total records: {len(records)}"
    )
    print(
        f"Output file: {OUTPUT_FILE}"
    )
    print()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        build()

    except Exception as error:

        print()
        print("=" * 62)
        print("AKAN KNOWLEDGE BASE BUILD FAILED")
        print("=" * 62)
        print()
        print(
            f"[ERROR] {error}"
        )
        print()

        raise
