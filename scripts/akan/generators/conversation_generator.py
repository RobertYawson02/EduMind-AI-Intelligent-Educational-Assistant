"""
==============================================================
AKAN CONVERSATION GENERATOR
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

CONVERSATIONS = [

("Maakye","Good morning","greeting","Greeting used in the morning."),

("Maaha","Good afternoon","greeting","Greeting used in the afternoon."),

("Maadwo","Good evening","greeting","Greeting used in the evening."),

("Wo ho te sɛn?","How are you?","wellbeing","Asking about someone's wellbeing."),

("Me ho yɛ","I am fine","wellbeing","Responding to a wellbeing question."),

("Mepa wo kyɛw","Please","politeness","Polite request."),

("Medaase","Thank you","politeness","Expression of gratitude."),

("Kosɛ","You're welcome","politeness","Reply after thanks."),

("Yiw","Yes","response","Affirmative response."),

("Daabi","No","response","Negative response."),
]

def generate():
    records=[]
    for i,(akan,english,subcategory,meaning) in enumerate(CONVERSATIONS,1):
        records.append(
            create_akan_record(
                record_id=f"AKAN-CONV-{i:05d}",
                akan_term=akan,
                english_term=english,
                category="conversation",
                subcategory=subcategory,
                definition_akan=meaning,
                definition_english=meaning,
                explanation_akan=f"Wɔde '{akan}' di dwuma wɔ nkɔmmɔ mu.",
                examples_akan=[akan],
                examples_english=[english],
                keywords_akan=[akan],
                keywords_english=[english],
                question_patterns=[f"Dɛn kyerɛ '{akan}'?"]
            )
        )
    return records