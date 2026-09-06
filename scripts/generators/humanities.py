"""
==============================================================
HUMANITIES KNOWLEDGE GENERATOR
Version 1.0
==============================================================

Purpose:
    Generate structured educational knowledge across the
    humanities and social-science domains.

Coverage:
    - History
    - Geography
    - Government and Civics
    - Economics
    - Sociology
    - Philosophy
    - Literature
    - Culture
    - Religion and Worldviews
    - Political Studies
    - Social Studies
    - Human Rights
    - Citizenship
    - Global Studies

Output:
    Standard knowledge-base records.

Schema:
    {
        "topic": "...",
        "keywords": [...],
        "definition": "...",
        "explanation": "...",
        "examples": [...],
        "category": "Humanities and Social Sciences"
    }

==============================================================
"""

from .common import build_record


CATEGORY = "Humanities and Social Sciences"


# ============================================================
# HUMANITIES TOPICS
# ============================================================

TOPICS = {

    # --------------------------------------------------------
    # HISTORY
    # --------------------------------------------------------

    "History": [
        "History",
        "Historical evidence",
        "Primary source",
        "Secondary source",
        "Ancient civilization",
        "Ancient Egypt",
        "Ancient Greece",
        "Roman Empire",
        "Ancient China",
        "Ancient India",
        "West African history",
        "Ghanaian history",
        "Ashanti Empire",
        "Mali Empire",
        "Songhai Empire",
        "Ghana Empire",
        "Trans-Saharan trade",
        "Atlantic slave trade",
        "European colonialism",
        "Colonialism in Africa",
        "Scramble for Africa",
        "Gold Coast",
        "British colonial rule",
        "Ghana independence",
        "African independence movements",
        "Pan-Africanism",
        "World War I",
        "World War II",
        "Cold War",
        "Industrial Revolution",
        "French Revolution",
        "American Revolution",
        "Russian Revolution",
        "Civil Rights Movement",
        "Decolonization",
        "Historical change",
        "Historical continuity",
        "Cause and effect in history",
        "Historical interpretation",
    ],

    # --------------------------------------------------------
    # GEOGRAPHY
    # --------------------------------------------------------

    "Geography": [
        "Geography",
        "Physical geography",
        "Human geography",
        "Environmental geography",
        "Map",
        "Map scale",
        "Latitude",
        "Longitude",
        "Equator",
        "Prime Meridian",
        "Time zones",
        "Continents",
        "Oceans",
        "Mountains",
        "Rivers",
        "Lakes",
        "Deserts",
        "Climate",
        "Weather",
        "Climate change",
        "Rainfall",
        "Temperature",
        "Humidity",
        "Wind",
        "Natural resources",
        "Population",
        "Population density",
        "Urbanization",
        "Migration",
        "Settlement",
        "Agriculture",
        "Deforestation",
        "Soil erosion",
        "Natural disasters",
        "Earthquakes",
        "Volcanoes",
        "Floods",
        "Drought",
        "Coastal erosion",
        "Sustainable development",
        "Geographical information systems",
    ],

    # --------------------------------------------------------
    # GOVERNMENT AND CIVICS
    # --------------------------------------------------------

    "Government and Civics": [
        "Government",
        "State",
        "Nation",
        "Nation-state",
        "Constitution",
        "Democracy",
        "Monarchy",
        "Republic",
        "Federal government",
        "Unitary government",
        "Parliamentary system",
        "Presidential system",
        "Separation of powers",
        "Checks and balances",
        "Executive branch",
        "Legislature",
        "Judiciary",
        "Rule of law",
        "Constitutional law",
        "Citizenship",
        "Civic responsibility",
        "Political participation",
        "Voting",
        "Election",
        "Political party",
        "Political representation",
        "Local government",
        "Decentralization",
        "Public policy",
        "Public administration",
        "Accountability",
        "Transparency",
        "Good governance",
        "Corruption",
        "Human rights",
        "Civil rights",
        "Freedom of expression",
        "Freedom of religion",
        "Freedom of association",
        "Justice",
    ],

    # --------------------------------------------------------
    # ECONOMICS
    # --------------------------------------------------------

    "Economics": [
        "Economics",
        "Microeconomics",
        "Macroeconomics",
        "Scarcity",
        "Choice",
        "Opportunity cost",
        "Demand",
        "Supply",
        "Market",
        "Price",
        "Equilibrium price",
        "Competition",
        "Monopoly",
        "Oligopoly",
        "Inflation",
        "Deflation",
        "Gross domestic product",
        "Gross national income",
        "Economic growth",
        "Economic development",
        "Unemployment",
        "Employment",
        "Fiscal policy",
        "Monetary policy",
        "Taxation",
        "Government spending",
        "Public debt",
        "Interest rate",
        "Central bank",
        "Money",
        "Banking",
        "International trade",
        "Imports",
        "Exports",
        "Exchange rate",
        "Foreign investment",
        "Entrepreneurship",
        "Productivity",
        "Poverty",
        "Income inequality",
    ],

    # --------------------------------------------------------
    # SOCIOLOGY
    # --------------------------------------------------------

    "Sociology": [
        "Sociology",
        "Society",
        "Culture",
        "Socialization",
        "Family",
        "Community",
        "Social group",
        "Social institution",
        "Social class",
        "Social status",
        "Social role",
        "Social norms",
        "Social values",
        "Social change",
        "Social structure",
        "Social interaction",
        "Social inequality",
        "Social mobility",
        "Urban society",
        "Rural society",
        "Population studies",
        "Gender roles",
        "Education and society",
        "Religion and society",
        "Crime and society",
        "Deviance",
        "Social control",
        "Globalization",
        "Migration and society",
        "Youth development",
    ],

    # --------------------------------------------------------
    # PHILOSOPHY
    # --------------------------------------------------------

    "Philosophy": [
        "Philosophy",
        "Metaphysics",
        "Epistemology",
        "Ethics",
        "Logic",
        "Aesthetics",
        "Political philosophy",
        "Philosophy of science",
        "Philosophy of mind",
        "Critical thinking",
        "Reasoning",
        "Argument",
        "Premise",
        "Conclusion",
        "Deductive reasoning",
        "Inductive reasoning",
        "Fallacy",
        "Truth",
        "Knowledge",
        "Belief",
        "Reality",
        "Free will",
        "Morality",
        "Justice",
        "Virtue",
        "Existentialism",
        "Stoicism",
        "Utilitarianism",
        "Deontology",
        "Natural law",
    ],

    # --------------------------------------------------------
    # LITERATURE
    # --------------------------------------------------------

    "Literature": [
        "Literature",
        "Prose",
        "Poetry",
        "Drama",
        "Novel",
        "Short story",
        "Essay",
        "Biography",
        "Autobiography",
        "Narrative",
        "Plot",
        "Character",
        "Setting",
        "Theme",
        "Conflict",
        "Point of view",
        "Narrator",
        "Symbolism",
        "Imagery",
        "Metaphor",
        "Simile",
        "Personification",
        "Irony",
        "Satire",
        "Alliteration",
        "Onomatopoeia",
        "Hyperbole",
        "Foreshadowing",
        "Flashback",
        "Tragedy",
        "Comedy",
        "Literary criticism",
        "Oral literature",
        "African literature",
        "Ghanaian literature",
        "Folktale",
        "Proverb",
        "Myth",
        "Legend",
    ],

    # --------------------------------------------------------
    # CULTURE
    # --------------------------------------------------------

    "Culture": [
        "Culture",
        "Cultural identity",
        "Cultural diversity",
        "Cultural heritage",
        "Tradition",
        "Custom",
        "Language and culture",
        "Food culture",
        "Music and culture",
        "Dance and culture",
        "Traditional clothing",
        "Festivals",
        "Family traditions",
        "African culture",
        "Ghanaian culture",
        "Akan culture",
        "Ewe culture",
        "Ga culture",
        "Dagomba culture",
        "Traditional leadership",
        "Chieftaincy",
        "Oral tradition",
        "Folklore",
        "Proverbs and culture",
        "Cultural change",
        "Cultural globalization",
        "Cultural preservation",
    ],

    # --------------------------------------------------------
    # RELIGION AND WORLDVIEWS
    # --------------------------------------------------------

    "Religion and Worldviews": [
        "Religion",
        "Worldview",
        "Religious belief",
        "Religious practice",
        "Religious tradition",
        "Christianity",
        "Islam",
        "Judaism",
        "Hinduism",
        "Buddhism",
        "Traditional African religions",
        "Akan traditional religion",
        "Religious ethics",
        "Religious festivals",
        "Sacred texts",
        "Prayer",
        "Worship",
        "Religious leadership",
        "Religious tolerance",
        "Interfaith dialogue",
        "Secularism",
        "Atheism",
        "Agnosticism",
        "Freedom of religion",
    ],

    # --------------------------------------------------------
    # POLITICAL STUDIES
    # --------------------------------------------------------

    "Political Studies": [
        "Politics",
        "Political science",
        "Political ideology",
        "Liberalism",
        "Conservatism",
        "Socialism",
        "Nationalism",
        "Capitalism",
        "Democratic participation",
        "Political power",
        "Political authority",
        "Political legitimacy",
        "Political institutions",
        "Political leadership",
        "Political communication",
        "Public opinion",
        "Civil society",
        "International relations",
        "Diplomacy",
        "Foreign policy",
        "Political conflict",
        "Political stability",
        "Peacebuilding",
        "Conflict resolution",
    ],

    # --------------------------------------------------------
    # HUMAN RIGHTS
    # --------------------------------------------------------

    "Human Rights": [
        "Human rights",
        "Universal human rights",
        "Right to life",
        "Right to education",
        "Right to health",
        "Right to privacy",
        "Freedom of speech",
        "Freedom of movement",
        "Freedom of religion",
        "Equality",
        "Non-discrimination",
        "Children's rights",
        "Women's rights",
        "Disability rights",
        "Refugee rights",
        "Workers' rights",
        "Digital rights",
        "Privacy rights",
        "Human dignity",
        "Social justice",
    ],

    # --------------------------------------------------------
    # SOCIAL STUDIES
    # --------------------------------------------------------

    "Social Studies": [
        "Social studies",
        "Family life",
        "Community development",
        "National development",
        "Leadership",
        "Followership",
        "Responsible citizenship",
        "Peace education",
        "Conflict management",
        "Decision making",
        "Problem solving",
        "Environmental responsibility",
        "Drug abuse prevention",
        "Road safety",
        "Personal responsibility",
        "Community participation",
        "National identity",
        "Patriotism",
        "Civic education",
        "Sustainable living",
    ],

    # --------------------------------------------------------
    # GLOBAL STUDIES
    # --------------------------------------------------------

    "Global Studies": [
        "Globalization",
        "Global economy",
        "Global health",
        "Global education",
        "International development",
        "International cooperation",
        "United Nations",
        "African Union",
        "ECOWAS",
        "World Bank",
        "International Monetary Fund",
        "UNESCO",
        "World Health Organization",
        "Climate diplomacy",
        "International migration",
        "Global inequality",
        "Sustainable Development Goals",
        "Global citizenship",
        "International law",
        "Humanitarian action",
    ],
}


# ============================================================
# GENERATION VARIATIONS
# ============================================================

VARIATIONS = [

    "definition",

    "explanation",

    "importance",

    "characteristics",

    "causes",

    "effects",

    "advantages",

    "disadvantages",

    "functions",

    "types",

    "classification",

    "examples",

    "applications",

    "historical_context",

    "modern_context",

    "comparison",

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