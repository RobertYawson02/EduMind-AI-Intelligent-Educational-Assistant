"""
Ghana-QA Twi Importer
Version 1.0

Imports a controlled subset of the official Ghana NLP Community
Twi QA dataset into the project's Akan retrieval corpus.

The source dataset is external and remains attributed.
Imported records are clearly marked as external_qa records.

No original curated Akan records are modified.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple

import pandas as pd
from huggingface_hub import hf_hub_download


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_DIR = (
    ROOT
    / "data"
    / "akan"
    / "sources"
)

OUTPUT_FILE = (
    OUTPUT_DIR
    / "ghana_qa_twi_import.json"
)

SOURCE_REPO = "ghananlpcommunity/ghana-qa"
SOURCE_FILE = "twi.csv"

# Controlled import size.
# Increase this later after validation.
MAX_RECORDS = 20000

CHUNK_SIZE = 5000


def normalize(value: Any) -> str:
    if value is None:
        return ""

    value = str(value).strip().lower()

    return re.sub(
        r"\s+",
        " ",
        value,
    )


def clean(value: Any) -> str:
    if value is None:
        return ""

    return str(value).strip()


def stable_id(question: str, answer: str) -> str:
    import hashlib

    raw = (
        normalize(question)
        + "||"
        + normalize(answer)
    )

    digest = hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()[:20]

    return f"ghana_qa_twi_{digest}"


def is_valid(question: str, answer: str) -> bool:
    if not question or not answer:
        return False

    # Reject extremely short/noisy rows.
    if len(question) < 5:
        return False

    if len(answer) < 2:
        return False

    # Reject obvious placeholder values.
    bad_values = {
        "nan",
        "none",
        "null",
        "n/a",
    }

    if normalize(question) in bad_values:
        return False

    if normalize(answer) in bad_values:
        return False

    return True


def build_record(
    question: str,
    answer: str,
    number: int,
) -> Dict[str, Any]:

    return {
        "id": stable_id(
            question,
            answer,
        ),
        "language": "Akan",
        "language_variant": "Twi",

        "type": "qa_retrieval",
        "record_role": "external_qa",

        "category": "general_knowledge",

        "question": question,
        "answer": answer,

        "word": "",
        "akan": "",
        "twi": "",

        "english": "",
        "translation": "",

        "meaning": "",
        "definition": "",

        "examples": [],
        "synonyms": [],
        "antonyms": [],
        "related_words": [],

        "keywords": [
            question,
        ],

        "intent": "general",

        "source": "Ghana-QA",
        "source_dataset": SOURCE_REPO,
        "source_file": SOURCE_FILE,

        "source_record_number": number,

        "license": "CC BY-NC 4.0",

        "quality": (
            "external_dataset_"
            "requires_validation"
        ),

        "version": "1.0",
    }


def download_source() -> str:
    print(
        "Downloading/loading Twi QA source..."
    )

    path = hf_hub_download(
        repo_id=SOURCE_REPO,
        filename=SOURCE_FILE,
        repo_type="dataset",
    )

    print(
        f"Source available at: {path}"
    )

    return path


def import_records(
    source_path: str,
) -> List[Dict[str, Any]]:

    records: List[Dict[str, Any]] = []

    seen: Set[
        Tuple[str, str]
    ] = set()

    processed = 0

    for chunk in pd.read_csv(
        source_path,
        chunksize=CHUNK_SIZE,
    ):

        # The repository's Twi file is already
        # Twi-specific, but support a language
        # column when present.
        if "lang" in chunk.columns:

            chunk = chunk[
                chunk["lang"]
                .astype(str)
                .str.lower()
                .eq("twi")
            ]

        if "question" not in chunk.columns:
            raise ValueError(
                "Expected 'question' column "
                "was not found."
            )

        if "answer" not in chunk.columns:
            raise ValueError(
                "Expected 'answer' column "
                "was not found."
            )

        for _, row in chunk.iterrows():

            question = clean(
                row["question"]
            )

            answer = clean(
                row["answer"]
            )

            if not is_valid(
                question,
                answer,
            ):
                continue

            key = (
                normalize(question),
                normalize(answer),
            )

            if key in seen:
                continue

            seen.add(key)

            processed += 1

            records.append(
                build_record(
                    question,
                    answer,
                    processed,
                )
            )

            if len(records) >= MAX_RECORDS:
                return records

    return records


def save(
    records: List[Dict[str, Any]],
) -> None:

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
            indent=2,
        )


def main() -> None:

    print()
    print("=" * 72)
    print("GHANA-QA TWi IMPORT")
    print("=" * 72)

    print(
        f"Maximum records: {MAX_RECORDS}"
    )

    source_path = download_source()

    records = import_records(
        source_path
    )

    save(records)

    print()
    print(
        f"Imported records: {len(records)}"
    )

    print(
        f"Output: {OUTPUT_FILE}"
    )

    print()
    print(
        "IMPORTANT:"
    )

    print(
        "Imported records are external QA "
        "material and remain clearly attributed."
    )

    print(
        "They have not replaced the curated "
        "Akan knowledge base."
    )

    print("=" * 72)


if __name__ == "__main__":
    main()
