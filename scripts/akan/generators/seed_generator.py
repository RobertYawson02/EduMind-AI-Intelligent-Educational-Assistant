"""
==============================================================
AKAN SEED KNOWLEDGE GENERATOR
Version 1.2
==============================================================

Purpose:
    Generate high-quality foundational Akan knowledge records.

This is NOT a translation-only dataset.

The seed layer provides foundational knowledge for:

    - vocabulary
    - meanings
    - everyday concepts
    - family and society
    - education
    - health
    - nature
    - food
    - work
    - technology
    - emotions
    - conversation
    - general knowledge
    - Akan contextual understanding

The large-scale vocabulary and subject-specific knowledge will
be handled by dedicated generators.

==============================================================
"""

from __future__ import annotations

import importlib.util
import os
import sys


# ============================================================
# PATH CONFIGURATION
# ============================================================

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

AKAN_DIR = os.path.dirname(CURRENT_DIR)

DATA_DIR = os.path.join(
    AKAN_DIR,
    "data"
)

SCHEMA_FILE = os.path.join(
    DATA_DIR,
    "akan_schema.py"
)


# ============================================================
# LOAD SCHEMA
# ============================================================

def _load_schema():
    """
    Load akan_schema.py directly from its filesystem path.
    """

    if not os.path.isfile(SCHEMA_FILE):
        raise FileNotFoundError(
            "Akan schema file was not found:\n"
            f"{SCHEMA_FILE}"
        )

    spec = importlib.util.spec_from_file_location(
        "akan_schema_runtime",
        SCHEMA_FILE
    )

    if spec is None or spec.loader is None:
        raise ImportError(
            f"Could not load Akan schema: {SCHEMA_FILE}"
        )

    module = importlib.util.module_from_spec(spec)

    sys.modules["akan_schema_runtime"] = module

    spec.loader.exec_module(module)

    return module


_SCHEMA = _load_schema()

create_akan_record = _SCHEMA.create_akan_record


# ============================================================
# FOUNDATION RECORD BUILDER
# ============================================================

def make_item(
    akan_term: str,
    english_term: str,
    subcategory: str,
    definition_akan: str,
    definition_english: str,
    explanation_akan: str,
    examples_akan: list[str],
    examples_english: list[str],
    keywords_akan: list[str],
    keywords_english: list[str],
    question_patterns: list[str],
    category: str = "foundational_knowledge",
):
    """
    Store one foundational Akan concept.
    """

    return {
        "akan_term": akan_term,
        "english_term": english_term,
        "subcategory": subcategory,
        "definition_akan": definition_akan,
        "definition_english": definition_english,
        "explanation_akan": explanation_akan,
        "examples_akan": examples_akan,
        "examples_english": examples_english,
        "keywords_akan": keywords_akan,
        "keywords_english": keywords_english,
        "question_patterns": question_patterns,
        "category": category,
    }


# ============================================================
# FOUNDATIONAL AKAN KNOWLEDGE
# ============================================================

FOUNDATION = [

    # --------------------------------------------------------
    # BASIC CONCEPTS
    # --------------------------------------------------------

    make_item(
        "nsuo",
        "water",
        "basic vocabulary",
        "Nsuo yɛ adeɛ a nnipa, mmoa ne afifideɛ hia na wɔatena ase.",
        "Water is a substance required by humans, animals, and plants for life.",
        "Nsuo ho hia paa ma nkwa. Yɛde nsuo nom, noa aduane, hohoro yɛn ho na yɛma afifideɛ nyin.",
        [
            "Me pɛ nsuo.",
            "Afifideɛ hia nsuo na anyin.",
        ],
        [
            "I want water.",
            "Plants need water to grow.",
        ],
        ["nsuo", "nsu", "nsuo ase"],
        ["water", "drinking water"],
        [
            "Dɛn ne nsuo?",
            "Dɛn nti na nsuo ho hia?",
            "Yɛde nsuo yɛ dɛn?",
            "What is water?",
        ],
        "vocabulary",
    ),

    make_item(
        "ogya",
        "fire",
        "basic vocabulary",
        "Ogya yɛ hyew a ɛtumi hyew nneɛma.",
        "Fire is a source of heat that can burn materials.",
        "Ogya tumi ma yɛnya ɔhyew na wɔde noa aduane. Nanso ɛsɛ sɛ yɛhwɛ so yie efisɛ ogya tumi sɛe nneɛma.",
        [
            "Ogya no yɛ hyew.",
            "Yɛde ogya noa aduane.",
        ],
        [
            "The fire is hot.",
            "We use fire to cook food.",
        ],
        ["ogya", "ogya no", "ɔhyew"],
        ["fire", "heat", "flame"],
        [
            "Dɛn ne ogya?",
            "Yɛde ogya yɛ dɛn?",
            "Dɛn nti na ogya yɛ hu?",
            "What is fire?",
        ],
        "vocabulary",
    ),

    make_item(
        "asase",
        "land",
        "nature",
        "Asase yɛ ɔkwan anaa beaeɛ a nnipa, mmoa ne afifideɛ te anaa nyin so.",
        "Land is the solid ground or area on which people, animals, and plants live or grow.",
        "Asase ho hia ma kuayɛ, adan sie, nnipa asetena ne nneɛma pii a yɛyɛ wɔ asetena mu.",
        [
            "Yɛdua afifideɛ wɔ asase mu.",
            "Nnipa te asase so.",
        ],
        [
            "We plant crops in the soil.",
            "People live on land.",
        ],
        ["asase", "asase no", "asase mu"],
        ["land", "ground", "soil"],
        [
            "Dɛn ne asase?",
            "Asase ho hia sɛn?",
            "Yɛde asase yɛ dɛn?",
            "What is land?",
        ],
        "general_knowledge",
    ),

    make_item(
        "wia",
        "sky",
        "nature",
        "Wia yɛ ɔsoro fã a yɛhu no fi asase so.",
        "The sky is the region above the earth that we see from the ground.",
        "Wia yɛ beaeɛ a yɛhu owia, ɔsram ne nsoromma wɔ bere ahodoɔ mu.",
        [
            "Owia wɔ wia mu.",
            "Nsoromma pue wɔ wia mu anadwo.",
        ],
        [
            "The sun is in the sky.",
            "Stars appear in the sky at night.",
        ],
        ["wia", "ɔsoro", "wia mu"],
        ["sky", "heavens"],
        [
            "Dɛn ne wia?",
            "Dɛn na yɛhu wɔ wia mu?",
            "What is the sky?",
        ],
        "general_knowledge",
    ),

    # --------------------------------------------------------
    # FAMILY AND SOCIETY
    # --------------------------------------------------------

    make_item(
        "abusua",
        "family",
        "family",
        "Abusua yɛ nnipa a wɔnam mogya, awareɛ anaa abusua mu ntam ayɔnkofa so wɔ abusuabɔ.",
        "A family is a group of people connected through kinship, marriage, or family relationships.",
        "Abusua yɛ asetena mu fapem. Ɛboa ma wɔhwɛ mmofra, kyɛ asɛyɛdeɛ na wɔde amammerɛ kɔ awoɔ ntoatoasoɔ so.",
        [
            "Yɛn abusua bom yɛ aduane.",
            "Abusua boa wɔn ho wɔ mmereɛ a ɛyɛ den.",
        ],
        [
            "Our family eats together.",
            "Families support one another during difficult times.",
        ],
        ["abusua", "abusuafoɔ", "abusua mu"],
        ["family", "relatives", "kinship"],
        [
            "Dɛn ne abusua?",
            "Dɛn nti na abusua ho hia?",
            "What is a family?",
        ],
        "society",
    ),

    make_item(
        "ɛna",
        "mother",
        "family",
        "Ɛna yɛ ɔbea a ɔwoo obi.",
        "A mother is a woman who gives birth to a person.",
        "Ɛna yɛ abusua mu nipa a ɔtaa hwɛ ne mma, ma wɔn akwankyerɛ na ɔboa wɔn wɔ asetena mu.",
        [
            "Me ɛna wɔ fie.",
            "Ɛna hwɛ ne mma.",
        ],
        [
            "My mother is at home.",
            "A mother takes care of her children.",
        ],
        ["ɛna", "maame", "ɛna no"],
        ["mother", "mom", "mummy"],
        [
            "Hena ne ɛna?",
            "Ɛna yɛ hena?",
            "Who is a mother?",
        ],
        "family",
    ),

    make_item(
        "agya",
        "father",
        "family",
        "Agya yɛ ɔbarima a ɔwoo obi anaa ɔyɛ obi papa wɔ abusua mu.",
        "A father is a man who fathers a person or serves as a male parent in a family.",
        "Agya yɛ abusua mu ɔwofoɔ a ɔtumi boa ma mmofra nya akwankyerɛ, hwɛ wɔn na ɔma wɔn mmoa.",
        [
            "Me agya reyɛ adwuma.",
            "Agya ne ne mma kasa.",
        ],
        [
            "My father is working.",
            "The father talks with his children.",
        ],
        ["agya", "papa", "agya no"],
        ["father", "dad", "parent"],
        [
            "Hena ne agya?",
            "Agya yɛ hena?",
            "Who is a father?",
        ],
        "family",
    ),

    make_item(
        "ɔman",
        "country",
        "society",
        "Ɔman yɛ asase ne nnipa a wɔte saa asase no so na wɔwɔ aban ne nhyehyɛeɛ.",
        "A country is a territory and population organized under a government.",
        "Ɔman wɔ nnipa, asase, aban, mmara ne ahyeɛ a ɛma wɔhyehyɛ ɔman no asetena.",
        [
            "Ghana yɛ ɔman wɔ Afrika.",
            "Ɔman biara wɔ ne mmara.",
        ],
        [
            "Ghana is a country in Africa.",
            "Every country has its laws.",
        ],
        ["ɔman", "aman", "ɔman no"],
        ["country", "nation", "state"],
        [
            "Dɛn ne ɔman?",
            "Ɔman yɛ dɛn?",
            "What is a country?",
        ],
        "society",
    ),

    make_item(
        "ɔmanfoɔ",
        "citizens",
        "society",
        "Ɔmanfoɔ yɛ nnipa a wɔyɛ ɔman bi mufoɔ.",
        "Citizens are members of a particular country.",
        "Ɔmanfoɔ wɔ hokwan ne asɛyɛdeɛ wɔ ɔman no mu na ɛsɛ sɛ wɔdi mmara so.",
        [
            "Ɔmanfoɔ di ɔman no mmara so.",
            "Ɔmanfoɔ wɔ asɛyɛdeɛ wɔ ɔman no mu.",
        ],
        [
            "Citizens obey the laws of the country.",
            "Citizens have responsibilities in their country.",
        ],
        ["ɔmanfoɔ", "ɔman muni", "amanfoɔ"],
        ["citizens", "citizen", "people of a country"],
        [
            "Hena ne ɔmanfoɔ?",
            "Dɛn ne ɔmanfoɔ asɛyɛdeɛ?",
            "Who are citizens?",
        ],
        "society",
    ),

    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    make_item(
        "adesua",
        "education",
        "education",
        "Adesua yɛ ɔkwan a obi fa so nya nimdeɛ, nteaseɛ ne ahokokwaw.",
        "Education is the process through which a person gains knowledge, understanding, and skills.",
        "Adesua betumi akɔ so wɔ sukuu, fie, adwumam anaa asetena mu. Ɛboa ma obi nya nimdeɛ ne ahokokwaw a ɛhia wɔ asetena mu.",
        [
            "Adesua ho hia ma mmofra.",
            "Sukuu yɛ baabi a yɛsua adeɛ.",
        ],
        [
            "Education is important for children.",
            "School is a place where we learn.",
        ],
        ["adesua", "sua adeɛ", "adesua mu"],
        ["education", "learning", "study"],
        [
            "Dɛn ne adesua?",
            "Dɛn nti na adesua ho hia?",
            "What is education?",
        ],
        "education",
    ),

    make_item(
        "sukuu",
        "school",
        "education",
        "Sukuu yɛ beaeɛ a wɔkyerɛkyerɛ na wɔsua adeɛ.",
        "A school is a place where teaching and learning take place.",
        "Sukuu boa asuafoɔ ma wɔnya nimdeɛ, ahokokwaw ne nkyerɛkyerɛ a ɛboa wɔn wɔ asetena mu.",
        [
            "Me kɔ sukuu da biara.",
            "Ɔkyerɛkyerɛ wɔ sukuu mu.",
        ],
        [
            "I go to school every day.",
            "He teaches at a school.",
        ],
        ["sukuu", "sukuu mu", "sua adeɛ"],
        ["school", "class", "learning institution"],
        [
            "Dɛn ne sukuu?",
            "Dɛn nti na yɛkɔ sukuu?",
            "What is a school?",
        ],
        "education",
    ),

    make_item(
        "ɔkyerɛkyerɛfoɔ",
        "teacher",
        "education",
        "Ɔkyerɛkyerɛfoɔ yɛ obi a ɔkyerɛkyerɛ nnipa adeɛ.",
        "A teacher is a person who teaches others.",
        "Ɔkyerɛkyerɛfoɔ boa asuafoɔ ma wɔte adeɛ ase, nya nimdeɛ na wɔde wɔn ahokokwaw di dwuma.",
        [
            "Ɔkyerɛkyerɛfoɔ no kyerɛkyerɛ akontaabu.",
            "Asuafoɔ tie ɔkyerɛkyerɛfoɔ no.",
        ],
        [
            "The teacher teaches mathematics.",
            "The students listen to the teacher.",
        ],
        ["ɔkyerɛkyerɛfoɔ", "kyerɛkyerɛfoɔ", "kyerɛkyerɛ"],
        ["teacher", "educator", "instructor"],
        [
            "Hena ne ɔkyerɛkyerɛfoɔ?",
            "Dɛn na ɔkyerɛkyerɛfoɔ yɛ?",
            "Who is a teacher?",
        ],
        "education",
    ),

    # --------------------------------------------------------
    # KNOWLEDGE AND THINKING
    # --------------------------------------------------------

    make_item(
        "nimdeɛ",
        "knowledge",
        "knowledge",
        "Nimdeɛ yɛ nsɛm, nokware, nteaseɛ ne nim a obi nya fa adeɛ anaa asɛm bi ho.",
        "Knowledge is information, facts, understanding, and awareness acquired about a subject or situation.",
        "Nimdeɛ betumi aba denam adesua, osuahunu, nhwehwɛmu, nsɛm a yɛtie ne nneɛma a yɛhu wɔ asetena mu.",
        [
            "Adesua boa ma yenya nimdeɛ.",
            "Nhwehwɛmu betumi ama yɛanya nimdeɛ foforɔ.",
        ],
        [
            "Education helps us gain knowledge.",
            "Research can give us new knowledge.",
        ],
        ["nimdeɛ", "nim", "nteaseɛ", "adesua"],
        ["knowledge", "understanding", "learning"],
        [
            "Dɛn ne nimdeɛ?",
            "Ɛhe na nimdeɛ firi ba?",
            "What is knowledge?",
        ],
        "knowledge",
    ),

    make_item(
        "adwene",
        "thought",
        "thinking",
        "Adwene yɛ nsusuiɛ anaa nteaseɛ a ɛba obi tirim.",
        "Thought is an idea, consideration, or mental process that occurs in a person's mind.",
        "Nnipa de adwene yɛ nhyehyɛeɛ, susu ɔhaw ho na wɔsi gyinaeɛ.",
        [
            "Ɔde ne adwene sii ɔhaw no so.",
            "Ɛsɛ sɛ yɛsusu ansa na yɛasi gyinaeɛ.",
        ],
        [
            "He focused his thought on the problem.",
            "We should think before making a decision.",
        ],
        ["adwene", "susuiɛ", "adwene mu"],
        ["thought", "thinking", "idea"],
        [
            "Dɛn ne adwene?",
            "Yɛde adwene yɛ dɛn?",
            "What is thought?",
        ],
        "knowledge",
    ),

    # --------------------------------------------------------
    # WORK AND ECONOMY
    # --------------------------------------------------------

    make_item(
        "adwuma",
        "work",
        "work",
        "Adwuma yɛ dwumadie anaa mmɔdenbɔ a obi yɛ de nya biribi anaa di botaeɛ bi ho dwuma.",
        "Work is an activity or effort performed to achieve a purpose or obtain a result.",
        "Adwuma betumi ayɛ honam fam adwuma, adwene mu adwuma, sukuu adwuma anaa adwuma a wɔyɛ de nya sika.",
        [
            "Ɔyɛ adwuma wɔ sukuu mu.",
            "Yɛyɛ adwuma denneennen sɛdeɛ yɛbɛdi botaeɛ ho dwuma.",
        ],
        [
            "He works at a school.",
            "We work hard to achieve our goal.",
        ],
        ["adwuma", "yɛ adwuma", "adwumayɛ"],
        ["work", "job", "activity"],
        [
            "Dɛn ne adwuma?",
            "Adwuma yɛ dɛn?",
            "What is work?",
        ],
        "work",
    ),

    make_item(
        "sika",
        "money",
        "economy",
        "Sika yɛ adeɛ a nnipa de tɔ nneɛma, tua ka na wɔyɛ aguadi.",
        "Money is a medium used to buy goods, pay for services, and conduct trade.",
        "Sika boa ma aguadi ne nsesa yɛ mmerɛ. Nnipa nya sika denam adwuma, aguadi ne akwan foforɔ so.",
        [
            "Me wɔ sika kakra.",
            "Yɛde sika tɔ aduane.",
        ],
        [
            "I have some money.",
            "We use money to buy food.",
        ],
        ["sika", "sika no", "sika yɛ"],
        ["money", "cash", "currency"],
        [
            "Dɛn ne sika?",
            "Yɛde sika yɛ dɛn?",
            "What is money?",
        ],
        "economy",
    ),

    # --------------------------------------------------------
    # HEALTH
    # --------------------------------------------------------

    make_item(
        "apɔmuden",
        "health",
        "health",
        "Apɔmuden yɛ tebea a obi nipadua ne n'adwene yɛ adwuma yie.",
        "Health is a state in which a person's body and mind function well.",
        "Apɔmuden hwehwɛ sɛ obi hwɛ ne nipadua, di aduane pa, nya ahomegyeɛ na ɔkwati nneɛma a ɛtumi ma no yareɛ.",
        [
            "Apɔmuden ho hia.",
            "Aduane pa boa apɔmuden.",
        ],
        [
            "Health is important.",
            "Good food supports health.",
        ],
        ["apɔmuden", "ɔyareɛ", "apɔm"],
        ["health", "wellness", "well-being"],
        [
            "Dɛn ne apɔmuden?",
            "Dɛn nti na apɔmuden ho hia?",
            "What is health?",
        ],
        "health",
    ),

    make_item(
        "ɔyareɛ",
        "disease",
        "health",
        "Ɔyareɛ yɛ tebea a ɛma nipadua anaa adwene ntumi nyɛ adwuma sɛnea ɛsɛ.",
        "A disease is a condition that affects the normal functioning of the body or mind.",
        "Ɔyareɛ bi tumi firi mmoawa, nkwa mu tebea, awosu anaa nneɛma foforɔ mu. Ɛho hia sɛ wɔhwehwɛ yareɛ no mu na wɔnya ayaresa a ɛfata.",
        [
            "Ɔyareɛ no maa no yɛɛ mmerɛ.",
            "Ɔkɔɔ ayaresabea sɛ wɔnhwɛ ne yareɛ.",
        ],
        [
            "The disease made him weak.",
            "He went to the hospital to have his illness examined.",
        ],
        ["ɔyareɛ", "yareɛ", "ɔyare"],
        ["disease", "illness", "sickness"],
        [
            "Dɛn ne ɔyareɛ?",
            "Dɛn na ɛtumi de ɔyareɛ ba?",
            "What is a disease?",
        ],
        "health",
    ),

    # --------------------------------------------------------
    # FOOD
    # --------------------------------------------------------

    make_item(
        "aduane",
        "food",
        "food",
        "Aduane yɛ nneɛma a nnipa di de nya ahoɔden ne aduanenoa mu mfasoɔ.",
        "Food consists of substances people eat to obtain energy and nutrients.",
        "Aduane ho hia ma nipadua nyin, ahoɔden ne apɔmuden. Aduane ahodoɔ ma nipadua nya nneɛma a ɛhia.",
        [
            "Me pɛ aduane.",
            "Aduane pa boa nipadua.",
        ],
        [
            "I want food.",
            "Good food supports the body.",
        ],
        ["aduane", "aduan", "aduane di"],
        ["food", "meal", "nutrition"],
        [
            "Dɛn ne aduane?",
            "Dɛn nti na aduane ho hia?",
            "What is food?",
        ],
        "food",
    ),

    make_item(
        "afifideɛ",
        "plants",
        "nature",
        "Afifideɛ yɛ nkwa nneɛma a wɔtaa nyin wɔ asase mu na wɔtumi yɛ wɔn ankasa aduane.",
        "Plants are living organisms that commonly grow in soil and can produce their own food.",
        "Afifideɛ ho hia ma nnipa ne mmoa efisɛ wɔma yɛnya aduane, oxygen, nnua ne nneɛma foforɔ.",
        [
            "Afifideɛ hia nsuo.",
            "Nnua yɛ afifideɛ.",
        ],
        [
            "Plants need water.",
            "Trees are plants.",
        ],
        ["afifideɛ", "afifide", "afifideɛ no"],
        ["plants", "vegetation", "crops"],
        [
            "Dɛn ne afifideɛ?",
            "Dɛn nti na afifideɛ ho hia?",
            "What are plants?",
        ],
        "nature",
    ),

    # --------------------------------------------------------
    # ANIMALS
    # --------------------------------------------------------

    make_item(
        "aboa",
        "animal",
        "animals",
        "Aboa yɛ nkwa adeɛ a ɛnyɛ nnipa na ɛtumi di, home, nyin na ɛwo.",
        "An animal is a living organism that is not a human and can feed, breathe, grow, and reproduce.",
        "Mmoa yɛ abɔdeɛ a wɔwɔ akwan ahodoɔ a wɔfa so tena ase. Nnipa de mmoa di dwuma wɔ aduane, kuayɛ ne nneɛma foforɔ mu.",
        [
            "Ɔkraman yɛ aboa.",
            "Mmoa hia aduane ne nsuo.",
        ],
        [
            "A dog is an animal.",
            "Animals need food and water.",
        ],
        ["aboa", "mmoa", "aboa no"],
        ["animal", "animals", "creature"],
        [
            "Dɛn ne aboa?",
            "Mmoa yɛ dɛn?",
            "What is an animal?",
        ],
        "animals",
    ),

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    make_item(
        "bere",
        "time",
        "time",
        "Bere yɛ adeɛ a yɛde kyerɛ sɛnea nsɛm si anaa ɛtwam.",
        "Time is a way of measuring when events occur and how they pass.",
        "Yɛde bere kyerɛ da, nnɔnhwere, simma ne mmere ahodoɔ. Bere boa ma yɛhyehyɛ yɛn dwumadie.",
        [
            "Bere no som bo.",
            "Ɛsɛ sɛ yɛde yɛn bere di dwuma yie.",
        ],
        [
            "Time is valuable.",
            "We should use our time well.",
        ],
        ["bere", "bere no", "mmere"],
        ["time", "period", "duration"],
        [
            "Dɛn ne bere?",
            "Dɛn nti na bere ho hia?",
            "What is time?",
        ],
        "time",
    ),

    make_item(
        "da",
        "day",
        "time",
        "Da yɛ bere a yɛde kyerɛ nnafua bi anaa nnɔnhwereɛ a ɛfata da baako.",
        "A day is a period used to refer to one calendar day or approximately one full cycle of daylight and night.",
        "Da yɛ bere a yɛde hyehyɛ yɛn asetena. Yɛwɔ nna ahodoɔ wɔ dapɛn mu.",
        [
            "Ɛnnɛ yɛ Memeneda.",
            "Da biara me kɔ sukuu.",
        ],
        [
            "Today is Saturday.",
            "I go to school every day.",
        ],
        ["da", "nnɛ", "da biara"],
        ["day", "today", "daily"],
        [
            "Dɛn ne da?",
            "Da biara yɛ dɛn?",
            "What is a day?",
        ],
        "time",
    ),

    # --------------------------------------------------------
    # EMOTIONS
    # --------------------------------------------------------

    make_item(
        "anigyeɛ",
        "happiness",
        "emotions",
        "Anigyeɛ yɛ nkateɛ a ɛma obi te nka sɛ n'ani agye na ne koma atɔ ne yam.",
        "Happiness is an emotional state in which a person feels pleased or joyful.",
        "Anigyeɛ betumi aba bere a obi nya adeɛ a ɔpɛ, di nkonim, nya abusuabɔ pa anaa osuahu a ɛyɛ anigyeɛ.",
        [
            "N'ani gyeeɛ paa.",
            "Nkonimdie no maa no anigyeɛ.",
        ],
        [
            "He was very happy.",
            "The victory made him happy.",
        ],
        ["anigyeɛ", "ani gye", "anigye"],
        ["happiness", "joy", "gladness"],
        [
            "Dɛn ne anigyeɛ?",
            "Dɛn na ɛtumi ma obi ani gye?",
            "What is happiness?",
        ],
        "emotions",
    ),

    make_item(
        "awerɛhoɔ",
        "sadness",
        "emotions",
        "Awerɛhoɔ yɛ nkateɛ a ɛma obi te yaw anaa anigyeɛ a ɛnni ne mu.",
        "Sadness is an emotional state involving sorrow or a lack of happiness.",
        "Awerɛhoɔ tumi ba bere a obi hwere obi, nnya nea ɔhwɛ kwan, anaa ɔfa osuahu a ɛyɛ den mu.",
        [
            "Asɛm no maa no awerɛhoɔ.",
            "Ɔwɔ awerɛhoɔ wɔ ne koma mu.",
        ],
        [
            "The situation made him sad.",
            "He has sadness in his heart.",
        ],
        ["awerɛhoɔ", "awerehow", "awerɛhow"],
        ["sadness", "sorrow", "grief"],
        [
            "Dɛn ne awerɛhoɔ?",
            "Dɛn na ɛtumi de awerɛhoɔ ba?",
            "What is sadness?",
        ],
        "emotions",
    ),

    # --------------------------------------------------------
    # TECHNOLOGY
    # --------------------------------------------------------

    make_item(
        "mfiridwuma",
        "technology",
        "technology",
        "Mfiridwuma yɛ nimdeɛ ne akwan a nnipa de nneɛma ne mfiri yɛ adwuma anaa siesie ɔhaw.",
        "Technology is the knowledge, methods, and tools people use to perform tasks and solve problems.",
        "Mfiridwuma ka kɔmputa, telefon, intanɛt, mfiri ne akwan ahodoɔ a ɛboa nnipa wɔ asetena ne adwuma mu.",
        [
            "Telefon yɛ mfiridwuma.",
            "Mfiridwuma ama nkitahodie ayɛ mmerɛ.",
        ],
        [
            "A telephone is technology.",
            "Technology has made communication easier.",
        ],
        ["mfiridwuma", "mfiridwuma ho", "mfiri"],
        ["technology", "technologies", "tools"],
        [
            "Dɛn ne mfiridwuma?",
            "Mfiridwuma boa yɛn sɛn?",
            "What is technology?",
        ],
        "technology",
    ),

    make_item(
        "kɔmputa",
        "computer",
        "technology",
        "Kɔmputa yɛ ɛlɛtrɔnik mfiri a ɛtumi gye nsɛm, yɛ ho adwuma, sie no na ɛyi nsɛm a wɔayɛ ho adwuma.",
        "A computer is an electronic device that can receive, process, store, and produce information.",
        "Kɔmputa yɛ adwuma wɔ adesua, aguadi, nhwehwɛmu, nkitahodie ne mfiridwuma mu.",
        [
            "Mede kɔmputa yɛ me sukuu adwuma.",
            "Kɔmputa tumi sie nsɛm.",
        ],
        [
            "I use a computer for my school work.",
            "A computer can store information.",
        ],
        ["kɔmputa", "computer", "kɔmputa no"],
        ["computer", "PC", "computing"],
        [
            "Dɛn ne kɔmputa?",
            "Kɔmputa yɛ dɛn?",
            "What is a computer?",
        ],
        "technology",
    ),

    # --------------------------------------------------------
    # COMMUNICATION
    # --------------------------------------------------------

    make_item(
        "nkitahodie",
        "communication",
        "communication",
        "Nkitahodie yɛ ɔkwan a nnipa fa so de nsɛm anaa adwene kɔ obi foforɔ nkyɛn.",
        "Communication is the process of sharing information or ideas with another person or group.",
        "Nkitahodie betumi ayɛ kasa, nwoma, telefon, nsɛnkyerɛnne anaa intanɛt so nkitahodie.",
        [
            "Kasa yɛ nkitahodie kwan.",
            "Telefon boa ma yɛkasa wɔ akyirikyiri.",
        ],
        [
            "Speech is a form of communication.",
            "Telephones help us communicate over distance.",
        ],
        ["nkitahodie", "kasa", "nkitahodie kwan"],
        ["communication", "interaction", "contact"],
        [
            "Dɛn ne nkitahodie?",
            "Yɛyɛ nkitahodie sɛn?",
            "What is communication?",
        ],
        "communication",
    ),

    # --------------------------------------------------------
    # BASIC ACTIONS
    # --------------------------------------------------------

    make_item(
        "nom",
        "drink",
        "actions",
        "Nom yɛ sɛ obi de nsuo anaa nsã a wɔtumi nom kɔ ne anom.",
        "To drink means to take a liquid into the mouth and swallow it.",
        "Nnipa nom nsuo, nufusu ne anonneɛ ahodoɔ. Nsuo nom yɛ adeɛ a ɛho hia ma nipadua.",
        [
            "Me nom nsuo.",
            "Mmofra no nom nufusu.",
        ],
        [
            "I drink water.",
            "The children drink milk.",
        ],
        ["nom", "nom nsuo", "nom adeɛ"],
        ["drink", "drinking"],
        [
            "Nom yɛ dɛn?",
            "Dɛn na yɛtumi nom?",
            "What does drink mean?",
        ],
        "actions",
    ),

    make_item(
        "di",
        "eat",
        "actions",
        "Di yɛ sɛ obi de aduane kɔ n'anom na ɔwe.",
        "To eat means to take food into the mouth and consume it.",
        "Nnipa di aduane de nya ahoɔden ne aduanenoa mu nneɛma a nipadua hia.",
        [
            "Me di aduane.",
            "Yɛdi nkɔmmɔ bere a yɛredidi.",
        ],
        [
            "I eat food.",
            "We talk while eating.",
        ],
        ["di", "redidi", "aduane di"],
        ["eat", "eating", "consume"],
        [
            "Di yɛ dɛn?",
            "Dɛn nti na yɛdi aduane?",
            "What does eat mean?",
        ],
        "actions",
    ),

    make_item(
        "kɔ",
        "go",
        "actions",
        "Kɔ yɛ sɛ obi tu firi beaeɛ baako kɔ beaeɛ foforɔ.",
        "To go means to move from one place to another.",
        "Kɔ yɛ adeɛ a nnipa yɛ daa de kɔ sukuu, adwuma, fie anaa baabi foforɔ.",
        [
            "Me kɔ sukuu.",
            "Ɔkɔ fie.",
        ],
        [
            "I go to school.",
            "He goes home.",
        ],
        ["kɔ", "rekɔ", "kɔ baabi"],
        ["go", "going", "move"],
        [
            "Kɔ yɛ dɛn?",
            "Ɔkwan bɛn so na yɛkɔ baabi?",
            "What does go mean?",
        ],
        "actions",
    ),

    # --------------------------------------------------------
    # VALUES
    # --------------------------------------------------------

    make_item(
        "nokware",
        "truth",
        "values",
        "Nokware yɛ asɛm anaa tebea a ɛne nea ɛyɛ nokorɛ hyia.",
        "Truth is a statement or condition that corresponds with what is real or correct.",
        "Nokware ho hia wɔ nkitahodie ne abusuabɔ mu efisɛ ɛma nnipa nya ahotosoɔ wɔ wɔn ho.",
        [
            "Ɛsɛ sɛ yɛka nokware.",
            "Nokware ma ahotosoɔ yɛ den.",
        ],
        [
            "We should tell the truth.",
            "Truth strengthens trust.",
        ],
        ["nokware", "nokorɛ", "ka nokware"],
        ["truth", "honesty", "true"],
        [
            "Dɛn ne nokware?",
            "Dɛn nti na nokware ho hia?",
            "What is truth?",
        ],
        "values",
    ),

    make_item(
        "ɔdɔ",
        "love",
        "emotions and values",
        "Ɔdɔ yɛ nkateɛ a ɛma obi nya ayamye, anigyeɛ ne ɔpɛ sɛ ɔboa anaa ɔhwɛ obi.",
        "Love is an emotional bond involving care, affection, goodwill, or concern for another.",
        "Ɔdɔ betumi ada ne ho adi wɔ abusua, adamfoɔ, ɔman ne nnipa ntam wɔ akwan ahodoɔ so.",
        [
            "Ɔdɔ ma nnipa boa wɔn ho.",
            "Abusua mu ɔdɔ ho hia.",
        ],
        [
            "Love makes people support one another.",
            "Love within a family is important.",
        ],
        ["ɔdɔ", "dɔ", "ɔdɔ mu"],
        ["love", "care", "affection"],
        [
            "Dɛn ne ɔdɔ?",
            "Ɔdɔ da adi sɛn?",
            "What is love?",
        ],
        "values",
    ),

]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """
    Generate all foundational Akan records.
    """

    records = []

    for number, item in enumerate(
        FOUNDATION,
        start=1
    ):

        record = create_akan_record(
            record_id=f"AKAN-SEED-{number:04d}",

            akan_term=item["akan_term"],

            english_term=item["english_term"],

            category=item["category"],

            subcategory=item["subcategory"],

            definition_akan=item["definition_akan"],

            definition_english=item["definition_english"],

            explanation_akan=item["explanation_akan"],

            examples_akan=item["examples_akan"],

            examples_english=item["examples_english"],

            keywords_akan=item["keywords_akan"],

            keywords_english=item["keywords_english"],

            question_patterns=item["question_patterns"],
        )

        records.append(record)

    return records


# ============================================================
# PUBLIC API
# ============================================================

__all__ = [
    "generate"
]