"""
==============================================================
BUILD KNOWLEDGE BASE V3
Intelligent Educational Assistant
==============================================================

Purpose:
    Modular knowledge-base generation system.

Architecture:

    build_knowledge_base.py
            |
            +-- generators/
                  |
                  +-- common.py
                  +-- computer_science.py
                  +-- programming.py
                  +-- networking.py
                  +-- cybersecurity.py
                  +-- web_development.py
                  +-- artificial_intelligence.py
                  +-- data_science.py
                  +-- database_systems.py
                  +-- cloud_computing.py
                  +-- operating_systems.py
                  +-- software_engineering.py
                  +-- internet_of_things.py
                  +-- mathematics.py
                  +-- digital_electronics.py
                  +-- general_science.py
                  +-- research.py
                  +-- study_skills.py
                  +-- academic_writing.py
                  +-- career.py

The builder automatically discovers generator modules.

Generator requirement:

    Each subject generator must contain:

        generate()

    and return either:

        list[dict]

    or:

        dict

The standard JSON schema is preserved:

{
    "topic": "...",
    "keywords": [...],
    "definition": "...",
    "explanation": "...",
    "examples": [...],
    "category": "..."
}

Output:
    data/educational_knowledge.json

Version:
    3.0

==============================================================
"""

from __future__ import annotations

import importlib
import json
import os
import sys
from collections import Counter
from datetime import datetime


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SCRIPTS_DIR = os.path.join(
    BASE_DIR,
    "scripts"
)

GENERATORS_DIR = os.path.join(
    SCRIPTS_DIR,
    "generators"
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

OUTPUT_FILE = os.path.join(
    DATA_DIR,
    "educational_knowledge.json"
)


# ============================================================
# ENSURE DIRECTORIES EXIST
# ============================================================

os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# ============================================================
# PYTHON PACKAGE PATH
# ============================================================

# Make the project root importable so that:
#
#     scripts.generators.module
#
# can be imported correctly.

if BASE_DIR not in sys.path:
    sys.path.insert(
        0,
        BASE_DIR
    )


# ============================================================
# VERSION
# ============================================================

BUILDER_VERSION = "3.0"

TARGET_MINIMUM = 15000


# ============================================================
# RECORD SCHEMA
# ============================================================

REQUIRED_FIELDS = {
    "topic",
    "keywords",
    "definition",
    "explanation",
    "examples",
    "category",
}


# ============================================================
# RECORD VALIDATION
# ============================================================

def validate_record(record: dict) -> bool:
    """
    Validate the standard knowledge-base record schema.
    """

    if not isinstance(
        record,
        dict
    ):
        return False

    if not REQUIRED_FIELDS.issubset(
        record.keys()
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

    if not isinstance(
        record["definition"],
        str
    ):
        return False

    if not isinstance(
        record["explanation"],
        str
    ):
        return False

    if not isinstance(
        record["examples"],
        list
    ):
        return False

    if not isinstance(
        record["category"],
        str
    ):
        return False

    if not record["category"].strip():
        return False

    return True


# ============================================================
# DUPLICATE KEY
# ============================================================

def record_key(record: dict) -> str:
    """
    Create a stable duplicate key.
    """

    topic = str(
        record.get(
            "topic",
            ""
        )
    ).strip().lower()

    category = str(
        record.get(
            "category",
            ""
        )
    ).strip().lower()

    definition = str(
        record.get(
            "definition",
            ""
        )
    ).strip().lower()

    return (
        f"{category}|"
        f"{topic}|"
        f"{definition}"
    )


# ============================================================
# DISCOVER GENERATORS
# ============================================================

def discover_generators():
    """
    Automatically discover generator modules inside:

        scripts/generators/

    Each valid module must contain:

        generate()

    Generators are imported as proper Python packages:

        scripts.generators.module_name

    This is important because generator modules may contain
    relative imports such as:

        from .common import build_record

    Files ignored:

        __init__.py
        common.py
        private files beginning with "_"
    """

    generators = []

    if not os.path.isdir(
        GENERATORS_DIR
    ):

        raise RuntimeError(
            "Generator directory not found:\n"
            f"{GENERATORS_DIR}"
        )

    print(
        f"Generator directory: {GENERATORS_DIR}"
    )

    print()

    # --------------------------------------------------------
    # Discover Python files
    # --------------------------------------------------------

    for filename in sorted(
        os.listdir(
            GENERATORS_DIR
        )
    ):

        if not filename.endswith(
            ".py"
        ):
            continue

        if filename.startswith(
            "_"
        ):
            continue

        if filename == "common.py":
            continue

        module_name = filename[:-3]

        package_module_name = (
            f"scripts.generators."
            f"{module_name}"
        )

        print(
            f"Discovering: {package_module_name}"
        )

        try:

            # ------------------------------------------------
            # Import as a proper package module
            # ------------------------------------------------

            module = importlib.import_module(
                package_module_name
            )

        except Exception as exc:

            print(
                f"WARNING: Could not import "
                f"{filename}: "
                f"{type(exc).__name__}: {exc}"
            )

            continue

        # ----------------------------------------------------
        # Find generate()
        # ----------------------------------------------------

        generate_function = getattr(
            module,
            "generate",
            None
        )

        if not callable(
            generate_function
        ):

            print(
                f"WARNING: {filename} does not "
                f"contain generate()"
            )

            print()

            continue

        generators.append(
            (
                module_name,
                module,
                generate_function
            )
        )

        print(
            f"  OK -> {module_name}"
        )

        print()

    return generators


# ============================================================
# NORMALIZE GENERATED DATA
# ============================================================

def normalize_generated(
    generated
):
    """
    Normalize generator output into a list.

    Accepted:

        dict
        list
        tuple

    Returns:

        list
    """

    if generated is None:

        raise RuntimeError(
            "generate() returned None"
        )

    if isinstance(
        generated,
        dict
    ):

        return [
            generated
        ]

    if isinstance(
        generated,
        (list, tuple)
    ):

        return list(
            generated
        )

    raise TypeError(
        "generate() must return "
        "a list, tuple, or dictionary"
    )


# ============================================================
# BUILD KNOWLEDGE BASE
# ============================================================

def build_knowledge_base():
    """
    Execute all discovered generators.

    Returns:

        records
        domain_statistics
        module_statistics
        duplicate_count
        invalid_count
        generator_errors
    """

    records = []

    seen = set()

    domain_statistics = Counter()

    module_statistics = Counter()

    duplicate_count = 0

    invalid_count = 0

    generator_errors = []

    generators = discover_generators()

    print(
        f"Generators discovered: "
        f"{len(generators)}"
    )

    print()

    if not generators:

        raise RuntimeError(
            "No valid generator modules were discovered."
        )

    # --------------------------------------------------------
    # Generator execution
    # --------------------------------------------------------

    print(
        "=" * 70
    )

    print(
        "RUNNING GENERATORS"
    )

    print(
        "=" * 70
    )

    print()

    for (
        module_name,
        module,
        generate_function
    ) in generators:

        print(
            f"Generating: {module_name}"
        )

        module_start = len(
            records
        )

        try:

            generated = generate_function()

            generated = normalize_generated(
                generated
            )

            # ------------------------------------------------
            # Process records
            # ------------------------------------------------

            for record in generated:

                # --------------------------------------------
                # Validate
                # --------------------------------------------

                if not validate_record(
                    record
                ):

                    invalid_count += 1

                    continue

                # --------------------------------------------
                # Duplicate detection
                # --------------------------------------------

                key = record_key(
                    record
                )

                if key in seen:

                    duplicate_count += 1

                    continue

                seen.add(
                    key
                )

                # --------------------------------------------
                # Store record
                # --------------------------------------------

                records.append(
                    record
                )

                category = str(
                    record.get(
                        "category",
                        "Unknown"
                    )
                ).strip()

                domain_statistics[
                    category
                ] += 1

                module_statistics[
                    module_name
                ] += 1

            module_total = (
                len(records)
                - module_start
            )

            print(
                f"  PASS -> "
                f"{module_total:,} records"
            )

        except Exception as exc:

            generator_errors.append(
                {
                    "module": module_name,
                    "error_type": type(
                        exc
                    ).__name__,
                    "error": str(
                        exc
                    )
                }
            )

            print(
                f"  FAIL -> "
                f"{type(exc).__name__}: "
                f"{exc}"
            )

        print()

    return (
        records,
        domain_statistics,
        module_statistics,
        duplicate_count,
        invalid_count,
        generator_errors
    )


# ============================================================
# SORT RECORDS
# ============================================================

def sort_records(
    records: list[dict]
) -> list[dict]:
    """
    Sort records consistently by:

        category
        topic
        definition
    """

    return sorted(
        records,
        key=lambda record: (
            str(
                record.get(
                    "category",
                    ""
                )
            ).lower(),

            str(
                record.get(
                    "topic",
                    ""
                )
            ).lower(),

            str(
                record.get(
                    "definition",
                    ""
                )
            ).lower()
        )
    )


# ============================================================
# FINAL DATABASE VALIDATION
# ============================================================

def validate_final_database(
    records: list[dict]
):
    """
    Perform a final validation pass.
    """

    valid_records = []

    invalid_records = 0

    for record in records:

        if validate_record(
            record
        ):

            valid_records.append(
                record
            )

        else:

            invalid_records += 1

    return (
        valid_records,
        invalid_records
    )


# ============================================================
# SAVE KNOWLEDGE BASE
# ============================================================

def save_knowledge_base(
    records: list[dict]
) -> None:
    """
    Safely save the generated knowledge base.

    The JSON is first written to a temporary file.
    Only after successful completion is it moved into
    the final location.
    """

    temporary_file = (
        OUTPUT_FILE
        + ".tmp"
    )

    with open(
        temporary_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            indent=4,
            ensure_ascii=False
        )

    os.replace(
        temporary_file,
        OUTPUT_FILE
    )


# ============================================================
# GENERATION REPORT
# ============================================================

def print_report(
    records,
    domain_statistics,
    module_statistics,
    duplicate_count,
    invalid_count,
    generator_errors
):

    print()

    print(
        "=" * 70
    )

    print(
        "KNOWLEDGE BASE GENERATION REPORT"
    )

    print(
        "=" * 70
    )

    print(
        f"Builder version       : "
        f"{BUILDER_VERSION}"
    )

    print(
        "Generated at          : "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(
        f"Final records         : "
        f"{len(records):,}"
    )

    print(
        f"Duplicates removed    : "
        f"{duplicate_count:,}"
    )

    print(
        f"Invalid records       : "
        f"{invalid_count:,}"
    )

    print(
        f"Generator failures    : "
        f"{len(generator_errors):,}"
    )

    print()

    # --------------------------------------------------------
    # Domain statistics
    # --------------------------------------------------------

    print(
        "-" * 70
    )

    print(
        "RECORDS BY DOMAIN"
    )

    print(
        "-" * 70
    )

    for category in sorted(
        domain_statistics
    ):

        print(
            f"{category:<40}"
            f"{domain_statistics[category]:>10,}"
        )

    print()

    # --------------------------------------------------------
    # Generator statistics
    # --------------------------------------------------------

    print(
        "-" * 70
    )

    print(
        "RECORDS BY GENERATOR"
    )

    print(
        "-" * 70
    )

    for module_name in sorted(
        module_statistics
    ):

        print(
            f"{module_name:<40}"
            f"{module_statistics[module_name]:>10,}"
        )

    print()

    # --------------------------------------------------------
    # Generator errors
    # --------------------------------------------------------

    if generator_errors:

        print(
            "-" * 70
        )

        print(
            "GENERATOR ERRORS"
        )

        print(
            "-" * 70
        )

        for error in generator_errors:

            print(
                f"{error['module']}: "
                f"{error['error_type']}: "
                f"{error['error']}"
            )

        print()

    # --------------------------------------------------------
    # Target status
    # --------------------------------------------------------

    print(
        "-" * 70
    )

    if len(records) >= TARGET_MINIMUM:

        print(
            f"TARGET STATUS       : PASS "
            f"({len(records):,} >= "
            f"{TARGET_MINIMUM:,})"
        )

    else:

        remaining = (
            TARGET_MINIMUM
            - len(records)
        )

        print(
            "TARGET STATUS       : "
            "EXPANSION REQUIRED"
        )

        print(
            f"Records remaining   : "
            f"{remaining:,}"
        )

    print()

    print(
        f"OUTPUT FILE         : "
        f"{OUTPUT_FILE}"
    )

    print(
        "=" * 70
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print()

    print(
        "=" * 70
    )

    print(
        "BUILDING EDUCATIONAL KNOWLEDGE BASE V3"
    )

    print(
        "=" * 70
    )

    print()

    print(
        f"PROJECT ROOT: {BASE_DIR}"
    )

    print(
        f"GENERATOR PATH: "
        f"{GENERATORS_DIR}"
    )

    print(
        f"OUTPUT PATH: "
        f"{OUTPUT_FILE}"
    )

    print()

    # --------------------------------------------------------
    # Verify generator directory
    # --------------------------------------------------------

    if not os.path.isdir(
        GENERATORS_DIR
    ):

        print(
            "ERROR: Generator directory does not exist."
        )

        print(
            GENERATORS_DIR
        )

        return 1

    # --------------------------------------------------------
    # Build
    # --------------------------------------------------------

    try:

        (
            records,
            domain_statistics,
            module_statistics,
            duplicate_count,
            invalid_count,
            generator_errors
        ) = build_knowledge_base()

    except Exception as exc:

        print()

        print(
            "BUILD FAILED"
        )

        print(
            f"{type(exc).__name__}: "
            f"{exc}"
        )

        return 1

    # --------------------------------------------------------
    # Sort
    # --------------------------------------------------------

    records = sort_records(
        records
    )

    # --------------------------------------------------------
    # Final validation
    # --------------------------------------------------------

    (
        records,
        final_invalid_count
    ) = validate_final_database(
        records
    )

    invalid_count += (
        final_invalid_count
    )

    # --------------------------------------------------------
    # Do not overwrite the database if nothing was generated
    # --------------------------------------------------------

    if not records:

        print()

        print(
            "ERROR: No valid knowledge records "
            "were generated."
        )

        print(
            "The existing knowledge base was "
            "not replaced."
        )

        return 1

    # --------------------------------------------------------
    # Save
    # --------------------------------------------------------

    try:

        save_knowledge_base(
            records
        )

    except Exception as exc:

        print()

        print(
            "ERROR: Could not save knowledge base."
        )

        print(
            f"{type(exc).__name__}: "
            f"{exc}"
        )

        return 1

    # --------------------------------------------------------
    # Report
    # --------------------------------------------------------

    print_report(
        records,
        domain_statistics,
        module_statistics,
        duplicate_count,
        invalid_count,
        generator_errors
    )

    print()

    # --------------------------------------------------------
    # Final status
    # --------------------------------------------------------

    if generator_errors:

        print(
            "WARNING: One or more generators failed."
        )

        print(
            "The database was saved, but the build "
            "is considered FAILED."
        )

        return 1

    if len(records) >= TARGET_MINIMUM:

        print(
            "All generators completed successfully."
        )

        print(
            "TARGET ACHIEVED."
        )

    else:

        print(
            "All discovered generators completed successfully."
        )

        print(
            "The database requires further expansion "
            "to reach the target."
        )

    print(
        "Knowledge base build completed."
    )

    print()

    return 0


# ============================================================
# DIRECT EXECUTION
# ============================================================

if __name__ == "__main__":

    raise SystemExit(
        main()
    )

