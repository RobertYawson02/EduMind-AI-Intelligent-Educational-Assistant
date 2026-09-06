"""
==============================================================
AKAN PROVERB GENERATOR
Version 1.0
==============================================================

Generates structured Akan proverb knowledge.

Each proverb contains:
- Akan proverb
- Literal meaning
- Deeper meaning
- English interpretation
- Context
- Usage
- Keywords
- Question patterns
"""

from __future__ import annotations

import importlib.util
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
AKAN_DIR = os.path.dirname(CURRENT_DIR)
SCHEMA_FILE = os.path.join(AKAN_DIR, "data", "akan_schema.py")

spec = importlib.util.spec_from_file_location(
    "akan_schema_runtime",
    SCHEMA_FILE
)

module = importlib.util.module_from_spec(spec)
sys.modules["akan_schema_runtime"] = module
spec.loader.exec_module(module)

create_akan_record = module.create_akan_record

# ============================================================
# AUTHENTIC AKAN PROVERBS
# ============================================================

PROVERBS = [

    {
        "akan":"Obi nnim obrempon ahyease.",
        "english":"Nobody knows the beginning of a great person.",
        "literal":"No one knows where greatness begins.",
        "meaning":"Do not despise humble beginnings.",
        "context":"Encouragement",
        "lesson":"Greatness often starts small."
    },

    {
        "akan":"Tikoro nko agyina.",
        "english":"One head does not hold council.",
        "literal":"A single head cannot make every decision.",
        "meaning":"Wisdom grows through consultation.",
        "context":"Leadership",
        "lesson":"Seek advice from others."
    },

    {
        "akan":"Anoma antu a, ɔbɔ da.",
        "english":"If a bird does not fly, it sleeps.",
        "literal":"Without effort there is no progress.",
        "meaning":"Action is necessary.",
        "context":"Motivation",
        "lesson":"Work leads to results."
    },

    {
        "akan":"Nsa baako nkura adesoa.",
        "english":"One hand cannot carry a load.",
        "literal":"One hand cannot lift a heavy burden.",
        "meaning":"Cooperation is important.",
        "context":"Teamwork",
        "lesson":"Work together."
    },

    {
        "akan":"Se wo werɛ fi na wosan kɔfa a, yɛnka sɛ wo ayera.",
        "english":"Returning for what you forgot is not being lost.",
        "literal":"Going back is not failure.",
        "meaning":"Correcting mistakes is wisdom.",
        "context":"Learning",
        "lesson":"Never fear starting again."
    }

]

# ============================================================
# GENERATOR
# ============================================================

def generate():

    records=[]

    for i, proverb in enumerate(PROVERBS, start=1):

        records.append(

            create_akan_record(

                record_id=f"AKAN-PROV-{i:05d}",

                akan_term=proverb["akan"],

                english_term=proverb["english"],

                category="proverbs",

                subcategory=proverb["context"],

                definition_akan=proverb["literal"],

                definition_english=proverb["literal"],

                explanation_akan=(
                    f"Mmɛ yi kyerɛ sɛ {proverb['meaning']}."
                ),

                examples_akan=[
                    proverb["akan"],
                    f"Wobetumi de mmɛ yi adi dwuma wɔ {proverb['context']} mu."
                ],

                examples_english=[
                    proverb["english"],
                    f"This proverb is commonly used in {proverb['context']} situations."
                ],

                keywords_akan=[
                    proverb["akan"],
                    "mmɛ",
                    proverb["context"]
                ],

                keywords_english=[
                    "Akan proverb",
                    proverb["context"],
                    proverb["lesson"]
                ],

                question_patterns=[
                    f"Dɛn na '{proverb['akan']}' kyerɛ?",
                    f"Dɛn ne mmɛ '{proverb['akan']}' ase?",
                    f"When is '{proverb['english']}' used?"
                ]

            )

        )

    return records

__all__=["generate"]