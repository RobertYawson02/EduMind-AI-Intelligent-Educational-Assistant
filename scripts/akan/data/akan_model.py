"""
==============================================================
AKAN KNOWLEDGE SEED DATA
Version 1.0
==============================================================

Purpose:
    Initial structured Akan knowledge dataset.

Important:
    This is NOT a translation-only dataset.

    Records are designed to support:
        - vocabulary
        - meanings
        - questions
        - explanations
        - examples
        - Akan-English relationships
        - general Akan knowledge
        - future academic knowledge in Akan
"""

from .akan_knowledge import create_akan_record


AKAN_KNOWLEDGE = [

    create_akan_record(
        record_id="akan_0001",
        akan_term="adwuma",
        english_term="work",
        category="general_knowledge",
        subcategory="vocabulary",
        definition_akan="Adwuma yɛ dwumadi anaa adeyɛ bi a obi yɛ de nya nea ɔrehwehwɛ.",
        definition_english="Work is an activity or task performed to achieve a desired result.",
        explanation_akan="Adwuma betumi akyerɛ nnwuma a yɛyɛ wɔ fie, sukuu, adwumam, afuo anaa beae foforo.",
        examples_akan=[
            "Merekɔ adwuma.",
            "Ɔreyɛ adwuma wɔ fie."
        ],
        examples_english=[
            "I am going to work.",
            "He is working at home."
        ],
        keywords_akan=[
            "adwuma",
            "yɛ adwuma",
            "adwumayɛ"
        ],
        keywords_english=[
            "work",
            "working",
            "job"
        ],
        question_patterns=[
            "Dɛn ne adwuma?",
            "Adwuma yɛ dɛn?",
            "Kyerɛkyerɛ adwuma mu."
        ],
    ),

    create_akan_record(
        record_id="akan_0002",
        akan_term="suku",
        english_term="school",
        category="education",
        subcategory="basic_education",
        definition_akan="Suku yɛ beae a wɔkyerɛkyerɛ nkurɔfo na wɔsua nimdeɛ ne ahokokwaw.",
        definition_english="A school is an institution where people receive education and develop knowledge and skills.",
        explanation_akan="Suku ma asuafo nya nimdeɛ, ahokokwaw ne nkyerɛkyerɛ a ɛboa wɔn wɔ asetena mu.",
        examples_akan=[
            "Merekɔ sukuu.",
            "Suku yɛ beae a yɛsua ade."
        ],
        examples_english=[
            "I am going to school.",
            "School is a place where we learn."
        ],
        keywords_akan=[
            "suku",
            "sukuu",
            "sukuu mu",
            "adesua"
        ],
        keywords_english=[
            "school",
            "education",
            "learning"
        ],
        question_patterns=[
            "Dɛn ne sukuu?",
            "Dɛn nti na yɛkɔ sukuu?",
            "Kyerɛkyerɛ sukuu mu."
        ],
    ),

    create_akan_record(
        record_id="akan_0003",
        akan_term="adesua",
        english_term="education",
        category="education",
        subcategory="learning",
        definition_akan="Adesua yɛ adeyɛ a obi nam so nya nimdeɛ, nteaseɛ ne ahokokwaw.",
        definition_english="Education is the process through which a person gains knowledge, understanding, and skills.",
        explanation_akan="Adesua betumi akɔ so wɔ sukuu, fie, adwumam anaa asetena mu.",
        examples_akan=[
            "Adesua ho hia wɔ asetena mu.",
            "Ɔde n’adwene asi adesua so."
        ],
        examples_english=[
            "Education is important in life.",
            "He has focused on his studies."
        ],
        keywords_akan=[
            "adesua",
            "sua ade",
            "nimdeɛ",
            "nkyerɛkyerɛ"
        ],
        keywords_english=[
            "education",
            "learning",
            "study",
            "knowledge"
        ],
        question_patterns=[
            "Dɛn ne adesua?",
            "Dɛn nti na adesua ho hia?",
            "Kyerɛkyerɛ adesua mu."
        ],
    ),

    create_akan_record(
        record_id="akan_0004",
        akan_term="nimdeɛ",
        english_term="knowledge",
        category="education",
        subcategory="knowledge",
        definition_akan="Nimdeɛ yɛ nteaseɛ ne nsɛm a obi sua anaa ohu fa ade bi ho.",
        definition_english="Knowledge is the understanding and information a person gains about something.",
        explanation_akan="Nimdeɛ betumi afi adesua, osuahu, nhwehwɛmu ne atie a yɛtie afiri afoforo hɔ.",
        examples_akan=[
            "Nimdeɛ boa obi ma ɔsi gyinae pa.",
            "Ɔwɔ nimdeɛ pii wɔ kɔmputa ho."
        ],
        examples_english=[
            "Knowledge helps a person make good decisions.",
            "He has much knowledge about computers."
        ],
        keywords_akan=[
            "nimdeɛ",
            "nteaseɛ",
            "osuahu"
        ],
        keywords_english=[
            "knowledge",
            "understanding",
            "experience"
        ],
        question_patterns=[
            "Dɛn ne nimdeɛ?",
            "Ɛhe na nimdeɛ fi?",
            "Dɛn nti na nimdeɛ ho hia?"
        ],
    ),

    create_akan_record(
        record_id="akan_0005",
        akan_term="abusua",
        english_term="family",
        category="society",
        subcategory="family",
        definition_akan="Abusua yɛ nnipa a wɔnam mogya, awareɛ anaa abusua ntam abusuabɔ so wɔ abusuabɔ.",
        definition_english="A family is a group of people connected through kinship, marriage, or family relationships.",
        explanation_akan="Abusua yɛ ade titiriw wɔ Akan amammerɛ mu na ɛboa ma wɔhwɛ wɔn ho, kyerɛkyerɛ mmofra na wɔkora amammerɛ so.",
        examples_akan=[
            "M’abusua wɔ Tarkwa.",
            "Abusua boa wɔn ho wɔn ho."
        ],
        examples_english=[
            "My family is in Tarkwa.",
            "Families support one another."
        ],
        keywords_akan=[
            "abusua",
            "abusuafo",
            "abusua mu"
        ],
        keywords_english=[
            "family",
            "relatives",
            "kinship"
        ],
        question_patterns=[
            "Dɛn ne abusua?",
            "Dɛn nti na abusua ho hia?",
            "Kyerɛkyerɛ abusua mu."
        ],
    ),

]


def get_seed_knowledge():
    """
    Return the initial Akan knowledge records.
    """

    return AKAN_KNOWLEDGE


def generate():
    """
    Generator-compatible entry point.
    """

    return get_seed_knowledge()
