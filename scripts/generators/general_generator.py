"""
==============================================================
GENERAL KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate broad foundational educational knowledge covering
    everyday concepts, society, communication, culture,
    environment, citizenship, life skills, and general studies.

Architecture:
    Uses the shared common.py utilities.

Output:
    Standard Version 3 knowledge records.
"""

from __future__ import annotations

from .common import build_knowledge_family


# ============================================================
# CATEGORY
# ============================================================

CATEGORY = "General Knowledge"


# ============================================================
# GENERAL KNOWLEDGE TOPICS
# ============================================================

TOPICS = [

    # --------------------------------------------------------
    # General Knowledge
    # --------------------------------------------------------

    ("Knowledge", ["human knowledge", "information"]),
    ("General Knowledge", ["common knowledge", "general studies"]),
    ("Information", ["facts", "knowledge"]),
    ("Fact", ["factual information", "verified information"]),
    ("Concept", ["idea", "abstract concept"]),
    ("Idea", ["thought", "notion"]),
    ("Theory", ["theoretical explanation"]),
    ("Principle", ["fundamental principle", "basic rule"]),
    ("Evidence", ["supporting evidence", "proof"]),
    ("Reasoning", ["logical reasoning", "thinking"]),
    ("Logic", ["logical thinking", "reasoning"]),
    ("Common Sense", ["practical reasoning"]),
    ("Observation", ["careful observation", "noticing"]),
    ("Experience", ["practical experience", "lived experience"]),

    # --------------------------------------------------------
    # Communication
    # --------------------------------------------------------

    ("Communication", ["human communication", "information exchange"]),
    ("Verbal Communication", ["spoken communication"]),
    ("Nonverbal Communication", ["body language", "non-verbal communication"]),
    ("Written Communication", ["written language", "written expression"]),
    ("Listening", ["active listening", "listening skills"]),
    ("Speaking", ["oral communication", "speaking skills"]),
    ("Reading", ["reading skills", "text comprehension"]),
    ("Writing", ["writing skills", "written expression"]),
    ("Public Speaking", ["speech", "oral presentation"]),
    ("Interpersonal Communication", ["person-to-person communication"]),
    ("Mass Communication", ["media communication", "public communication"]),
    ("Feedback", ["communication feedback", "response"]),
    ("Language", ["human language", "linguistic communication"]),
    ("Translation", ["language translation", "translation process"]),
    ("Interpretation", ["language interpretation", "oral interpretation"]),

    # --------------------------------------------------------
    # Society
    # --------------------------------------------------------

    ("Society", ["human society", "social community"]),
    ("Community", ["local community", "social group"]),
    ("Culture", ["human culture", "cultural practices"]),
    ("Tradition", ["cultural tradition", "custom"]),
    ("Custom", ["social custom", "cultural practice"]),
    ("Socialization", ["social development", "social learning"]),
    ("Social Institution", ["social organization", "institution"]),
    ("Family", ["family system", "household"]),
    ("Education in Society", ["education and society"]),
    ("Religion in Society", ["religion and society"]),
    ("Social Values", ["societal values", "shared values"]),
    ("Social Norms", ["social rules", "societal norms"]),
    ("Social Change", ["societal change", "social transformation"]),
    ("Social Development", ["community development", "social progress"]),
    ("Social Responsibility", ["social duty", "community responsibility"]),

    # --------------------------------------------------------
    # Citizenship
    # --------------------------------------------------------

    ("Citizenship", ["citizen participation", "civic identity"]),
    ("Citizen", ["member of a state", "national citizen"]),
    ("Civic Education", ["civic studies", "citizenship education"]),
    ("Civic Responsibility", ["civic duty", "citizenship responsibility"]),
    ("Human Rights", ["fundamental rights", "rights of people"]),
    ("Civil Rights", ["citizens' rights", "legal rights"]),
    ("Freedom", ["liberty", "individual freedom"]),
    ("Equality", ["equal treatment", "social equality"]),
    ("Justice", ["fairness", "social justice"]),
    ("Democracy", ["democratic government", "popular government"]),
    ("Rule of Law", ["law and governance", "legal principle"]),
    ("Constitution", ["constitutional law", "national constitution"]),
    ("Government", ["public administration", "state government"]),
    ("Public Service", ["government service", "public administration"]),
    ("Leadership", ["leadership skills", "effective leadership"]),
    ("Good Governance", ["effective governance", "responsible government"]),

    # --------------------------------------------------------
    # Geography
    # --------------------------------------------------------

    ("Geography", ["study of Earth", "geographical studies"]),
    ("Physical Geography", ["natural geography"]),
    ("Human Geography", ["social geography", "human geography"]),
    ("Earth", ["planet Earth", "world"]),
    ("Continent", ["continental region"]),
    ("Country", ["nation", "sovereign state"]),
    ("State", ["political state", "territory"]),
    ("Capital City", ["national capital", "capital"]),
    ("City", ["urban area", "municipality"]),
    ("Town", ["settlement", "urban settlement"]),
    ("Village", ["rural settlement"]),
    ("Population", ["human population"]),
    ("Population Growth", ["population increase"]),
    ("Migration", ["human migration", "movement of people"]),
    ("Urbanization", ["urban development", "urban growth"]),
    ("Rural Area", ["rural community", "countryside"]),
    ("Urban Area", ["city area", "urban community"]),
    ("Map", ["geographical map", "mapping"]),
    ("Map Scale", ["geographical scale"]),
    ("Latitude", ["geographic latitude"]),
    ("Longitude", ["geographic longitude"]),
    ("Climate", ["regional climate", "climate system"]),
    ("Weather", ["atmospheric conditions", "weather conditions"]),
    ("Natural Resource", ["natural resources", "Earth resources"]),

    # --------------------------------------------------------
    # Environment
    # --------------------------------------------------------

    ("Environment", ["natural environment", "surroundings"]),
    ("Environmental Science", ["environmental studies"]),
    ("Ecosystem", ["ecological system"]),
    ("Ecology", ["study of ecosystems"]),
    ("Biodiversity", ["biological diversity", "species diversity"]),
    ("Conservation", ["environmental conservation", "resource conservation"]),
    ("Deforestation", ["forest loss", "forest destruction"]),
    ("Afforestation", ["tree planting", "forest establishment"]),
    ("Reforestation", ["forest restoration", "tree replanting"]),
    ("Pollution", ["environmental pollution"]),
    ("Air Pollution", ["atmospheric pollution"]),
    ("Water Pollution", ["aquatic pollution"]),
    ("Soil Pollution", ["land pollution"]),
    ("Noise Pollution", ["environmental noise"]),
    ("Waste Management", ["waste disposal", "waste control"]),
    ("Recycling", ["material recycling", "waste recycling"]),
    ("Climate Change", ["global climate change"]),
    ("Global Warming", ["Earth warming", "climate warming"]),
    ("Greenhouse Effect", ["atmospheric greenhouse effect"]),
    ("Sustainable Development", ["sustainability", "sustainable growth"]),
    ("Renewable Resource", ["renewable natural resource"]),
    ("Nonrenewable Resource", ["finite natural resource"]),

    # --------------------------------------------------------
    # Economy and Everyday Economics
    # --------------------------------------------------------

    ("Economy", ["economic system", "national economy"]),
    ("Economics", ["economic studies"]),
    ("Supply", ["economic supply"]),
    ("Demand", ["economic demand"]),
    ("Market", ["economic market", "marketplace"]),
    ("Price", ["market price", "cost"]),
    ("Income", ["personal income", "earnings"]),
    ("Saving", ["personal saving", "financial saving"]),
    ("Investment", ["financial investment"]),
    ("Budget", ["financial budget", "budget planning"]),
    ("Inflation", ["price inflation", "rising prices"]),
    ("Deflation", ["falling prices", "economic deflation"]),
    ("Employment", ["work", "employment opportunity"]),
    ("Unemployment", ["lack of employment"]),
    ("Entrepreneurship", ["business creation", "entrepreneurial activity"]),
    ("Trade", ["economic trade", "exchange"]),
    ("International Trade", ["global trade", "international commerce"]),
    ("Tax", ["taxation", "government tax"]),
    ("Banking", ["banking system", "financial services"]),
    ("Money", ["currency", "medium of exchange"]),
    ("Currency", ["money system", "national currency"]),

    # --------------------------------------------------------
    # Personal Development
    # --------------------------------------------------------

    ("Personal Development", ["self-development", "personal growth"]),
    ("Self-Awareness", ["self knowledge", "self-understanding"]),
    ("Self-Discipline", ["personal discipline", "self-control"]),
    ("Confidence", ["self-confidence", "personal confidence"]),
    ("Goal Setting", ["personal goals", "goal planning"]),
    ("Decision Making", ["decision skills", "making decisions"]),
    ("Time Management", ["time planning", "time organization"]),
    ("Stress Management", ["stress control", "stress reduction"]),
    ("Emotional Intelligence", ["EQ", "emotional awareness"]),
    ("Resilience", ["psychological resilience", "adaptability"]),
    ("Motivation", ["personal motivation", "drive"]),
    ("Teamwork", ["team collaboration", "group work"]),
    ("Cooperation", ["collaboration", "working together"]),
    ("Conflict Resolution", ["conflict management", "dispute resolution"]),
    ("Leadership Skills", ["leadership abilities"]),
    ("Life Skills", ["practical life skills", "daily living skills"]),

    # --------------------------------------------------------
    # Culture and Heritage
    # --------------------------------------------------------

    ("Heritage", ["cultural heritage", "national heritage"]),
    ("Cultural Heritage", ["cultural inheritance"]),
    ("National Heritage", ["national culture", "heritage"]),
    ("Folklore", ["traditional stories", "folk culture"]),
    ("Myth", ["traditional myth", "mythology"]),
    ("Legend", ["traditional legend", "historical story"]),
    ("Proverb", ["traditional proverb", "wise saying"]),
    ("Traditional Music", ["folk music", "traditional songs"]),
    ("Traditional Dance", ["cultural dance", "folk dance"]),
    ("Traditional Art", ["folk art", "cultural art"]),
    ("Craftsmanship", ["traditional crafts", "craft skills"]),
    ("Museum", ["cultural museum", "heritage museum"]),
    ("Archaeology", ["archaeological studies", "ancient remains"]),
    ("Heritage Preservation", ["cultural preservation"]),
    ("Cultural Identity", ["identity and culture", "cultural identity"]),

    # --------------------------------------------------------
    # History
    # --------------------------------------------------------

    ("History", ["historical studies", "study of the past"]),
    ("Historical Event", ["event in history", "past event"]),
    ("Historical Evidence", ["evidence from history"]),
    ("Ancient Civilization", ["ancient society", "early civilization"]),
    ("Civilization", ["human civilization", "advanced society"]),
    ("Empire", ["historical empire", "imperial state"]),
    ("Kingdom", ["historical kingdom", "monarchy"]),
    ("Colonialism", ["colonial rule", "colonial system"]),
    ("Independence", ["national independence", "self-rule"]),
    ("Industrial Revolution", ["industrialization", "industrial development"]),
    ("World War", ["global war", "major international conflict"]),
    ("Political History", ["history of politics"]),
    ("Economic History", ["history of economics"]),
    ("Social History", ["history of society"]),
    ("African History", ["history of Africa", "African historical studies"]),

    # --------------------------------------------------------
    # Media and Information
    # --------------------------------------------------------

    ("Media", ["mass media", "communication media"]),
    ("News", ["current news", "news information"]),
    ("Journalism", ["news reporting", "journalistic studies"]),
    ("Newspaper", ["print news", "news publication"]),
    ("Radio", ["radio broadcasting"]),
    ("Television", ["TV broadcasting", "television media"]),
    ("Social Media", ["social networking", "online social media"]),
    ("Digital Media", ["online media", "digital communication"]),
    ("Advertising", ["commercial communication", "advertisement"]),
    ("Public Relations", ["PR", "organizational communication"]),
    ("Media Literacy", ["media awareness", "media education"]),
    ("Information Literacy", ["information skills", "information evaluation"]),
    ("Misinformation", ["false information", "incorrect information"]),
    ("Disinformation", ["deliberately false information"]),
    ("Fact Checking", ["fact verification", "information verification"]),

    # --------------------------------------------------------
    # Everyday Science
    # --------------------------------------------------------

    ("Science", ["scientific knowledge", "scientific studies"]),
    ("Scientific Method", ["scientific investigation"]),
    ("Observation", ["scientific observation"]),
    ("Experiment", ["scientific experiment"]),
    ("Measurement", ["scientific measurement"]),
    ("Matter", ["physical matter", "substance"]),
    ("Energy", ["physical energy", "energy forms"]),
    ("Force", ["physical force", "interaction"]),
    ("Motion", ["movement", "physical motion"]),
    ("Light", ["visible light", "electromagnetic radiation"]),
    ("Sound", ["sound waves", "audible sound"]),
    ("Heat", ["thermal energy", "heat transfer"]),
    ("Temperature", ["thermal temperature"]),
    ("Electricity", ["electrical energy", "electric power"]),
    ("Magnetism", ["magnetic effects", "magnetic force"]),

    # --------------------------------------------------------
    # Practical Technology
    # --------------------------------------------------------

    ("Technology", ["modern technology", "technological systems"]),
    ("Digital Literacy", ["digital skills", "technology literacy"]),
    ("Internet Literacy", ["online literacy", "internet skills"]),
    ("Computer Literacy", ["basic computer skills"]),
    ("Mobile Technology", ["mobile devices", "mobile computing"]),
    ("Smartphone", ["mobile phone", "smart device"]),
    ("Artificial Intelligence", ["AI", "intelligent systems"]),
    ("Robotics", ["robot technology", "robotics"]),
    ("Automation", ["automated technology"]),
    ("Cybersecurity Awareness", ["online security awareness"]),
    ("Cloud Technology", ["cloud services", "cloud systems"]),
    ("Digital Payment", ["electronic payment", "cashless payment"]),
    ("Electronic Commerce", ["e-commerce", "online shopping"]),
    ("Online Education", ["digital education", "e-learning"]),

    # --------------------------------------------------------
    # Health and Wellbeing — General Awareness
    # --------------------------------------------------------

    ("Health", ["human health", "wellbeing"]),
    ("Wellbeing", ["wellness", "healthy living"]),
    ("Nutrition", ["healthy nutrition", "food and nutrition"]),
    ("Balanced Diet", ["healthy diet", "balanced nutrition"]),
    ("Physical Activity", ["exercise", "physical fitness"]),
    ("Personal Hygiene", ["hygiene", "cleanliness"]),
    ("Sleep", ["healthy sleep", "rest"]),
    ("Mental Wellbeing", ["emotional wellbeing", "psychological wellbeing"]),
    ("Healthy Lifestyle", ["healthy living", "health habits"]),
    ("Public Health", ["community health", "population health"]),
    ("Health Education", ["health awareness", "health learning"]),

    # --------------------------------------------------------
    # Ethics and Values
    # --------------------------------------------------------

    ("Ethics", ["moral philosophy", "ethical principles"]),
    ("Morality", ["moral values", "moral behaviour"]),
    ("Integrity", ["honesty", "moral integrity"]),
    ("Honesty", ["truthfulness", "honest behaviour"]),
    ("Respect", ["mutual respect", "respectful behaviour"]),
    ("Responsibility", ["personal responsibility", "social responsibility"]),
    ("Accountability", ["being accountable", "responsibility"]),
    ("Fairness", ["fair treatment", "justice"]),
    ("Trust", ["trustworthiness", "social trust"]),
    ("Empathy", ["understanding others", "emotional empathy"]),
    ("Tolerance", ["respect for differences", "social tolerance"]),
    ("Compassion", ["care for others", "kindness"]),
    ("Ethical Decision Making", ["moral decision making"]),

    # --------------------------------------------------------
    # Religion and Worldviews — General Academic Study
    # --------------------------------------------------------

    ("Religion", ["religious studies", "faith systems"]),
    ("Religious Studies", ["study of religion"]),
    ("Worldview", ["world view", "belief system"]),
    ("Belief", ["belief system", "personal belief"]),
    ("Faith", ["religious faith", "faith system"]),
    ("Religious Tradition", ["faith tradition", "religious culture"]),
    ("Religious Text", ["sacred text", "religious scripture"]),
    ("Religious Ethics", ["religious morality"]),
    ("Interfaith Dialogue", ["religious dialogue", "interfaith communication"]),
    ("Religious Diversity", ["diversity of religions"]),

    # --------------------------------------------------------
    # Practical Everyday Knowledge
    # --------------------------------------------------------

    ("Transportation", ["transport systems", "movement of people"]),
    ("Road Safety", ["traffic safety", "road awareness"]),
    ("Public Transportation", ["mass transit", "public transport"]),
    ("Housing", ["residential housing", "shelter"]),
    ("Food Safety", ["safe food handling", "food hygiene"]),
    ("Consumer Awareness", ["consumer education", "consumer rights"]),
    ("Financial Literacy", ["money management", "financial education"]),
    ("Digital Safety", ["online safety", "internet safety"]),
    ("Emergency Preparedness", ["emergency planning", "disaster preparedness"]),
    ("Disaster Management", ["disaster response", "emergency management"]),
    ("First Aid Awareness", ["basic first aid", "emergency first aid"]),
    ("Community Development", ["local development", "community improvement"]),

]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """
    Generate the complete General Knowledge knowledge base.
    """

    records = []

    for topic, aliases in TOPICS:

        records.extend(
            build_knowledge_family(
                topic=topic,
                category=CATEGORY,
                aliases=aliases,
                education_level="university",
                difficulty="intermediate",
            )
        )

    return records
