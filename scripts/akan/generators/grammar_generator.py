"""
==============================================================
AKAN GRAMMAR GENERATOR
==============================================================
"""

from __future__ import annotations
import importlib.util
import os
import sys

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
AKAN_DIR=os.path.dirname(CURRENT_DIR)
SCHEMA_FILE=os.path.join(AKAN_DIR,"data","akan_schema.py")

spec=importlib.util.spec_from_file_location("akan_schema_runtime",SCHEMA_FILE)
module=importlib.util.module_from_spec(spec)
sys.modules["akan_schema_runtime"]=module
spec.loader.exec_module(module)

create_akan_record=module.create_akan_record

GRAMMAR = [
    ("Me","I","pronoun"),
    ("Wo","You","pronoun"),
    ("Ɔ","He/She","pronoun"),
    ("Yɛn","We","pronoun"),
    ("Moma","You (plural)","pronoun"),
    ("Wɔn","They","pronoun"),
    ("Dɛn","What","question word"),
    ("Hena","Who","question word"),
    ("Ɛhe","Where","question word"),
    ("Bere bɛn","When","question word"),
    ("Dɛn nti na","Why","question pattern"),
    ("Ɔkwan bɛn so","How","question pattern"),
]

def generate():
    records=[]
    for i,(akan,english,subcategory) in enumerate(GRAMMAR,1):
        records.append(
            create_akan_record(
                record_id=f"AKAN-GRAM-{i:05d}",
                akan_term=akan,
                english_term=english,
                category="grammar",
                subcategory=subcategory,
                definition_akan=f"{akan} yɛ {subcategory}.",
                definition_english=f"{english} is a {subcategory}.",
                explanation_akan=f"Wɔde '{akan}' di dwuma wɔ Akan kasa mu.",
                examples_akan=[f"{akan} yɛ nhwɛsoɔ."],
                examples_english=[f"{english} is an example."],
                keywords_akan=[akan],
                keywords_english=[english],
                question_patterns=[f"Dɛn ne {akan}?"]
            )
        )
    return records