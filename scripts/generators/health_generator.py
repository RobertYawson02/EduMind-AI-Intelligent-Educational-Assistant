"""
==============================================================
HEALTH KNOWLEDGE GENERATOR
Version 1.0
==============================================================

Purpose:
    Generate structured educational health-science knowledge.

Coverage:
    - Human anatomy
    - Physiology
    - Nutrition
    - Hygiene
    - Public health
    - First aid
    - Common diseases
    - Infectious diseases
    - Non-communicable diseases
    - Mental health education
    - Maternal and child health
    - Health and lifestyle
    - Medical terminology
    - Health prevention
    - Health education

Output:
    Standard knowledge-base records.

Schema:
    {
        "topic": "...",
        "keywords": [...],
        "definition": "...",
        "explanation": "...",
        "examples": [...],
        "category": "Health Sciences"
    }

==============================================================
"""

from .common import build_record


CATEGORY = "Health Sciences"


# ============================================================
# HEALTH TOPICS
# ============================================================

TOPICS = {

    "Human Anatomy": [
        "Human body",
        "Brain",
        "Heart",
        "Lungs",
        "Kidneys",
        "Liver",
        "Stomach",
        "Small intestine",
        "Large intestine",
        "Pancreas",
        "Skin",
        "Bones",
        "Muscles",
        "Blood vessels",
        "Spinal cord",
        "Nervous system",
        "Digestive system",
        "Respiratory system",
        "Circulatory system",
        "Skeletal system",
        "Muscular system",
        "Urinary system",
        "Endocrine system",
        "Immune system",
        "Reproductive system",
    ],

    "Physiology": [
        "Blood circulation",
        "Breathing",
        "Digestion",
        "Heart rate",
        "Blood pressure",
        "Body temperature",
        "Hormones",
        "Reflex action",
        "Nerve impulse",
        "Respiration",
        "Homeostasis",
        "Metabolism",
        "Immune response",
        "Muscle contraction",
        "Kidney filtration",
    ],

    "Nutrition": [
        "Nutrition",
        "Carbohydrates",
        "Proteins",
        "Fats",
        "Vitamins",
        "Minerals",
        "Water",
        "Dietary fibre",
        "Balanced diet",
        "Malnutrition",
        "Iron",
        "Calcium",
        "Vitamin A",
        "Vitamin C",
        "Vitamin D",
        "Vitamin B12",
        "Food groups",
        "Healthy eating",
        "Food safety",
    ],

    "Hygiene and Prevention": [
        "Personal hygiene",
        "Hand washing",
        "Oral hygiene",
        "Dental hygiene",
        "Environmental hygiene",
        "Safe drinking water",
        "Sanitation",
        "Waste management",
        "Food hygiene",
        "Respiratory hygiene",
        "Disease prevention",
        "Vaccination",
        "Infection prevention",
    ],

    "Common Diseases": [
        "Malaria",
        "Common cold",
        "Influenza",
        "Diarrhea",
        "Cholera",
        "Typhoid fever",
        "Tuberculosis",
        "Pneumonia",
        "Asthma",
        "Diabetes",
        "Hypertension",
        "Anaemia",
        "Obesity",
        "Heart disease",
        "Stroke",
        "Cancer",
    ],

    "Infectious Diseases": [
        "Infectious disease",
        "Bacterial infection",
        "Viral infection",
        "Fungal infection",
        "Parasitic infection",
        "Disease transmission",
        "Pathogens",
        "Viruses",
        "Bacteria",
        "Fungi",
        "Parasites",
        "Epidemic",
        "Pandemic",
        "Vector-borne disease",
    ],

    "First Aid": [
        "First aid",
        "First aid kit",
        "Minor cuts",
        "Minor burns",
        "Nosebleed",
        "Sprain",
        "Strain",
        "Fainting",
        "Choking",
        "Heat exhaustion",
        "Dehydration",
        "Emergency response",
        "Calling emergency services",
    ],

    "Mental Health Education": [
        "Mental health",
        "Emotional wellbeing",
        "Stress",
        "Anxiety",
        "Depression",
        "Sleep and wellbeing",
        "Healthy relationships",
        "Social support",
        "Coping skills",
        "Self-care",
        "Academic stress",
    ],

    "Maternal and Child Health": [
        "Pregnancy",
        "Prenatal care",
        "Antenatal care",
        "Child nutrition",
        "Breastfeeding",
        "Child vaccination",
        "Child growth",
        "Child development",
        "Maternal nutrition",
        "Newborn care",
    ],

    "Healthy Lifestyle": [
        "Physical activity",
        "Exercise",
        "Sleep",
        "Healthy weight",
        "Stress management",
        "Healthy lifestyle",
        "Substance avoidance",
        "Screen time",
        "Rest and recovery",
    ],

    "Medical Terminology": [
        "Diagnosis",
        "Symptom",
        "Sign",
        "Treatment",
        "Prevention",
        "Medication",
        "Prescription",
        "Patient",
        "Healthcare provider",
        "Clinical examination",
        "Laboratory test",
        "Medical history",
    ],

    "Public Health": [
        "Public health",
        "Health promotion",
        "Disease surveillance",
        "Community health",
        "Health education",
        "Environmental health",
        "Occupational health",
        "Epidemiology",
        "Primary healthcare",
        "Healthcare system",
    ],
}


# ============================================================
# GENERATION VARIATIONS
# ============================================================

VARIATIONS = [

    "definition",

    "explanation",

    "importance",

    "functions",

    "characteristics",

    "causes",

    "effects",

    "prevention",

    "risk_factors",

    "symptoms",

    "examples",

    "applications",

    "classification",

    "key_points",

    "revision",

    "short_answer",

    "exam_question",

    "common_mistake",

    "real_world_example",

]


# ============================================================
# GENERATOR
# ============================================================

def generate():

    records = []

    for section, topics in TOPICS.items():

        for topic in topics:

            for variation in VARIATIONS:

                records.append(
                    build_record(
                        topic=topic,
                        category=CATEGORY,
                        variation=variation
                    )
                )

    return records