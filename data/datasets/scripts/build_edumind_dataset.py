"""EduMind AI dataset acquisition and processing pipeline.

This project keeps its working architecture intact while adding a practical,
local dataset processing path for a manageable Ghanaian-language development
sample. The builder reads local raw CSV/JSON sources, normalizes records, drops
empty duplicates, and writes a processed dataset that the app can load lazily.
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
DATASETS = DATA / "datasets"
DOWNLOADS = DATASETS / "downloads"
PROCESSED = DATASETS / "processed"
MANIFEST_PATH = DATASETS / "dataset_manifest.json"

DOWNLOADS.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", "")
    text = text.replace("\r", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def candidate_files() -> List[Path]:
    files = []
    for directory in [DOWNLOADS, DATASETS]:
        if directory.exists():
            files.extend(sorted(directory.rglob("*.csv")))
            files.extend(sorted(directory.rglob("*.json")))
    unique = []
    seen = set()
    for path in files:
        key = str(path.resolve())
        if key not in seen:
            unique.append(path)
            seen.add(key)
    return unique


def load_csv_records(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not row:
                continue
            rows.append({key: value for key, value in row.items()})
    return rows


def load_json_records(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        items = payload.get("records") or payload.get("data") or payload.get("items")
        if isinstance(items, list):
            return [item for item in items if isinstance(item, dict)]
    return []


def normalize_record(raw: Dict[str, Any]) -> Dict[str, Any]:
    english = normalize_text(
        raw.get("english")
        or raw.get("en")
        or raw.get("source_text")
        or raw.get("question")
        or raw.get("query")
        or raw.get("prompt")
        or raw.get("input")
        or ""
    )
    twi = normalize_text(
        raw.get("twi")
        or raw.get("akan")
        or raw.get("target")
        or raw.get("answer")
        or raw.get("translation")
        or raw.get("response")
        or raw.get("output")
        or ""
    )

    if not english and "text" in raw:
        english = normalize_text(raw.get("text"))
    if not twi and "value" in raw:
        twi = normalize_text(raw.get("value"))

    category = normalize_text(raw.get("category") or raw.get("type") or "translation")
    if not category:
        category = "translation"

    record = OrderedDict()
    record["id"] = normalize_text(raw.get("id") or f"record_{abs(hash(str(raw)) % 1000000)}")
    record["source"] = normalize_text(raw.get("source") or "GhanaNLP")
    record["language"] = normalize_text(raw.get("language") or "Twi")
    record["source_language"] = normalize_text(raw.get("source_language") or "English")
    record["english"] = english
    record["twi"] = twi
    record["category"] = category

    for key in ["source_url", "notes", "license", "dataset"]:
        value = raw.get(key)
        if value not in (None, ""):
            record[key] = normalize_text(value)

    return record


def deduplicate(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    final: List[Dict[str, Any]] = []
    for record in records:
        english = normalize_text(record.get("english"))
        twi = normalize_text(record.get("twi"))
        key = (english.lower(), twi.lower())
        if not english or not twi:
            continue
        if key in seen:
            continue
        seen.add(key)
        final.append(record)
    return final


def build_processed_dataset() -> List[Dict[str, Any]]:
    raw_sources: List[Path] = []

    preferred_files = [
        DATASETS / "ghana_qa_sample.csv",
        DOWNLOADS / "ghana_qa_sample.csv",
        DATASETS / "ghana_qa.csv",
        DOWNLOADS / "ghana_qa.csv",
    ]
    for path in preferred_files:
        if path.exists():
            raw_sources.append(path)

    for path in candidate_files():
        if path.name in {"ghana_qa_sample.csv", "ghana_qa.csv", "edumind_twi_english.csv", "edumind_twi_english.json"}:
            continue
        if path.suffix.lower() in {".csv", ".json"}:
            raw_sources.append(path)

    records: List[Dict[str, Any]] = []
    for path in raw_sources:
        try:
            if path.suffix.lower() == ".csv":
                rows = load_csv_records(path)
                records.extend(normalize_record(row) for row in rows)
            elif path.suffix.lower() == ".json":
                rows = load_json_records(path)
                records.extend(normalize_record(row) for row in rows)
        except Exception as exc:
            print(f"Skipping unreadable source [{path.name}]: {exc}")

    cleaned = deduplicate(records)
    return cleaned


def write_json_dataset(records: List[Dict[str, Any]], path: Path) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(records, handle, ensure_ascii=False, indent=2)


def write_csv_dataset(records: List[Dict[str, Any]], path: Path) -> None:
    fieldnames = ["id", "source", "language", "source_language", "english", "twi", "category"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow({key: record.get(key, "") for key in fieldnames})


def update_manifest(count: int, dataset_path: Path) -> None:
    manifest = {
        "dataset_name": "edumind_twi_english",
        "source": "GhanaNLP sample / local educational Twi QA dataset",
        "status": "processed",
        "processed_file": str(dataset_path.relative_to(ROOT)),
        "record_count": count,
        "language_pairs": ["Twi", "English"],
        "notes": "Development sample used to validate the in-project dataset acquisition and processing pipeline.",
    }
    with MANIFEST_PATH.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)


def main() -> None:
    print("=" * 60)
    print("EduMind AI Dataset Builder")
    print("=" * 60)
    print(f"Project Root : {ROOT}")
    print(f"Downloads    : {DOWNLOADS}")
    print(f"Processed    : {PROCESSED}")

    record_list = build_processed_dataset()
    print(f"Raw candidate files : {len(candidate_files())}")
    print(f"Normalized records : {len(record_list)}")

    if not record_list:
        print("No valid records were found. Creating an empty processed dataset shell.")
        record_list = []

    output_json = PROCESSED / "edumind_twi_english.json"
    output_csv = PROCESSED / "edumind_twi_english.csv"
    write_json_dataset(record_list, output_json)
    write_csv_dataset(record_list, output_csv)

    update_manifest(len(record_list), output_json)

    print(f"Processed JSON : {output_json}")
    print(f"Processed CSV  : {output_csv}")
    print(f"Manifest       : {MANIFEST_PATH}")
    print("Dataset workspace ready.")


if __name__ == "__main__":
    main()
