""" 
==============================================================
AKAN VOCABULARY GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate structured Akan vocabulary knowledge records.

All records are created through the shared Version 3.0
Akan schema.

The generator produces UNIQUE vocabulary records from the
defined word banks. It does not duplicate the same word simply
to reach a target number.

==============================================================
"""

from __future__ import annotations

from scripts.akan.data.akan_schema import create_akan_record


# ============================================================
# WORD BANKS
# ============================================================

WORD_BANKS = {

    "people": [
        ("abarimaa", "boy"),
        ("abaa", "girl"),
        ("ɔbarima", "man"),
        ("ɔbaa", "woman"),
        ("abofra", "child"),
        ("adamfo", "friend"),
        ("ɔkyerɛkyerɛni", "teacher"),
        ("osuani", "student"),
        ("ɔsɔfo", "pastor"),
        ("oduruyɛfo", "doctor"),
        ("ɔpanyin", "elder"),
        ("ɔhene", "chief"),
        ("ɔbaahemaa", "queenmother"),
        ("ɔwarefo", "spouse"),
        ("abusuani", "relative"),
        ("ɔwofo", "parent"),
        ("agya", "father"),
        ("ɛna", "mother"),
        ("ɔba", "child"),
        ("onuabarima", "brother"),
        ("onuabaa", "sister"),
        ("nana", "grandparent"),
        ("nanabarima", "grandfather"),
        ("nanaabaa", "grandmother"),
        ("abusua", "family"),
    ],

    "family": [
        ("agya", "father"),
        ("ɛna", "mother"),
        ("ba", "child"),
        ("ɔba", "child"),
        ("abarimaa", "son"),
        ("abaa", "daughter"),
        ("onuabarima", "brother"),
        ("onuabaa", "sister"),
        ("nua", "sibling"),
        ("agyaase", "paternal relative"),
        ("ɛnaase", "maternal relative"),
        ("abusua", "family"),
        ("abusuafo", "family members"),
        ("abusua panyin", "family head"),
        ("awofo", "parents"),
        ("nanabarima", "grandfather"),
        ("nanaabaa", "grandmother"),
        ("nana", "grandparent"),
        ("abusua panyin", "family elder"),
        ("yere", "wife"),
        ("okunu", "husband"),
    ],

    "body": [
        ("ti", "head"),
        ("ani", "eye"),
        ("aso", "ear"),
        ("ano", "mouth"),
        ("tɛkrɛma", "tongue"),
        ("se", "tooth"),
        ("ɔkɔn", "neck"),
        ("nsa", "hand"),
        ("nsateaa", "finger"),
        ("ban", "arm"),
        ("nantin", "foot"),
        ("nan", "leg"),
        ("kotoku", "stomach"),
        ("akoma", "heart"),
        ("mogya", "blood"),
        ("honam", "body"),
        ("ti nhwi", "hair"),
        ("aniwa", "eye"),
        ("afuru", "belly"),
        ("akyi", "back"),
        ("abasa", "shoulder"),
        ("kotodwe", "knee"),
        ("nan ase", "sole of the foot"),
    ],

    "food": [
        ("fufu", "fufu"),
        ("banku", "banku"),
        ("ampesi", "boiled food"),
        ("nkwan", "soup"),
        ("borɔdeɛ", "plantain"),
        ("bankye", "cassava"),
        ("bayere", "yam"),
        ("koko", "porridge"),
        ("ɛmo", "rice"),
        ("aburo", "maize"),
        ("emo", "rice"),
        ("aduane", "food"),
        ("nkyene", "salt"),
        ("sukɔre", "sugar"),
        ("ngo", "oil"),
        ("nsuo", "water"),
        ("nufusu", "milk"),
        ("kosua", "egg"),
        ("nam", "meat"),
        ("apataa", "fish"),
        ("borɔferɛ", "pineapple"),
        ("ɔberɛ", "orange"),
        ("anona", "sugar apple"),
        ("kwadu", "banana"),
        ("papae", "pawpaw"),
        ("mango", "mango"),
    ],

    "animals": [
        ("ɔkraman", "dog"),
        ("ɔkra", "cat"),
        ("akokɔ", "chicken"),
        ("nantwie", "cow"),
        ("apɔnkye", "goat"),
        ("odwan", "sheep"),
        ("ɔtorɔ", "pig"),
        ("ɔsono", "elephant"),
        ("gyata", "lion"),
        ("akorɔma", "hawk"),
        ("akroma", "eagle"),
        ("ɔkɔre", "parrot"),
        ("ɔwɔ", "snake"),
        ("ɔsebɔ", "leopard"),
        ("ɔdɔmmire", "lion"),
        ("ɔkoɔ", "tortoise"),
        ("akokɔsradeɛ", "chicken fat"),
        ("akyekyedeɛ", "spider"),
        ("aboa", "animal"),
        ("apɔnkye", "goat"),
        ("ɔtwe", "monkey"),
        ("ɔsono", "elephant"),
        ("ɔkɔtɔ", "crab"),
        ("apataa", "fish"),
        ("nantwie", "cow"),
    ],

    "nature": [
        ("owia", "sun"),
        ("ɔsram", "moon"),
        ("nsoroma", "star"),
        ("asase", "earth"),
        ("soro", "sky"),
        ("nsuo", "water"),
        ("mframa", "wind"),
        ("osu", "rain"),
        ("anyinam", "lightning"),
        ("aprannaa", "thunder"),
        ("ogya", "fire"),
        ("dua", "tree"),
        ("ɛpono", "door"),
        ("afifideɛ", "plant"),
        ("nhwiren", "flower"),
        ("ahaban", "leaf"),
        ("aba", "seed"),
        ("nkyene", "salt"),
        ("mmepɔ", "mountain"),
        ("subɔnten", "river"),
        ("po", "sea"),
        ("tare", "lake"),
        ("kwae", "forest"),
        ("anhwea", "sand"),
        ("ɔbo", "stone"),
    ],

    "places": [
        ("fie", "home"),
        ("sukuu", "school"),
        ("ayaresabea", "hospital"),
        ("asɔredan", "church"),
        ("gua", "market"),
        ("adidibea", "restaurant"),
        ("akwantuo", "journey"),
        ("kurow", "town"),
        ("ɔman", "country"),
        ("ahenkurow", "capital city"),
        ("polisifo", "police station"),
        ("fiase", "home"),
        ("adwuma", "workplace"),
        ("agoprama", "farm"),
        ("bank", "bank"),
        ("asɛnka dan", "church building"),
    ],

    "transport": [
        ("kar", "car"),
        ("tro-tro", "minibus"),
        ("ɔhyɛ", "vehicle"),
        ("bɔs", "bus"),
        ("keteke", "train"),
        ("wimhyɛn", "airplane"),
        ("ahyɛn", "ship"),
        ("pɔnkɔ", "horse"),
        ("sakre", "bicycle"),
        ("moto", "motorcycle"),
        ("taxi", "taxi"),
        ("kwan", "road"),
        ("akwantuo", "journey"),
        ("akwantufo", "traveller"),
    ],

    "verbs": [
        ("di", "eat"),
        ("nom", "drink"),
        ("kɔ", "go"),
        ("ba", "come"),
        ("te", "sit"),
        ("gyina", "stand"),
        ("sua", "learn"),
        ("kyerɛ", "teach"),
        ("ka", "speak"),
        ("hwɛ", "look"),
        ("kenkan", "read"),
        ("kyerɛw", "write"),
        ("dwene", "think"),
        ("yɛ", "do"),
        ("ma", "give"),
        ("fa", "take"),
        ("to", "put"),
        ("tɔ", "buy"),
        ("tɔn", "sell"),
        ("dɔ", "love"),
        ("boa", "help"),
        ("tie", "hear"),
        ("te", "understand"),
        ("hu", "see"),
        ("frɛ", "call"),
        ("sɔre", "rise"),
        ("da", "sleep"),
        ("nante", "walk"),
        ("tu", "run"),
        ("sere", "laugh"),
        ("su", "weep"),
        ("bisa", "ask"),
        ("yi", "remove"),
        ("siesie", "prepare"),
        ("si", "build"),
    ],

    "adjectives": [
        ("pa", "good"),
        ("bɔne", "bad"),
        ("kɛse", "big"),
        ("ketewa", "small"),
        ("tentene", "long"),
        ("tia", "short"),
        ("fɛ", "beautiful"),
        ("yɛ den", "hard"),
        ("yɛ mmerɛw", "easy"),
        ("yɛ hyew", "hot"),
        ("yɛ nwini", "cold"),
        ("dɛ", "sweet"),
        ("yɛ nwini", "cool"),
        ("yɛ den", "strong"),
        ("yɛ mmerɛw", "soft"),
        ("tetew", "old"),
        ("foforo", "new"),
        ("ahoɔfɛ", "beautiful"),
        ("ahoɔden", "strong"),
        ("kwan so", "straight"),
    ],

    "emotions": [
        ("anigyeɛ", "joy"),
        ("awerɛhow", "sadness"),
        ("ɔdɔ", "love"),
        ("abufuo", "anger"),
        ("ehu", "fear"),
        ("anigye", "happiness"),
        ("awerɛho", "sorrow"),
        ("ahopopo", "worry"),
        ("ahosɛpɛ", "excitement"),
        ("aniwu", "shame"),
        ("ahantan", "pride"),
        ("ahometew", "surprise"),
        ("awerɛkyekye", "comfort"),
        ("ayamye", "compassion"),
    ],

    "education": [
        ("sukuu", "school"),
        ("osuani", "student"),
        ("ɔkyerɛkyerɛni", "teacher"),
        ("adesua", "lesson"),
        ("adesuafo", "learners"),
        ("nhoma", "book"),
        ("krataa", "paper"),
        ("kyerɛw", "write"),
        ("kenkan", "read"),
        ("nimdeɛ", "knowledge"),
        ("nyansa", "wisdom"),
        ("sɔhwɛ", "examination"),
        ("adwuma", "work"),
        ("adesua dan", "classroom"),
        ("akyerɛkyerɛ", "teaching"),
        ("sukuu panyin", "headteacher"),
        ("asɛm", "subject"),
        ("nkyerɛkyerɛ", "instruction"),
        ("nsɛmmisa", "questions"),
        ("mmuaeɛ", "answers"),
    ],

    "technology": [
        ("kɔmputa", "computer"),
        ("intanɛt", "internet"),
        ("telefon", "telephone"),
        ("ɛlɛktrɔnik", "electronic"),
        ("dijitaal", "digital"),
        ("sofwɛɛ", "software"),
        ("haadwɛɛ", "hardware"),
        ("nɛtwɛɛk", "network"),
        ("data", "data"),
        ("fael", "file"),
        ("program", "program"),
        ("website", "website"),
        ("app", "application"),
        ("password", "password"),
        ("email", "email"),
        ("keyboard", "keyboard"),
        ("mouse", "computer mouse"),
        ("screen", "screen"),
        ("server", "server"),
        ("database", "database"),
        ("kod", "code"),
        ("system", "system"),
    ],

    "health": [
        ("ayaresa", "health"),
        ("ayaresabea", "hospital"),
        ("oduruyɛfo", "doctor"),
        ("ɔyarefo", "patient"),
        ("aduro", "medicine"),
        ("ɔyare", "illness"),
        ("honam", "body"),
        ("mogya", "blood"),
        ("akoma", "heart"),
        ("ti", "head"),
        ("ani", "eye"),
        ("aso", "ear"),
        ("ano", "mouth"),
        ("nsa", "hand"),
        ("nan", "leg"),
        ("ɔhome", "breathing"),
        ("ahomegye", "rest"),
        ("adurodan", "pharmacy"),
        ("ayaresɛ", "disease"),
        ("ayaresabea", "clinic"),
    ],
}


# ============================================================
# RECORD BUILDER
# ============================================================

def build_record(
    index: int,
    category: str,
    akan: str,
    english: str,
):
    """Build one validated Akan vocabulary record."""

    return create_akan_record(
        record_id=f"AKAN-VOCAB-{index:04d}",
        akan_term=akan,
        english_term=english,
        category="vocabulary",
        subcategory=category,

        definition_akan=(
            f"{akan} yɛ Akan asɛmfua a ɛkyerɛ {english}."
        ),

        definition_english=(
            f"{akan} is an Akan vocabulary term associated "
            f"with the meaning '{english}'."
        ),

        explanation_akan=(
            f"Wɔde '{akan}' di dwuma wɔ Akan kasa mu "
            f"de kyerɛ {english}."
        ),

        examples_akan=[
            f"Me ka '{akan}'.",
            f"Wɔde '{akan}' di dwuma wɔ da biara asetena mu.",
        ],

        examples_english=[
            f"I use the word '{english}'.",
            f"The word '{english}' is used in everyday communication.",
        ],

        keywords_akan=[
            akan,
            f"Akan {akan}",
        ],

        keywords_english=[
            english,
            f"Akan word for {english}",
        ],

        question_patterns=[
            f"Dɛn ne {akan}?",
            f"{akan} kyerɛ dɛn?",
            f"Ɛdeɛn na {akan} kyerɛ?",
            f"What is {akan}?",
            f"What is the Akan word for {english}?",
            f"How do you say {english} in Akan?",
        ],
    )


# ============================================================
# GENERATOR
# ============================================================

def generate():
    """
    Generate all unique Akan vocabulary records.

    Duplicate Akan-English pairs are removed so the generator
    does not create artificial duplicates.
    """

    records = []
    seen = set()

    record_number = 1

    for category, words in WORD_BANKS.items():

        for akan, english in words:

            key = (
                akan.strip().lower(),
                english.strip().lower(),
            )

            if key in seen:
                continue

            seen.add(key)

            records.append(
                build_record(
                    index=record_number,
                    category=category,
                    akan=akan,
                    english=english,
                )
            )

            record_number += 1

    return records


# ============================================================
# EXPORTS
# ============================================================

__all__ = [
    "WORD_BANKS",
    "build_record",
    "generate",
]
