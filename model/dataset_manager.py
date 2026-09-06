"""Dataset loading and lightweight caching for the QA system."""

import json
import os
import re
import unicodedata

import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(BASE, "data", "datasets")
PROCESSED_DIR = os.path.join(DIR, "processed")
FILES = {
    "ghana_qa": ["ghana_qa.csv", "ghana_qa_sample.csv"],
    "twi_parallel": ["twi_english_parallel.csv"],
    "twi_english": [
        "edumind_twi_english.json",
        "edumind_twi_english.csv",
    ],
}
_cache = {}


def _normalize_text(value):
    if value is None:
        return ""
    text = str(value).strip()
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u200b", "")
    text = text.replace("\r", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def dataset_path(name):
    for filename in FILES.get(name, []):
        path = os.path.join(DIR, filename)
        if os.path.isfile(path):
            return path

    if name == "twi_english":
        for filename in ["edumind_twi_english.json", "edumind_twi_english.csv"]:
            path = os.path.join(PROCESSED_DIR, filename)
            if os.path.isfile(path):
                return path

    return None


def dataset_available(name):
    return dataset_path(name) is not None


def normalize_twi_record(record):
    if not isinstance(record, dict):
        return {}

    english = _normalize_text(
        record.get("english")
        or record.get("en")
        or record.get("source_text")
        or record.get("question")
        or record.get("query")
        or ""
    )
    twi = _normalize_text(
        record.get("twi")
        or record.get("akan")
        or record.get("target")
        or record.get("answer")
        or record.get("translation")
        or record.get("response")
        or ""
    )

    category = _normalize_text(record.get("category") or record.get("type") or "translation")
    if not category:
        category = "translation"

    cleaned = {
        "id": _normalize_text(record.get("id") or f"twi_{len(english) + len(twi)}"),
        "source": _normalize_text(record.get("source") or "GhanaNLP"),
        "language": _normalize_text(record.get("language") or "Twi"),
        "source_language": _normalize_text(record.get("source_language") or "English"),
        "english": english,
        "twi": twi,
        "category": category,
    }

    if "source_url" in record and record.get("source_url"):
        cleaned["source_url"] = _normalize_text(record.get("source_url"))

    for key in ["notes", "license", "dataset"]:
        if key in record and record.get(key):
            cleaned[key] = _normalize_text(record.get(key))

    return cleaned


def _load_json_dataset(path):
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, list):
        return [normalize_twi_record(item) for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        items = payload.get("records") or payload.get("data") or payload.get("items")
        if isinstance(items, list):
            return [normalize_twi_record(item) for item in items if isinstance(item, dict)]
    return []


def load_processed_twi_dataset():
    path = dataset_path("twi_english")
    if not path:
        return []
    if path.endswith(".json"):
        data = _load_json_dataset(path)
        _cache["twi_english"] = data
        return data

    try:
        df = pd.read_csv(path)
        if df is None or df.empty:
            return []
        rows = []
        for _, row in df.iterrows():
            cleaned = normalize_twi_record(row.to_dict())
            if cleaned.get("english") and cleaned.get("twi"):
                rows.append(cleaned)
        _cache["twi_english"] = rows
        return rows
    except Exception as exc:
        print(f"Processed dataset load error [{path}]: {exc}")
        return []


def load_dataset(name):
    if name in _cache:
        return _cache[name]

    if name == "twi_english":
        rows = load_processed_twi_dataset()
        _cache[name] = rows
        return rows

    path = dataset_path(name)
    if not path:
        return None
    try:
        df = pd.read_csv(path)
        if df is None or df.empty:
            return None
        _cache[name] = df
        return df
    except Exception as exc:
        print(f"Dataset load error [{name}]: {exc}")
        return None


def clear_dataset_cache():
    _cache.clear()
