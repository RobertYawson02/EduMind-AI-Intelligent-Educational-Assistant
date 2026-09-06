"""
Akan Vocabulary Expansion Engine
Version 1.0

Purpose:
    Expand the existing Akan vocabulary foundation into a much larger,
    structured vocabulary dataset while preserving the existing schema.

Important:
    This generator does not modify the existing V3.0 knowledge base.
    It creates a separate expansion file that can later be validated
    and merged.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[3]

SOURCE_FILE = (
    ROOT
    / "data"
    / "akan"
    / "akan_knowledge_base.json"
)

OUTPUT_DIR = (
    ROOT
    / "data"
    / "akan"
    / "sources"
)

OUTPUT_FILE = OUTPUT_DIR / "vocabulary_expansion.json"


# ---------------------------------------------------------------------
# Vocabulary knowledge
# ---------------------------------------------------------------------

VOCABULARY_GROUPS: Dict[str, List[Dict[str, Any]]] = {

    "family": [
        {
            "akan": "agya",
            "english": "father",
            "category": "family",
            "meaning": "A male parent or a man who has the role of a father.",
            "related_words": ["ɛna", "abusua", "awofo"],
        },
        {
            "akan": "ɛna",
            "english": "mother",
            "category": "family",
            "meaning": "A female parent or a woman who has the role of a mother.",
            "related_words": ["agya", "abusua", "awofo"],
        },
        {
            "akan": "ɔba",
            "english": "child",
            "category": "family",
            "meaning": "A young human being in relation to a parent or family.",
            "related_words": ["abusua", "agya", "ɛna"],
        },
        {
            "akan": "abarimaa",
            "english": "boy",
            "category": "family",
            "meaning": "A male child or young male person.",
            "related_words": ["ɔba", "ababasia"],
        },
        {
            "akan": "ababasia",
            "english": "girl",
            "category": "family",
            "meaning": "A female child or young female person.",
            "related_words": ["ɔba", "abarimaa"],
        },
        {
            "akan": "ɔyere",
            "english": "wife",
            "category": "family",
            "meaning": "A married woman in relation to her husband.",
            "related_words": ["ɔkunu", "aware", "abusua"],
        },
        {
            "akan": "ɔkunu",
            "english": "husband",
            "category": "family",
            "meaning": "A married man in relation to his wife.",
            "related_words": ["ɔyere", "aware", "abusua"],
        },
        {
            "akan": "abusua",
            "english": "family",
            "category": "family",
            "meaning": "A group of people connected through kinship or descent.",
            "related_words": ["agya", "ɛna", "awofo"],
        },
        {
            "akan": "awofo",
            "english": "parents",
            "category": "family",
            "meaning": "The father and mother or people who have parental responsibility.",
            "related_words": ["agya", "ɛna", "abusua"],
        },
    ],

    "people": [
        {
            "akan": "onipa",
            "english": "person",
            "category": "people",
            "meaning": "A human being.",
            "related_words": ["nnipa", "ɔbarima", "ɔbaa"],
        },
        {
            "akan": "nnipa",
            "english": "people",
            "category": "people",
            "meaning": "Human beings considered as a group.",
            "related_words": ["onipa", "ɔman", "abusua"],
        },
        {
            "akan": "ɔbarima",
            "english": "man",
            "category": "people",
            "meaning": "An adult male person.",
            "related_words": ["ɔbaa", "onipa"],
        },
        {
            "akan": "ɔbaa",
            "english": "woman",
            "category": "people",
            "meaning": "An adult female person.",
            "related_words": ["ɔbarima", "onipa"],
        },
        {
            "akan": "ɔpanyin",
            "english": "elder",
            "category": "people",
            "meaning": "A respected older person, often recognized for experience and wisdom.",
            "related_words": ["nyansa", "obu", "abusua"],
        },
    ],

    "body": [
        {
            "akan": "ti",
            "english": "head",
            "category": "body",
            "meaning": "The uppermost part of the human body containing the brain, eyes, ears and other organs.",
            "related_words": ["ani", "aso", "ano"],
        },
        {
            "akan": "ani",
            "english": "eye",
            "category": "body",
            "meaning": "The organ used for seeing.",
            "related_words": ["ti", "hwɛ"],
        },
        {
            "akan": "aso",
            "english": "ear",
            "category": "body",
            "meaning": "The organ used for hearing.",
            "related_words": ["ti", "tie"],
        },
        {
            "akan": "ano",
            "english": "mouth",
            "category": "body",
            "meaning": "The opening through which a person eats and speaks.",
            "related_words": ["tɛkrɛma", "se"],
        },
        {
            "akan": "tɛkrɛma",
            "english": "tongue",
            "category": "body",
            "meaning": "The muscular organ in the mouth used for speaking, tasting and moving food.",
            "related_words": ["ano", "kasa"],
        },
        {
            "akan": "nsa",
            "english": "hand",
            "category": "body",
            "meaning": "The part of the body at the end of the arm used for holding and manipulating objects.",
            "related_words": ["abasa", "yɛ"],
        },
        {
            "akan": "nan",
            "english": "leg",
            "category": "body",
            "meaning": "A limb used for standing and walking.",
            "related_words": ["nantew", "nante"],
        },
    ],

    "nature": [
        {
            "akan": "nsuo",
            "english": "water",
            "category": "nature",
            "meaning": "A liquid essential for life, drinking, agriculture and many human activities.",
            "related_words": ["asubɔnten", "po", "osuo"],
        },
        {
            "akan": "osuo",
            "english": "rain",
            "category": "nature",
            "meaning": "Water that falls from clouds to the earth.",
            "related_words": ["nsuo", "ɔsram", "ewiem"],
        },
        {
            "akan": "ewiem",
            "english": "sky",
            "category": "nature",
            "meaning": "The space or apparent region above the earth.",
            "related_words": ["owia", "ɔsram", "ɔsoro"],
        },
        {
            "akan": "owia",
            "english": "sun",
            "category": "nature",
            "meaning": "The star that provides Earth with light and heat.",
            "related_words": ["ewiem", "awia"],
        },
        {
            "akan": "ɔsram",
            "english": "moon",
            "category": "nature",
            "meaning": "The natural satellite of the earth.",
            "related_words": ["ewiem", "owia"],
        },
        {
            "akan": "asubɔnten",
            "english": "river",
            "category": "nature",
            "meaning": "A natural flowing body of water.",
            "related_words": ["nsuo", "po"],
        },
        {
            "akan": "po",
            "english": "sea",
            "category": "nature",
            "meaning": "A large body of salt water connected with an ocean.",
            "related_words": ["nsuo", "asubɔnten"],
        },
    ],

    "food": [
        {
            "akan": "aduane",
            "english": "food",
            "category": "food",
            "meaning": "Something eaten or drunk to provide nourishment.",
            "related_words": ["didii", "nom", "aduan"],
        },
        {
            "akan": "emo",
            "english": "rice",
            "category": "food",
            "meaning": "A cereal grain commonly prepared and eaten as food.",
            "related_words": ["aduane", "nnuane"],
        },
        {
            "akan": "bankye",
            "english": "cassava",
            "category": "food",
            "meaning": "A root crop widely cultivated and eaten in many parts of Ghana.",
            "related_words": ["aduane", "dɔnkɔ"],
        },
        {
            "akan": "ɛmo",
            "english": "maize",
            "category": "food",
            "meaning": "A cereal crop commonly used as food.",
            "related_words": ["aduane", "afifide"],
        },
        {
            "akan": "nkyene",
            "english": "salt",
            "category": "food",
            "meaning": "A mineral substance commonly used to season food.",
            "related_words": ["aduane", "no"],
        },
    ],

    "school": [
        {
            "akan": "sukuu",
            "english": "school",
            "category": "education",
            "meaning": "An institution where people receive organized education.",
            "related_words": ["adesua", "ɔkyerɛkyerɛni", "osuani"],
        },
        {
            "akan": "osuani",
            "english": "student",
            "category": "education",
            "meaning": "A person who is studying or receiving formal education.",
            "related_words": ["sukuu", "adesua", "ɔkyerɛkyerɛni"],
        },
        {
            "akan": "ɔkyerɛkyerɛni",
            "english": "teacher",
            "category": "education",
            "meaning": "A person whose work involves teaching or educating others.",
            "related_words": ["sukuu", "osuani", "adesua"],
        },
        {
            "akan": "adesua",
            "english": "lesson",
            "category": "education",
            "meaning": "A period or unit of organized teaching and learning.",
            "related_words": ["sukuu", "osuani", "ɔkyerɛkyerɛni"],
        },
        {
            "akan": "nhoma",
            "english": "book",
            "category": "education",
            "meaning": "A written or printed work used for reading, learning or reference.",
            "related_words": ["kenkan", "adesua", "sukuu"],
        },
    ],

    "actions": [
        {
            "akan": "kasa",
            "english": "speak",
            "category": "action",
            "meaning": "To communicate using spoken words.",
            "related_words": ["tie", "ano", "tɛkrɛma"],
        },
        {
            "akan": "tie",
            "english": "hear",
            "category": "action",
            "meaning": "To perceive sound through the ears.",
            "related_words": ["aso", "kasa"],
        },
        {
            "akan": "hwɛ",
            "english": "look",
            "category": "action",
            "meaning": "To direct the eyes toward something.",
            "related_words": ["ani", "hu"],
        },
        {
            "akan": "hu",
            "english": "see",
            "category": "action",
            "meaning": "To perceive something with the eyes.",
            "related_words": ["ani", "hwɛ"],
        },
        {
            "akan": "nante",
            "english": "walk",
            "category": "action",
            "meaning": "To move from one place to another using the feet.",
            "related_words": ["nan", "akwantu"],
        },
        {
            "akan": "di",
            "english": "eat",
            "category": "action",
            "meaning": "To take food into the body through the mouth.",
            "related_words": ["aduane", "nom"],
        },
        {
            "akan": "nom",
            "english": "drink",
            "category": "action",
            "meaning": "To take liquid into the body through the mouth.",
            "related_words": ["nsuo", "aduane"],
        },
        {
            "akan": "kenkan",
            "english": "read",
            "category": "education",
            "meaning": "To look at and understand written words.",
            "related_words": ["nhoma", "sukuu", "adesua"],
        },
        {
            "akan": "kyerɛw",
            "english": "write",
            "category": "education",
            "meaning": "To represent words or ideas using written symbols.",
            "related_words": ["nhoma", "kenkan", "adesua"],
        },
    ],

    "qualities": [
        {
            "akan": "papa",
            "english": "good",
            "category": "quality",
            "meaning": "Having a desirable, useful or positive quality.",
            "related_words": ["bɔne", "fɛ", "yɛ"],
            "antonyms": ["bɔne"],
        },
        {
            "akan": "bɔne",
            "english": "bad",
            "category": "quality",
            "meaning": "Having an undesirable, harmful or negative quality.",
            "related_words": ["papa"],
            "antonyms": ["papa"],
        },
        {
            "akan": "kɛse",
            "english": "big",
            "category": "quality",
            "meaning": "Large in size, extent or importance.",
            "related_words": ["ketewa"],
            "antonyms": ["ketewa"],
        },
        {
            "akan": "ketewa",
            "english": "small",
            "category": "quality",
            "meaning": "Limited in size or extent.",
            "related_words": ["kɛse"],
            "antonyms": ["kɛse"],
        },
        {
            "akan": "fɛ",
            "english": "beautiful",
            "category": "quality",
            "meaning": "Having qualities that are pleasing to the senses or admired.",
            "related_words": ["papa"],
        },
        {
            "akan": "nyansa",
            "english": "wisdom",
            "category": "quality",
            "meaning": "The ability to make sound judgments based on knowledge and experience.",
            "related_words": ["nimdeɛ", "osuahunu"],
        },
        {
            "akan": "nimdeɛ",
            "english": "knowledge",
            "category": "education",
            "meaning": "Understanding or awareness gained through learning or experience.",
            "related_words": ["nyansa", "adesua"],
        },
    ],

    "time": [
        {
            "akan": "da",
            "english": "day",
            "category": "time",
            "meaning": "A period associated with daylight or a twenty-four-hour period.",
            "related_words": ["anɔpa", "awia", "anadwo"],
        },
        {
            "akan": "anɔpa",
            "english": "morning",
            "category": "time",
            "meaning": "The early part of the day.",
            "related_words": ["da", "awia"],
        },
        {
            "akan": "awia",
            "english": "afternoon",
            "category": "time",
            "meaning": "The part of the day after midday and before evening.",
            "related_words": ["anɔpa", "anadwo"],
        },
        {
            "akan": "anadwo",
            "english": "night",
            "category": "time",
            "meaning": "The period of darkness after evening.",
            "related_words": ["da", "awia", "anɔpa"],
        },
        {
            "akan": "ɛnnɛ",
            "english": "today",
            "category": "time",
            "meaning": "The current day.",
            "related_words": ["nkyɛ", "ɔkyena"],
        },
        {
            "akan": "ɔkyena",
            "english": "tomorrow",
            "category": "time",
            "meaning": "The day after today.",
            "related_words": ["ɛnnɛ"],
        },
    ],
}


# ---------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------

def normalize(value: str) -> str:
    """Normalize a string for duplicate detection."""

    value = str(value).strip().lower()
    value = re.sub(r"\s+", " ", value)

    return value


def stable_id(category: str, akan: str, english: str) -> str:
    """Generate a deterministic record ID."""

    category_key = re.sub(
        r"[^a-z0-9]+",
        "_",
        normalize(category),
    ).strip("_")

    akan_key = re.sub(
        r"[^a-z0-9]+",
        "_",
        normalize(akan),
    ).strip("_")

    english_key = re.sub(
        r"[^a-z0-9]+",
        "_",
        normalize(english),
    ).strip("_")

    return f"akan_vocab_{category_key}_{akan_key}_{english_key}"


def load_existing_records() -> List[Dict[str, Any]]:
    """Load the existing V3.0 knowledge base."""

    if not SOURCE_FILE.exists():
        return []

    try:
        with SOURCE_FILE.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            for key in (
                "records",
                "entries",
                "knowledge",
                "data",
                "items",
            ):
                if isinstance(data.get(key), list):
                    return data[key]

    except (OSError, json.JSONDecodeError):
        pass

    return []


def existing_pairs(
    records: List[Dict[str, Any]],
) -> set[tuple[str, str]]:
    """Build an existing Akan-English pair index."""

    pairs = set()

    for record in records:
        akan = record.get("akan") or record.get("twi") or record.get("word")
        english = record.get("english") or record.get("translation")

        if akan and english:
            pairs.add(
                (
                    normalize(str(akan)),
                    normalize(str(english)),
                )
            )

    return pairs


# ---------------------------------------------------------------------
# Record construction
# ---------------------------------------------------------------------

def build_record(
    item: Dict[str, Any],
    index: int,
) -> Dict[str, Any]:
    """Build a schema-compatible vocabulary record."""

    akan = str(item["akan"]).strip()
    english = str(item["english"]).strip()
    category = str(item["category"]).strip()
    meaning = str(item["meaning"]).strip()

    related_words = list(
        dict.fromkeys(
            str(value).strip()
            for value in item.get("related_words", [])
            if str(value).strip()
        )
    )

    synonyms = list(
        dict.fromkeys(
            str(value).strip()
            for value in item.get("synonyms", [])
            if str(value).strip()
        )
    )

    antonyms = list(
        dict.fromkeys(
            str(value).strip()
            for value in item.get("antonyms", [])
            if str(value).strip()
        )
    )

    examples = item.get("examples", [])

    if not examples:
        examples = [
            f"{akan} yɛ asɛm a wɔde kyerɛ {english}."
        ]

    return {
        "id": stable_id(
            category,
            akan,
            english,
        ),
        "language": "Akan",
        "language_variant": "Twi",
        "type": "vocabulary",
        "category": category,
        "word": akan,
        "akan": akan,
        "twi": akan,
        "english": english,
        "translation": english,
        "meaning": meaning,
        "definition": meaning,
        "examples": examples,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "related_words": related_words,
        "keywords": [
            akan,
            english,
            category,
        ],
        "source": "akan_curated_vocabulary_expansion",
        "version": "1.0",
        "quality": "curated",
    }


# ---------------------------------------------------------------------
# Expansion
# ---------------------------------------------------------------------

def generate_vocabulary() -> List[Dict[str, Any]]:
    """Generate new vocabulary records."""

    existing = load_existing_records()
    known = existing_pairs(existing)

    records: List[Dict[str, Any]] = []

    seen_ids = set()

    index = 1

    for category, items in VOCABULARY_GROUPS.items():

        for item in items:

            akan = normalize(item["akan"])
            english = normalize(item["english"])

            pair = (akan, english)

            if pair in known:
                continue

            record = build_record(
                item,
                index,
            )

            if record["id"] in seen_ids:
                continue

            seen_ids.add(record["id"])
            records.append(record)

            index += 1

    return records


# ---------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------

def save_records(records: List[Dict[str, Any]]) -> None:
    """Save expansion records separately."""

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

    print(
        f"Generated {len(records)} new vocabulary records."
    )

    print(
        f"Saved to: {OUTPUT_FILE}"
    )


def main() -> None:
    records = generate_vocabulary()

    save_records(records)


if __name__ == "__main__":
    main()
