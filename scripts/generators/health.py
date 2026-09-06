"""
==============================================================
HEALTH SCIENCES KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY = "Health Sciences"

CONCEPTS = [

    # Human body
    ("Human Health", ["health"]),
    ("Human Body", ["human anatomy"]),
    ("Cell", ["body cell"]),
    ("Tissue", ["body tissue"]),
    ("Organ", ["body organ"]),
    ("Organ System", ["body system"]),

    # Major systems
    ("Digestive System", ["digestion"]),
    ("Respiratory System", ["breathing system"]),
    ("Circulatory System", ["blood circulation"]),
    ("Nervous System", ["nervous system"]),
    ("Endocrine System", ["hormone system"]),
    ("Immune System", ["immunity"]),
    ("Skeletal System", ["bones"]),
    ("Muscular System", ["muscles"]),
    ("Urinary System", ["excretory system"]),
    ("Reproductive System", ["reproduction"]),

    # Nutrition
    ("Nutrition", ["healthy eating"]),
    ("Balanced Diet", ["balanced nutrition"]),
    ("Carbohydrate", ["carbohydrates"]),
    ("Protein", ["proteins"]),
    ("Fat", ["dietary fats"]),
    ("Vitamin", ["vitamins"]),
    ("Mineral", ["minerals"]),
    ("Water", ["drinking water"]),
    ("Fiber", ["dietary fiber"]),
    ("Malnutrition", ["poor nutrition"]),
    ("Obesity", ["overweight"]),
    ("Undernutrition", ["underweight"]),

    # Diseases
    ("Disease", ["illness"]),
    ("Infection", ["infectious disease"]),
    ("Bacteria", ["bacterial infection"]),
    ("Virus", ["viral infection"]),
    ("Fungi", ["fungal infection"]),
    ("Parasite", ["parasitic infection"]),
    ("Malaria", ["malaria disease"]),
    ("Tuberculosis", ["TB"]),
    ("HIV", ["human immunodeficiency virus"]),
    ("AIDS", ["acquired immune deficiency syndrome"]),
    ("Diabetes", ["diabetes mellitus"]),
    ("Hypertension", ["high blood pressure"]),
    ("Asthma", ["asthma disease"]),
    ("Cholera", ["cholera disease"]),

    # First Aid
    ("First Aid", ["emergency care"]),
    ("CPR", ["cardiopulmonary resuscitation"]),
    ("Burn", ["burn injury"]),
    ("Bleeding", ["hemorrhage"]),
    ("Fracture", ["broken bone"]),
    ("Shock", ["medical shock"]),
    ("Choking", ["airway obstruction"]),

    # Public Health
    ("Public Health", ["community health"]),
    ("Vaccination", ["immunization"]),
    ("Sanitation", ["hygiene"]),
    ("Personal Hygiene", ["cleanliness"]),
    ("Disease Prevention", ["preventive health"]),
    ("Mental Health", ["psychological health"]),
    ("Stress Management", ["stress reduction"]),
    ("Exercise", ["physical activity"]),
    ("Sleep", ["healthy sleep"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records