"""
==============================================================
AKAN SCIENCE GENERATOR
Version 1.0
==============================================================

Purpose:
    Generate structured science knowledge in Akan.

Coverage:
    - Biology
    - Physics
    - Chemistry
    - Earth Science
    - Human Body
    - Scientific Method

This is designed for explanation-first learning.
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

SCIENCE = [

    {
        "akan_term":"Nyansapɛ",
        "english_term":"Science",
        "subcategory":"general science",
        "definition_akan":"Nyansapɛ yɛ nhwehwɛmu a ɛhwehwɛ sɛnea wiase ne nneɛma a ɛwɔ mu yɛ adwuma.",
        "definition_english":"Science is the systematic study of the natural world through observation and evidence."
    },

    {
        "akan_term":"Ahomegyeɛ",
        "english_term":"Energy",
        "subcategory":"physics",
        "definition_akan":"Ahomegyeɛ yɛ tumi a ɛma adeɛ tumi yɛ adwuma anaa sesa.",
        "definition_english":"Energy is the ability to do work or cause change."
    },

    {
        "akan_term":"Tumi",
        "english_term":"Force",
        "subcategory":"physics",
        "definition_akan":"Tumi yɛ adeɛ a ɛtumi twe anaa pia adeɛ.",
        "definition_english":"Force is a push or pull acting on an object."
    },

    {
        "akan_term":"Nkwa mu nneɛma",
        "english_term":"Living things",
        "subcategory":"biology",
        "definition_akan":"Nkwa mu nneɛma yɛ nneɛma a wɔwo, nyin, home na wɔsan wu.",
        "definition_english":"Living things grow, reproduce, breathe, and eventually die."
    },

    {
        "akan_term":"Afifideɛ",
        "english_term":"Plants",
        "subcategory":"biology",
        "definition_akan":"Afifideɛ yɛ nkwa mu nneɛma a wɔyɛ wɔn aduan denam owia hann so.",
        "definition_english":"Plants make their own food using sunlight."
    },

    {
        "akan_term":"Mmoa",
        "english_term":"Animals",
        "subcategory":"biology",
        "definition_akan":"Mmoa yɛ nkwa mu nneɛma a wɔnya wɔn aduan fi nneɛma foforɔ.",
        "definition_english":"Animals obtain food from other organisms."
    },

    {
        "akan_term":"Nsuo",
        "english_term":"Water",
        "subcategory":"chemistry",
        "definition_akan":"Nsuo ho hia ma nkwa nyinaa.",
        "definition_english":"Water is essential for all life."
    },

    {
        "akan_term":"Mframa",
        "english_term":"Air",
        "subcategory":"earth science",
        "definition_akan":"Mframa yɛ gas ahodoɔ a atwa asase ho ahyia.",
        "definition_english":"Air is a mixture of gases surrounding the Earth."
    },

    {
        "akan_term":"Owia",
        "english_term":"Sun",
        "subcategory":"earth science",
        "definition_akan":"Owia ma hann ne ahomegyeɛ ma asase.",
        "definition_english":"The Sun provides light and energy to Earth."
    },

    {
        "akan_term":"Asase",
        "english_term":"Earth",
        "subcategory":"earth science",
        "definition_akan":"Asase yɛ planet a yɛte so.",
        "definition_english":"Earth is the planet where humans live."
    },

    {
        "akan_term":"Nipadua",
        "english_term":"Human body",
        "subcategory":"human biology",
        "definition_akan":"Nipadua yɛ nipa no honam ne ne nhyehyɛeɛ nyinaa.",
        "definition_english":"The human body consists of interconnected organs and systems."
    },

    {
        "akan_term":"Akoma",
        "english_term":"Heart",
        "subcategory":"human biology",
        "definition_akan":"Akoma pue mogya kɔ nipadua nyinaa mu.",
        "definition_english":"The heart pumps blood throughout the body."
    },

    {
        "akan_term":"Ahomegyeɛ nhwehwɛmu",
        "english_term":"Scientific method",
        "subcategory":"scientific method",
        "definition_akan":"Nyansapɛ mu nhwehwɛmu fa nsɛmmisa, nhwehwɛmu, sɔhwɛ ne adanseɛ so.",
        "definition_english":"The scientific method involves asking questions, investigating, experimenting, and evaluating evidence."
    }

]

def build_record(item, number):

    return create_akan_record(

        record_id=f"AKAN-SCI-{number:05d}",

        akan_term=item["akan_term"],

        english_term=item["english_term"],

        category="science",

        subcategory=item["subcategory"],

        definition_akan=item["definition_akan"],

        definition_english=item["definition_english"],

        explanation_akan=(
            f"{item['akan_term']} yɛ nyansapɛ mu adwene titire a ɛboa ma yɛte wiase ase."
        ),

        examples_akan=[
            f"Wɔde {item['akan_term']} di dwuma wɔ nyansapɛ mu."
        ],

        examples_english=[
            f"{item['english_term']} is studied in science."
        ],

        keywords_akan=[
            item["akan_term"],
            "nyansapɛ",
            item["subcategory"]
        ],

        keywords_english=[
            item["english_term"],
            "science",
            item["subcategory"]
        ],

        question_patterns=[
            f"Dɛn ne {item['akan_term']}?",
            f"{item['akan_term']} kyerɛ sɛn?",
            f"What is {item['english_term']}?"
        ]
    )

def generate():

    records=[]

    for i,item in enumerate(SCIENCE,1):

        records.append(
            build_record(item,i)
        )

    return records

__all__=["generate"]