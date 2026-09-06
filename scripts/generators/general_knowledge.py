"""
==============================================================
GENERAL KNOWLEDGE GENERATOR
Version 1.0
==============================================================

Generates structured educational records for:

- Countries
- Capitals
- Currencies
- Continents
- Oceans
- Mountains
- Rivers
- Astronomy
- Famous Scientists
- Inventors
- International Organizations
- Historical Events

Output:
    Standard knowledge-base records.
"""

from .common import build_record

CATEGORY = "General Knowledge"

VARIATIONS = [
    "definition",
    "explanation",
    "examples",
    "applications",
    "importance",
    "characteristics",
    "comparison",
    "revision",
    "exam_question",
    "true_false",
    "fill_blank",
    "real_world_example",
    "key_points",
    "short_answer",
    "common_mistake",
]

TOPICS = {

    "Countries":[
        "Ghana","Nigeria","Kenya","South Africa","Egypt","Morocco","Ethiopia",
        "United States","Canada","Brazil","Argentina","Mexico","United Kingdom",
        "France","Germany","Italy","Spain","Portugal","China","Japan","India",
        "Russia","Australia","New Zealand"
    ],

    "Capitals":[
        "Accra","Abuja","Nairobi","Pretoria","Cairo","Rabat","Addis Ababa",
        "Washington DC","Ottawa","Brasilia","Buenos Aires","Mexico City",
        "London","Paris","Berlin","Rome","Madrid","Lisbon","Beijing","Tokyo",
        "New Delhi","Moscow","Canberra","Wellington"
    ],

    "Currencies":[
        "Ghana Cedi","Naira","Rand","US Dollar","Canadian Dollar","Euro",
        "Pound Sterling","Japanese Yen","Chinese Yuan","Indian Rupee",
        "Australian Dollar"
    ],

    "Continents":[
        "Africa","Asia","Europe","North America","South America",
        "Australia","Antarctica"
    ],

    "Oceans":[
        "Atlantic Ocean","Pacific Ocean","Indian Ocean",
        "Arctic Ocean","Southern Ocean"
    ],

    "Rivers":[
        "River Nile","Amazon River","Mississippi River","River Volta",
        "River Niger","Yangtze River","River Thames"
    ],

    "Mountains":[
        "Mount Everest","Mount Kilimanjaro","Mount Elgon",
        "Mount Kenya","Aconcagua"
    ],

    "Astronomy":[
        "Solar System","Sun","Moon","Mercury","Venus","Earth","Mars",
        "Jupiter","Saturn","Uranus","Neptune","Pluto","Galaxy","Milky Way",
        "Black Hole","Asteroid","Comet","Meteor"
    ],

    "Scientists":[
        "Isaac Newton","Albert Einstein","Marie Curie","Galileo Galilei",
        "Nikola Tesla","Thomas Edison","Charles Darwin","Louis Pasteur"
    ],

    "Organizations":[
        "United Nations","African Union","ECOWAS","UNESCO",
        "World Health Organization","World Bank","International Monetary Fund"
    ],

    "Historical Events":[
        "World War One","World War Two","Industrial Revolution",
        "French Revolution","Moon Landing","Independence of Ghana"
    ]
}


def generate():

    records=[]

    for section, items in TOPICS.items():

        for topic in items:

            for variation in VARIATIONS:

                records.append(
                    build_record(
                        topic=topic,
                        category=CATEGORY,
                        variation=variation
                    )
                )

    return records