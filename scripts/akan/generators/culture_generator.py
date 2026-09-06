"""
==============================================================
AKAN CULTURE KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate structured Akan cultural knowledge.

This is NOT a translation-only dataset.

Coverage:
    - Akan identity
    - Akan communities
    - Family and kinship
    - Matrilineal organization
    - Elders and respect
    - Chieftaincy
    - Queenmothers
    - Festivals
    - Naming traditions
    - Marriage traditions
    - Funeral traditions
    - Food and cuisine
    - Clothing and textiles
    - Kente
    - Adinkra
    - Oral tradition
    - Ananse stories
    - Proverbs
    - Music and dance
    - Greetings
    - Hospitality
    - Community life
    - Traditional education
    - Occupations
    - Inheritance and heritage
    - Language and identity
    - Childhood and upbringing
    - Social values
    - Cultural preservation
    - Modern Akan society
    - Akan culture and technology

The generator uses the shared Akan schema.

IMPORTANT:
    This file is designed to work when the generator is loaded
    by the central Akan knowledge-base builder.

==============================================================
"""

from __future__ import annotations


# ============================================================
# SCHEMA IMPORT
# ============================================================

# Preferred import when this file is loaded as part of the
# scripts.akan.generators package.
try:
    from ..data.akan_schema import create_akan_record

# Fallback import for environments where the project root is
# placed directly on sys.path.
except ImportError:
    try:
        from akan_schema import create_akan_record
    except ImportError as exc:
        raise ImportError(
            "Unable to import create_akan_record from akan_schema. "
            "Make sure scripts/akan/data/akan_schema.py exists."
        ) from exc


# ============================================================
# HELPER
# ============================================================

def make_item(
    akan_term: str,
    english_term: str,
    subcategory: str,
    definition_akan: str,
    definition_english: str,
    explanation_akan: str,
    examples_akan: list[str],
    examples_english: list[str],
    keywords_akan: list[str],
    keywords_english: list[str],
    question_patterns: list[str],
) -> dict:
    """
    Create one intermediate cultural knowledge item.

    The item is later converted into the project's shared
    Akan record format by generate().
    """

    return {
        "akan_term": akan_term,
        "english_term": english_term,
        "subcategory": subcategory,
        "definition_akan": definition_akan,
        "definition_english": definition_english,
        "explanation_akan": explanation_akan,
        "examples_akan": examples_akan,
        "examples_english": examples_english,
        "keywords_akan": keywords_akan,
        "keywords_english": keywords_english,
        "question_patterns": question_patterns,
    }


# ============================================================
# CULTURAL KNOWLEDGE
# ============================================================

CULTURE = [

    # ========================================================
    # 1. AKAN IDENTITY
    # ========================================================

    make_item(
        "Akan",
        "Akan identity",
        "identity",
        "Akan yɛ din a wɔde frɛ nnipa ne kasa ne amammerɛ akuw a wɔwɔ Abibirem Atɔeɛ.",
        "Akan refers to a major cultural and linguistic identity in West Africa.",
        "Akan nipasu ka kasa, abusua, amammerɛ, abakɔsɛm, gyinapɛn ne asetena mu nkitahodie ho.",
        ["Akan nipasu wɔ kasa ne amammerɛ mu."],
        ["Akan identity is expressed through language and culture."],
        ["Akan", "Akan nipasu", "Akanfoɔ"],
        ["Akan", "Akan identity", "Akan people"],
        [
            "Dɛn ne Akan?",
            "Hwan ne Akanfoɔ?",
            "What is Akan identity?",
        ],
    ),

    make_item(
        "Akanfoɔ",
        "Akan people",
        "identity",
        "Akanfoɔ yɛ nnipa a wɔwɔ Akan kasa ne amammerɛ mu nkitahodie.",
        "Akan people are communities associated with Akan languages and cultural traditions.",
        "Akanfoɔ wɔ mmeaeɛ ahodoɔ wɔ Ghana ne Abibirem Atɔeɛ, na wɔn amammerɛ wɔ nsonsonoeɛ wɔ mpɔtam ahodoɔ mu.",
        ["Akanfoɔ wɔ Ghana ne Abibirem Atɔeɛ mmeaeɛ ahodoɔ."],
        ["Akan people live in different parts of Ghana and West Africa."],
        ["Akanfoɔ", "Akan", "Akan nnipa"],
        ["Akan people", "Akan communities"],
        [
            "Hwan ne Akanfoɔ?",
            "Ɛhe na Akanfoɔ te?",
            "Who are the Akan people?",
        ],
    ),

    make_item(
        "Akan amammerɛ",
        "Akan culture",
        "identity",
        "Akan amammerɛ yɛ amanneɛ, gyinapɛn, kasa, gyidie ne asetena mu nneyɛeɛ a wɔde kɔ awoɔ ntoatoasoɔ so.",
        "Akan culture consists of customs, values, language, beliefs, and practices transmitted across generations.",
        "Akan amammerɛ ka abusua, kasa, aduane, ntoma, afahyɛ, nnwom, anansesɛm ne obu ho.",
        ["Akan amammerɛ wɔ nneɛma pii a ɛka ho."],
        ["Akan culture includes many forms of social and cultural expression."],
        ["Akan amammerɛ", "amammerɛ", "Akan asetena"],
        ["Akan culture", "Akan traditions", "Akan customs"],
        [
            "Dɛn ne Akan amammerɛ?",
            "Akan amammerɛ yɛ dɛn?",
            "What is Akan culture?",
        ],
    ),

    make_item(
        "Akanfoɔ asetena",
        "Akan way of life",
        "identity",
        "Akanfoɔ asetena yɛ ɔkwan ahodoɔ a Akanfoɔ fa so tena, di nkitaho na wɔyɛ wɔn amammerɛ mu dwumadie.",
        "Akan way of life refers to patterns of living, social interaction, and cultural practice among Akan communities.",
        "Asetena mu nneɛma ka abusua, adwuma, kasa, amanneɛ, afahyɛ ne mpɔtam mu nkabom ho.",
        ["Akanfoɔ asetena wɔ abusua ne mpɔtam nkabom mu."],
        ["Akan life includes family and community relationships."],
        ["Akanfoɔ asetena", "asetena", "Akan amammerɛ"],
        ["Akan way of life", "Akan lifestyle", "Akan society"],
        [
            "Dɛn ne Akanfoɔ asetena?",
            "Akanfoɔ tena sɛn?",
            "What is the Akan way of life?",
        ],
    ),

    # ========================================================
    # 2. FAMILY AND KINSHIP
    # ========================================================

    make_item(
        "Abusua",
        "Family and kinship",
        "family and kinship",
        "Abusua yɛ nnipa a wɔnam abusua mu abusuabɔ so wɔ ayɔnkofa.",
        "Abusua refers to family and kinship relationships.",
        "Abusua yɛ Akan asetena mu fapem na ɛka ɔboa, asɛyɛdeɛ ne abusua mu nkitahodie ho.",
        ["Abusuafoɔ boa wɔn ho wɔ ahohiahia mu."],
        ["Family members support one another during difficult times."],
        ["abusua", "abusuafoɔ", "abusua mu"],
        ["family", "relatives", "kinship"],
        [
            "Dɛn ne abusua?",
            "Dɛn nti na abusua ho hia?",
            "What is family in Akan culture?",
        ],
    ),

    make_item(
        "Matrilineal abusua",
        "Matrilineal kinship",
        "family and kinship",
        "Matrilineal abusua yɛ abusua nhyehyɛeɛ a wɔde ɛna afam so kyerɛ abusua mu nkitahodie wɔ Akan amammerɛ mu.",
        "Matrilineal kinship traces important family relationships through the maternal line.",
        "Akan abusua nhyehyɛeɛ wɔ mmeaeɛ pii mu ma ɛna afam so nya dwuma wɔ abusua mu nkitahodie ne agyapadeɛ mu.",
        ["Abusua mu nkitahodie betumi afa ɛna afam so."],
        ["Kinship relationships may be traced through the maternal line."],
        ["matrilineal abusua", "ɛna afam", "abusua"],
        ["matrilineal kinship", "maternal lineage"],
        [
            "Dɛn ne matrilineal abusua?",
            "Akan abusua fa he?",
            "What is matrilineal kinship?",
        ],
    ),

    make_item(
        "Abusua panyin",
        "Family elder",
        "family and kinship",
        "Abusua panyin yɛ ɔpanyin a ɔwɔ abusua mu dwuma wɔ afotuo ne abusua nsɛm mu.",
        "A family elder is a respected senior person who helps guide family affairs.",
        "Abusua panyin betumi de osuahunu ne afotuo aboa abusua no wɔ nsɛm ahodoɔ mu.",
        ["Abusua panyin de afotuo ma abusuafoɔ."],
        ["A family elder gives advice to relatives."],
        ["abusua panyin", "panyin", "abusua"],
        ["family elder", "senior relative"],
        [
            "Hwan ne abusua panyin?",
            "Dɛn ne abusua panyin dwuma?",
        ],
    ),

    make_item(
        "Abusuafoɔ",
        "Relatives",
        "family and kinship",
        "Abusuafoɔ yɛ nnipa a wɔka abusua baako anaa wɔwɔ abusua mu abusuabɔ.",
        "Relatives are people connected through a family or kinship relationship.",
        "Abusuafoɔ betumi aboa wɔn ho wɔ ayie, awareɛ, afahyɛ ne nsɛnnennen mu.",
        ["Abusuafoɔ hyia wɔ abusua dwumadie ase."],
        ["Relatives gather during family occasions."],
        ["abusuafoɔ", "abusua", "abusua mu"],
        ["relatives", "family members", "kin"],
        [
            "Hwan ne abusuafoɔ?",
            "Dɛn ne abusuafoɔ?",
        ],
    ),

    make_item(
        "Abusua mu ayɔnkofa",
        "Family relationship",
        "family and kinship",
        "Abusua mu ayɔnkofa yɛ abusuabɔ ne nkitahodie a ɛda abusuafoɔ ntam.",
        "Family relationship refers to connections and interactions among relatives.",
        "Abusua mu ayɔnkofa betumi akɔ so denam mmoa, afotuo, nkitahodie ne dwumadie a wɔyɛ bom so.",
        ["Abusua mu ayɔnkofa betumi ayɛ den denam mmoa so."],
        ["Family relationships can become stronger through mutual support."],
        ["abusua", "ayɔnkofa", "nkitahodie"],
        ["family relationship", "kinship relationship", "family ties"],
        [
            "Dɛn ne abusua mu ayɔnkofa?",
            "Ɔkwan bɛn so na abusuafoɔ hyɛ wɔn ho den?",
        ],
    ),

    # ========================================================
    # 3. ELDERS AND RESPECT
    # ========================================================

    make_item(
        "Mpanyimfoɔ",
        "Elders",
        "elders and respect",
        "Mpanyimfoɔ yɛ nnipa a wɔn mfeɛ, osuahunu ne nyansa ma wɔwɔ dwuma titire wɔ abusua ne mpɔtam mu.",
        "Elders are respected members of a family or community whose experience gives them important roles.",
        "Mpanyimfoɔ de afotuo ma mmofra, siesie ntam na wɔboa ma wɔsi gyinaeɛ.",
        ["Mpanyimfoɔ de afotuo ma mmofra."],
        ["Elders advise younger people."],
        ["mpanyimfoɔ", "panyin", "mpanyimfoɔ dwuma"],
        ["elders", "Akan elders", "community elders"],
        [
            "Hwan ne mpanyimfoɔ?",
            "Dɛn ne mpanyimfoɔ dwuma?",
        ],
    ),

    make_item(
        "Obu",
        "Respect",
        "elders and respect",
        "Obu yɛ suban a ɛkyerɛ sɛ obi bu nnipa, mpanyimfoɔ ne afoforo.",
        "Respect is a social value expressed toward elders and other people.",
        "Obu ne ahobrɛaseɛ yɛ Akan asetena mu gyinapɛn a ɛboa ma nkurɔfoɔ tena asomdwoeɛ mu.",
        ["Mmofra sua sɛ wɔmmfa obu nni mpanyimfoɔ anim."],
        ["Children are taught to show respect toward elders."],
        ["obu", "obu ma mpanyimfoɔ", "ahobrɛaseɛ"],
        ["respect", "humility", "social respect"],
        [
            "Dɛn ne obu?",
            "Dɛn nti na obu ho hia?",
            "How is respect expressed?",
        ],
    ),

    make_item(
        "Ahobrɛaseɛ",
        "Humility",
        "social values",
        "Ahobrɛaseɛ yɛ suban a obi de no fam ase na ɔnnyɛ ne ho kɛseɛ wɔ afoforo anim.",
        "Humility is the quality of behaving modestly and without excessive pride.",
        "Akan asetena mu ahobrɛaseɛ taa ne obu, ntie ne nkitahodie pa bom.",
        ["Ahobrɛaseɛ boa ma nnipa tena asomdwoeɛ mu."],
        ["Humility can support peaceful relationships."],
        ["ahobrɛaseɛ", "brɛ wo ho ase", "obu"],
        ["humility", "modesty", "respect"],
        [
            "Dɛn ne ahobrɛaseɛ?",
            "Dɛn nti na ahobrɛaseɛ ho hia?",
        ],
    ),

    make_item(
        "Ayɔnkofa",
        "Social relationship",
        "social values",
        "Ayɔnkofa yɛ nkitahodie a ɛda nnipa anaa abusuafoɔ ntam.",
        "Ayɔnkofa refers to relationships and social connections between people.",
        "Akan asetena mu ayɔnkofa betumi akɔ so wɔ abusua, mpɔtam, awareɛ ne adamfoɔsɛm mu.",
        ["Ayɔnkofa pa boa ma mpɔtam no yɛ baako."],
        ["Good social relationships help communities remain united."],
        ["ayɔnkofa", "nkitahodie", "adamfoɔsɛm"],
        ["relationship", "social connection", "friendship"],
        [
            "Dɛn ne ayɔnkofa?",
            "Dɛn na ɛma ayɔnkofa yɛ den?",
        ],
    ),

    make_item(
        "Tie mpanyimfoɔ",
        "Listening to elders",
        "elders and respect",
        "Tie mpanyimfoɔ yɛ suban a mmofra anaa nkurɔfoɔ tie afotuo ne nsɛm a mpanyimfoɔ ka.",
        "Listening to elders refers to paying attention to the advice and guidance of respected senior people.",
        "Wɔ Akan asetena mu no, tie ne ntieɛ betumi ayɛ ɔkwan a wɔfa so sua nyansa ne osuahunu.",
        ["Abofra tie ne panyin afotuo."],
        ["A child listens to an elder's advice."],
        ["tie mpanyimfoɔ", "afotuo", "mpanyimfoɔ"],
        ["listening to elders", "elder guidance", "respect"],
        [
            "Dɛn nti na tie mpanyimfoɔ ho hia?",
            "Dɛn na mmofra sua firi mpanyimfoɔ hɔ?",
        ],
    ),

    # ========================================================
    # 4. CHIEFTAINCY AND TRADITIONAL LEADERSHIP
    # ========================================================

    make_item(
        "Ahennie",
        "Chieftaincy",
        "traditional leadership",
        "Ahennie yɛ Akan amammerɛ mu nhyehyɛeɛ a ɛfa ahemfoɔ ne mpanyimfoɔ sohwɛ ho.",
        "Chieftaincy is a traditional leadership institution involving chiefs and elders.",
        "Ahennie wɔ dwuma wɔ amammerɛ, afotuo, mpɔtam mu asomdwoeɛ ne amanneɛ mu.",
        ["Ɔhene ne mpanyimfoɔ boa ma wɔhwɛ mpɔtam no nsɛm so."],
        ["The chief and elders help oversee community affairs."],
        ["ahennie", "ɔhene", "ahemfoɔ"],
        ["chieftaincy", "traditional leadership", "chief"],
        [
            "Dɛn ne ahennie?",
            "Dɛn ne ɔhene dwuma?",
            "What is Akan chieftaincy?",
        ],
    ),

    make_item(
        "Ɔhene",
        "Chief",
        "traditional leadership",
        "Ɔhene yɛ ɔbarima a ɔdi mpɔtam anaa amanneɛ mu ahennie dwuma wɔ Akan amammerɛ mu.",
        "A chief is a male traditional leader within an Akan traditional community.",
        "Ɔhene ne mpanyimfoɔ yɛ adwuma bom wɔ amanneɛ, afotuo ne mpɔtam mu nsɛm ho.",
        ["Ɔhene ne mpanyimfoɔ hyia di mpɔtam no nsɛm ho dwuma."],
        ["The chief and elders meet to discuss community matters."],
        ["ɔhene", "hene", "ahennie"],
        ["chief", "Akan chief", "traditional ruler"],
        [
            "Hwan ne ɔhene?",
            "Dɛn ne ɔhene dwuma?",
        ],
    ),

    make_item(
        "Ɔbaahemaa",
        "Queenmother",
        "traditional leadership",
        "Ɔbaahemaa yɛ ɔbaa a ɔwɔ dwuma titire wɔ Akan amammerɛ mu ahennie anaa mpɔtam mu.",
        "A queenmother is a female traditional leader with important community and cultural responsibilities.",
        "Ɔbaahemaa betumi de afotuo ama mpɔtam no na wadi mmea ne mmofra ho nsɛm anim.",
        ["Ɔbaahemaa de afotuo ma mpɔtam no."],
        ["The queenmother advises the community."],
        ["ɔbaahemaa", "ahemmaa", "ɔbaa panyin"],
        ["queenmother", "female traditional leader"],
        [
            "Dɛn ne ɔbaahemaa?",
            "Dɛn ne ɔbaahemaa dwuma?",
        ],
    ),

    make_item(
        "Mpanyimfoɔ ahemfie",
        "Council of elders",
        "traditional leadership",
        "Mpanyimfoɔ ahemfie yɛ mpanyimfoɔ a wɔboa ɔhene wɔ mpɔtam mu nsɛm ne afotuo mu.",
        "A council of elders is a group of respected elders who advise traditional leadership.",
        "Mpanyimfoɔ betumi de osuahunu ne amanneɛ ho nimdeɛ aboa ma wɔsi gyinaeɛ.",
        ["Mpanyimfoɔ de afotuo ma ɔhene."],
        ["Elders advise the chief."],
        ["mpanyimfoɔ", "ahemfie", "afotuo"],
        ["council of elders", "elders council", "traditional council"],
        [
            "Dɛn ne mpanyimfoɔ ahemfie?",
            "Dɛn ne mpanyimfoɔ dwuma wɔ ahennie mu?",
        ],
    ),

    make_item(
        "Ahemfie",
        "Traditional palace",
        "traditional leadership",
        "Ahemfie yɛ beaeɛ a ɔhene ne ne mpanyimfoɔ di amammerɛ mu dwuma na wɔdi mpɔtam nsɛm ho nkɔmmɔ.",
        "Ahemfie is a traditional palace or royal setting associated with the chief and traditional leadership.",
        "Ahemfie betumi ayɛ beaeɛ a amanneɛ, afotuo ne mpɔtam mu nhyiamɔ kɔ so.",
        ["Mpɔtamfoɔ hyia wɔ ahemfie wɔ dwumadie bi ase."],
        ["Community members may gather at the palace for cultural activities."],
        ["ahemfie", "ɔhene", "ahennie"],
        ["traditional palace", "chief's palace", "royal setting"],
        [
            "Dɛn ne ahemfie?",
            "Dɛn na wɔyɛ wɔ ahemfie?",
        ],
    ),

    # ========================================================
    # 5. FESTIVALS
    # ========================================================

    make_item(
        "Afahyɛ",
        "Festival",
        "festivals",
        "Afahyɛ yɛ amammerɛ mu dwumadie a wɔyɛ de kae abakɔsɛm, nyameaseda anaa adeɛ titire.",
        "A festival is a cultural occasion held for remembrance, thanksgiving, or an important purpose.",
        "Afahyɛ ma mpɔtamfoɔ hyia, yɛ amanneɛ na wɔhyɛ wɔn amammerɛ mu nkabom den.",
        ["Afahyɛ ma abusua ne mpɔtamfoɔ hyia."],
        ["Festivals bring families and communities together."],
        ["afahyɛ", "Akan afahyɛ", "afahyɛ ahodoɔ"],
        ["festival", "Akan festival", "cultural festival"],
        [
            "Dɛn ne afahyɛ?",
            "Dɛn nti na Akanfoɔ yɛ afahyɛ?",
        ],
    ),

    make_item(
        "Afahyɛ abakɔsɛm",
        "Historical purpose of festivals",
        "festivals",
        "Afahyɛ bi wɔ abakɔsɛm a ɛkyerɛ nea enti a mpɔtam bi fii ase yɛɛ afahyɛ no.",
        "Some festivals have historical origins explaining why communities established them.",
        "Afahyɛ betumi ama awoɔ ntoatoasoɔ foforɔ ate wɔn mpɔtam no abakɔsɛm.",
        ["Afahyɛ ma mmofra sua wɔn mpɔtam abakɔsɛm."],
        ["Festivals can help younger generations learn community history."],
        ["afahyɛ", "abakɔsɛm", "amammerɛ"],
        ["festival history", "historical tradition", "cultural history"],
        [
            "Dɛn nti na afahyɛ bi wɔ hɔ?",
            "How can festivals preserve history?",
        ],
    ),

    make_item(
        "Afahyɛ nkabom",
        "Community unity through festivals",
        "festivals",
        "Afahyɛ nkabom yɛ sɛnea afahyɛ boa ma abusua ne mpɔtamfoɔ hyia na wɔyɛ adeɛ bom.",
        "Festival solidarity refers to the way festivals encourage families and communities to unite.",
        "Afahyɛ ma nnipa a wɔte mmeaeɛ foforɔ betumi asan aba wɔn mpɔtam ahyia.",
        ["Nnipa a wɔatu akɔ baabi foforɔ betumi aba afahyɛ ase."],
        ["People who have moved elsewhere may return for festivals."],
        ["afahyɛ nkabom", "nkabom", "mpɔtam"],
        ["festival unity", "community unity"],
        [
            "Ɔkwan bɛn so na afahyɛ ma nkabom?",
        ],
    ),

    make_item(
        "Afahyɛ amanneɛ",
        "Festival customs",
        "festivals",
        "Afahyɛ amanneɛ yɛ nneyɛeɛ ne amanneɛ a wɔyɛ wɔ afahyɛ berɛ mu.",
        "Festival customs are practices and ceremonies carried out during a festival.",
        "Afahyɛ amanneɛ betumi ayɛ soronko wɔ mpɔtam ne afahyɛ ahodoɔ mu.",
        ["Afahyɛ amanneɛ bi ka nnwom ne asaw ho."],
        ["Some festival customs include music and dance."],
        ["afahyɛ amanneɛ", "afahyɛ", "amanneɛ"],
        ["festival customs", "festival traditions"],
        [
            "Dɛn ne afahyɛ amanneɛ?",
            "Dɛn na wɔyɛ wɔ afahyɛ ase?",
        ],
    ),

    # ========================================================
    # 6. NAMING TRADITIONS
    # ========================================================

    make_item(
        "Din to",
        "Naming ceremony",
        "naming traditions",
        "Din to yɛ amanneɛ a wɔde ma abofra din na wɔde no ba abusua ne mpɔtam mu.",
        "A naming ceremony is a traditional practice for formally giving a child a name and introducing the child to the community.",
        "Din ho hia wɔ Akan amammerɛ mu na ɛtumi ne awoɔ da, abusua ne abusua no anidasoɔ wɔ abofra no ho di nkitahodie.",
        ["Abusuafoɔ hyia wɔ din to ase."],
        ["Family members gather for a naming ceremony."],
        ["din to", "abofra din", "Akan din"],
        ["naming ceremony", "Akan naming", "child naming"],
        [
            "Dɛn ne din to?",
            "Dɛn nti na din ho hia?",
            "How are Akan children named?",
        ],
    ),

    make_item(
        "Awoɔ da din",
        "Day-of-birth name",
        "naming traditions",
        "Awoɔ da din yɛ din a ɛfa da a wɔwoo abofra no ho wɔ Akan amammerɛ mu.",
        "A day-of-birth name is a name associated with the day on which a child was born.",
        "Akan din ahodoɔ bi wɔ nkitahodie a ɛda wɔn awoɔ da ne din ntam.",
        ["Abusua betumi de awoɔ da adi dwuma wɔ abofra din mu."],
        ["A family may use the day of birth in naming a child."],
        ["awoɔ da", "din", "abofra din"],
        ["day-name", "birth-day name", "Akan day name"],
        [
            "Dɛn ne awoɔ da din?",
            "How does birth day relate to Akan naming?",
        ],
    ),

    make_item(
        "Abofra din",
        "Child's name",
        "naming traditions",
        "Abofra din yɛ din a abusua de frɛ abofra no na ɛma no nipasu wɔ ɔmanfoɔ mu.",
        "A child's name is the name by which the child is identified within family and society.",
        "Din betumi akyerɛ abusua, awoɔ da, anidasoɔ anaa asɛm bi a ɛfa n'awoɔ ho.",
        ["Abusua no paw abofra din wɔ amanneɛ mu."],
        ["The family chooses a child's name through a cultural process."],
        ["abofra din", "din", "Akan din"],
        ["child's name", "Akan name", "personal name"],
        [
            "Dɛn ne abofra din?",
            "Dɛn na Akan din betumi akyerɛ?",
        ],
    ),

    make_item(
        "Din ne abusua",
        "Name and family identity",
        "naming traditions",
        "Din ne abusua yɛ abusuabɔ a ɛda obi din ne abusua a ɔfiri mu ntam.",
        "Name and family identity describes the connection between a person's name and family identity.",
        "Akan din betumi ama obi ada abusua anaa amammerɛ mu nkitahodie adi.",
        ["Din bi betumi ama nnipa ahu abusua mu nkitahodie."],
        ["A name may reflect family or cultural connections."],
        ["din", "abusua", "nipasu"],
        ["name", "family identity", "personal identity"],
        [
            "Ɔkwan bɛn so na din ne abusua wɔ abusuabɔ?",
        ],
    ),

    # ========================================================
    # 7. MARRIAGE
    # ========================================================

    make_item(
        "Awareɛ",
        "Marriage",
        "marriage traditions",
        "Awareɛ yɛ ayɔnkofa a ɛka ɔbarima ne ɔbaa ne wɔn mmusua bom wɔ amanneɛ ne asɛyɛdeɛ mu.",
        "Marriage is a relationship connecting a man, woman, and their families through recognized social responsibilities.",
        "Akan awareɛ taa ka mmusua baanu bom na ɛwɔ afotuo ne amanneɛ.",
        ["Awareɛ ka mmusua baanu bom."],
        ["Marriage connects two families."],
        ["awareɛ", "aware", "awarefoɔ"],
        ["marriage", "Akan marriage", "marriage customs"],
        [
            "Dɛn ne Akan awareɛ?",
            "Akan awareɛ yɛ dɛn?",
        ],
    ),

    make_item(
        "Awareɛ amanneɛ",
        "Marriage customs",
        "marriage traditions",
        "Awareɛ amanneɛ yɛ nneyɛeɛ ne nhyehyɛeɛ a abusua de di awareɛ ho dwuma.",
        "Marriage customs are practices and procedures associated with marriage.",
        "Akan mpɔtam ahodoɔ betumi anya awareɛ amanneɛ a ɛsono wɔn ho wɔ mmeaeɛ ahodoɔ mu.",
        ["Awareɛ amanneɛ betumi ayɛ soronko wɔ abusua ahodoɔ mu."],
        ["Marriage customs can differ among communities and families."],
        ["awareɛ amanneɛ", "aware", "abusua"],
        ["marriage customs", "marriage traditions"],
        [
            "Dɛn ne awareɛ amanneɛ?",
            "How do Akan marriage customs differ?",
        ],
    ),

    make_item(
        "Awarefoɔ",
        "Married couple",
        "marriage traditions",
        "Awarefoɔ yɛ ɔbarima ne ɔbaa a wɔaware.",
        "A married couple refers to two people joined in marriage.",
        "Akan asetena mu awarefoɔ wɔ asɛyɛdeɛ wɔ wɔn ho wɔn ho ne wɔn mmusua anim.",
        ["Awarefoɔ nya asɛyɛdeɛ wɔ wɔn abusua anim."],
        ["Married couples have responsibilities toward their families."],
        ["awarefoɔ", "aware", "awareɛ"],
        ["married couple", "spouses"],
        [
            "Hwan ne awarefoɔ?",
            "Dɛn ne awarefoɔ asɛyɛdeɛ?",
        ],
    ),

    make_item(
        "Awareɛ ne abusua",
        "Marriage and family",
        "marriage traditions",
        "Awareɛ ne abusua yɛ abusuabɔ a ɛda awareɛ ne mmusua baanu a wɔde awareɛ ka wɔn ho ntam.",
        "Marriage and family describes the relationship between marriage and the families connected through it.",
        "Akan awareɛ betumi ama mmusua baanu anya nkitahodie foforɔ.",
        ["Awareɛ ma mmusua baanu nya ayɔnkofa."],
        ["Marriage can create relationships between two families."],
        ["awareɛ", "abusua", "awarefoɔ"],
        ["marriage", "family", "marriage and kinship"],
        [
            "Ɔkwan bɛn so na awareɛ ka mmusua bom?",
        ],
    ),

    # ========================================================
    # 8. FUNERAL TRADITIONS
    # ========================================================

    make_item(
        "Ayie",
        "Funeral",
        "funeral traditions",
        "Ayie yɛ amanneɛ a abusua ne mpɔtam yɛ de di awufoɔ ni na wɔkyerɛ awerɛhow.",
        "A funeral is a cultural ceremony for honouring the deceased and expressing grief.",
        "Ayie mu dwumadie betumi ayɛ soronko wɔ abusua ne mpɔtam ahodoɔ mu.",
        ["Abusuafoɔ hyia di awufoɔ ni."],
        ["Family members gather to honour the deceased."],
        ["ayie", "awufoɔ", "awerɛhow"],
        ["funeral", "Akan funeral", "funeral customs"],
        [
            "Dɛn ne ayie?",
            "Dɛn nti na Akanfoɔ yɛ ayie?",
        ],
    ),

    make_item(
        "Ayie nnwom",
        "Funeral songs",
        "funeral traditions",
        "Ayie nnwom yɛ nnwom a wɔto wɔ ayie mu de da awerɛhow, nkaeɛ anaa afotuo adi.",
        "Funeral songs are songs performed during funerals to express grief, remembrance, or reflection.",
        "Nnwom wɔ dwuma wɔ Akan ayie mu na ne nsɛm betumi ama nkurɔfoɔ asusuw ɔbra ne ɔwu ho.",
        ["Wɔto nnwom wɔ ayie ase."],
        ["Songs may be performed during funerals."],
        ["ayie nnwom", "nnwom", "ayie"],
        ["funeral songs", "mourning songs"],
        [
            "Dɛn ne ayie nnwom?",
            "Why are songs used at funerals?",
        ],
    ),

    make_item(
        "Awufoɔ nkaeɛ",
        "Remembrance of the deceased",
        "funeral traditions",
        "Awufoɔ nkaeɛ yɛ sɛnea abusua ne mpɔtam ka wɔn a wɔawuwu no ho asɛm na wɔkae wɔn abrabɔ.",
        "Remembrance of the deceased is the act of recalling and honouring those who have died.",
        "Nkaeɛ ma abusuafoɔ tumi ka ɔno a wawuo no suban, ne dwuma ne ne nkaeɛ ho asɛm.",
        ["Abusuafoɔ ka awufoɔ no ho nsɛm wɔ ayie mu."],
        ["Family members talk about the deceased during funeral activities."],
        ["awufoɔ nkaeɛ", "nkaeɛ", "ayie"],
        ["remembrance", "memory of deceased", "funeral remembrance"],
        [
            "Dɛn ne awufoɔ nkaeɛ?",
            "How are the deceased remembered?",
        ],
    ),

    make_item(
        "Ayie mu nkabom",
        "Community support during funerals",
        "funeral traditions",
        "Ayie mu nkabom yɛ sɛnea abusua ne mpɔtamfoɔ bom boa abusua a wɔayera wɔn dɔfoɔ.",
        "Funeral solidarity refers to the support families receive from relatives and community members during funerals.",
        "Nkabom betumi ada adi wɔ mmoa, adwuma, afotuo ne ɔkyɛfa mu.",
        ["Mpɔtamfoɔ boa abusua no wɔ ayie mu."],
        ["Community members support the family during a funeral."],
        ["ayie", "nkabom", "mmoa"],
        ["funeral support", "community support", "solidarity"],
        [
            "Ɔkwan bɛn so na mpɔtamfoɔ boa wɔ ayie mu?",
        ],
    ),

    # ========================================================
    # 9. FOOD AND CUISINE
    # ========================================================

    make_item(
        "Akan aduane",
        "Akan food",
        "food and cuisine",
        "Akan aduane yɛ nnuane ne nkyɛmu ahodoɔ a Akanfoɔ noa na wɔdi wɔ wɔn asetena mu.",
        "Akan food refers to traditional dishes and food practices associated with Akan communities.",
        "Akan aduane wɔ nsonsonoeɛ wɔ mpɔtam ahodoɔ mu na nnuane bi yɛ daa aduane.",
        ["Fufu ne nkwan yɛ aduane a nnipa pii di."],
        ["Fufu with soup is eaten by many people."],
        ["Akan aduane", "aduane", "nkwan"],
        ["Akan food", "traditional food", "Akan cuisine"],
        [
            "Dɛn ne Akan aduane?",
            "Akanfoɔ di aduane bɛn?",
        ],
    ),

    make_item(
        "Fufu",
        "Fufu",
        "food and cuisine",
        "Fufu yɛ aduane a wɔyɛ denam nnɔbaeɛ bi a wɔbɔ na wɔyam anaa wɔhyehyɛ so.",
        "Fufu is a traditional West African food prepared from starchy crops that are pounded or processed into a soft dough.",
        "Fufu taa ne nkwan di na nnuane a wɔde yɛ no betumi ayɛ soronko wɔ mpɔtam ahodoɔ mu.",
        ["Wɔtaa di fufu ne nkwan."],
        ["Fufu is often eaten with soup."],
        ["fufu", "aduane", "nkwan"],
        ["fufu", "traditional food", "Akan cuisine"],
        [
            "Dɛn ne fufu?",
            "Dɛn na wɔde fufu di?",
        ],
    ),

    make_item(
        "Ampesi",
        "Boiled plantain or yam meal",
        "food and cuisine",
        "Ampesi yɛ nnɔbaeɛ te sɛ borɔdeɛ anaa bayere a wɔanoa ma ɛyɛ aduane.",
        "Ampesi is a meal made from boiled starchy crops such as plantain or yam.",
        "Ampesi betumi ne nkwan, kontomire anaa aduanemmoa ahodoɔ adi.",
        ["Wɔde nkwan ne ampesi di."],
        ["Ampesi may be eaten with soup."],
        ["ampesi", "borɔdeɛ", "bayere"],
        ["ampesi", "boiled plantain", "boiled yam"],
        [
            "Dɛn ne ampesi?",
            "Dɛn na wɔde ampesi di?",
        ],
    ),

    make_item(
        "Kontomire",
        "Cocoyam leaves",
        "food and cuisine",
        "Kontomire yɛ nhaban a wɔde yɛ aduane wɔ Ghana ne Akan mpɔtam pii.",
        "Kontomire refers to cocoyam leaves commonly used in Ghanaian cuisine.",
        "Wɔde kontomire yɛ nkwan ne nnuane ahodoɔ.",
        ["Wɔde kontomire yɛ aduane."],
        ["Cocoyam leaves are used to prepare food."],
        ["kontomire", "nhaban", "aduane"],
        ["cocoyam leaves", "food", "traditional cuisine"],
        [
            "Dɛn ne kontomire?",
            "Ɔkwan bɛn so na wɔde kontomire yɛ aduane?",
        ],
    ),

    make_item(
        "Bankye",
        "Cassava",
        "food and agriculture",
        "Bankye yɛ nnɔbaeɛ a wɔdua na wɔde yɛ nnuane ahodoɔ.",
        "Cassava is a root crop cultivated and used to prepare various foods.",
        "Bankye betumi ayɛ fufu, gari ne nnuane foforɔ mu adeɛ.",
        ["Wɔdua bankye de yɛ aduane."],
        ["Cassava is grown and used in food preparation."],
        ["bankye", "nnɔbaeɛ", "aduane"],
        ["cassava", "crop", "food"],
        [
            "Dɛn ne bankye?",
            "Dɛn na wɔde bankye yɛ?",
        ],
    ),

    # ========================================================
    # 10. CLOTHING AND TEXTILES
    # ========================================================

    make_item(
        "Kente",
        "Kente",
        "clothing and textiles",
        "Kente yɛ ntoma a wɔnwene no kwan soronko mu na ɛwɔ amammerɛ mu nteaseɛ.",
        "Kente is a traditionally woven textile associated with Akan and other West African traditions.",
        "Kente wɔ nsusuiɛ ne kɔla ahodoɔ na wɔtaa de no yɛ ntadeɛ ma dwumadie titire.",
        ["Wɔtaa de kente yɛ ntadeɛ wɔ afahyɛ ase."],
        ["Kente is often worn during festivals."],
        ["kente", "ntoma", "nsusuiɛ"],
        ["Kente", "Kente cloth", "traditional textile"],
        [
            "Dɛn ne kente?",
            "Dɛn nti na kente ho hia?",
        ],
    ),

    make_item(
        "Ntoma",
        "Cloth or textile",
        "clothing and textiles",
        "Ntoma yɛ adeɛ a wɔnwene anaa wɔyɛ no de kata nipadua anaa yɛ ntadeɛ.",
        "Cloth is a woven or manufactured textile used for clothing and other purposes.",
        "Ntoma wɔ dwuma wɔ Akan amammerɛ mu wɔ ntadeɛ, afahyɛ ne amanneɛ mu.",
        ["Wɔde ntoma yɛ ntadeɛ."],
        ["Cloth is used to make clothing."],
        ["ntoma", "ntadeɛ", "kente"],
        ["cloth", "textile", "fabric"],
        [
            "Dɛn ne ntoma?",
            "Dɛn na wɔde ntoma yɛ?",
        ],
    ),

    make_item(
        "Ntadeɛ",
        "Clothing",
        "clothing and textiles",
        "Ntadeɛ yɛ nneɛma a nnipa hyɛ de kata wɔn nipadua.",
        "Clothing refers to garments worn to cover the body.",
        "Akan ntadeɛ betumi ayɛ daa ntadeɛ anaa amammerɛ mu ntadeɛ a wɔhyɛ wɔ dwumadie titire ase.",
        ["Nnipa hyɛ ntadeɛ wɔ afahyɛ ase."],
        ["People wear traditional clothing during festivals."],
        ["ntadeɛ", "ntoma", "kente"],
        ["clothing", "traditional clothing", "garments"],
        [
            "Dɛn ne ntadeɛ?",
            "Akanfoɔ hyɛ ntadeɛ bɛn?",
        ],
    ),

    make_item(
        "Kente nwene",
        "Kente weaving",
        "clothing and textiles",
        "Kente nwene yɛ adwuma a wɔde nhama ne nwene mfiri anaa nnwinnadeɛ yɛ kente ntoma.",
        "Kente weaving is the craft of producing Kente cloth through weaving techniques.",
        "Kente nwene hia nimdeɛ, ntoboaseɛ ne nsusuiɛ ho nteaseɛ.",
        ["Ɔnwenefoɔ nwene kente."],
        ["A weaver produces Kente cloth."],
        ["kente nwene", "ɔnwenefoɔ", "kente"],
        ["Kente weaving", "weaving", "textile craft"],
        [
            "Dɛn ne kente nwene?",
            "Hwan na ɔnwene kente?",
        ],
    ),

    # ========================================================
    # 11. ADINKRA AND SYMBOLS
    # ========================================================

    make_item(
        "Adinkra",
        "Adinkra symbols",
        "symbols and visual culture",
        "Adinkra yɛ nsɛnkyerɛnneɛ a wɔde nsusuiɛ so kyerɛ nyansa, gyinapɛn ne asetena mu nsɛm.",
        "Adinkra refers to visual symbols used to communicate ideas, values, wisdom, and cultural concepts.",
        "Adinkra nsɛnkyerɛnneɛ wɔ nkyerɛaseɛ ahodoɔ na wɔtaa hu wɔ ntoma ne nneɛma foforɔ so.",
        ["Wɔde Adinkra nsɛnkyerɛnneɛ gu ntoma so."],
        ["Adinkra symbols are placed on cloth."],
        ["Adinkra", "nsɛnkyerɛnneɛ", "Adinkra nsusuiɛ"],
        ["Adinkra", "Adinkra symbols", "Akan symbols"],
        [
            "Dɛn ne Adinkra?",
            "Dɛn na Adinkra nsɛnkyerɛnneɛ kyerɛ?",
        ],
    ),

    make_item(
        "Adinkra nsɛnkyerɛnneɛ",
        "Adinkra symbols",
        "symbols and visual culture",
        "Adinkra nsɛnkyerɛnneɛ yɛ nsɛnkyerɛnneɛ ahodoɔ a wɔde kyerɛ adwene anaa gyinapɛn bi.",
        "Adinkra symbols are visual signs used to represent particular ideas or values.",
        "Nsɛnkyerɛnneɛ bi betumi ne nyansa, asomdwoeɛ, nkabom anaa ahobrɛaseɛ ayɛ adwene.",
        ["Adinkra nsɛnkyerɛnneɛ bi kyerɛ nyansa."],
        ["Some Adinkra symbols communicate wisdom."],
        ["Adinkra", "nsɛnkyerɛnneɛ", "nyansa"],
        ["Adinkra symbols", "visual symbols", "cultural symbols"],
        [
            "Dɛn ne Adinkra nsɛnkyerɛnneɛ?",
            "Dɛn na Adinkra kyerɛ?",
        ],
    ),

    make_item(
        "Nsɛnkyerɛnneɛ",
        "Symbol",
        "symbols and visual culture",
        "Nsɛnkyerɛnneɛ yɛ agyiraeɛ anaa mfoni a ɛgyina hɔ ma adwene, adeɛ anaa nkyerɛaseɛ bi.",
        "A symbol is a sign or visual representation that stands for an idea, thing, or meaning.",
        "Adinkra yɛ nhwɛsoɔ a ɛkyerɛ sɛ nsɛnkyerɛnneɛ betumi de adwene adi nkitaho.",
        ["Nsɛnkyerɛnneɛ bi wɔ nkyerɛaseɛ."],
        ["A symbol may carry a particular meaning."],
        ["nsɛnkyerɛnneɛ", "Adinkra", "agyiraeɛ"],
        ["symbol", "sign", "visual representation"],
        [
            "Dɛn ne nsɛnkyerɛnneɛ?",
            "Dɛn nti na nsɛnkyerɛnneɛ ho hia?",
        ],
    ),

    # ========================================================
    # 12. ORAL TRADITION
    # ========================================================

    make_item(
        "Anansesɛm",
        "Ananse stories",
        "oral tradition",
        "Anansesɛm yɛ Akan amammerɛ mu anansesɛm a wɔde Ananse, nnipa anaa mmoa ho nsɛm kyerɛkyerɛ.",
        "Anansesɛm are Akan oral stories often involving Ananse, people, or animals.",
        "Anansesɛm taa wɔ adesua, afotuo anaa nyansa bi wɔ mu.",
        ["Mpanyimfoɔ ka anansesɛm kyerɛ mmofra."],
        ["Elders tell Ananse stories to children."],
        ["anansesɛm", "Ananse", "anansesɛm ka"],
        ["Ananse stories", "Akan folktales", "oral storytelling"],
        [
            "Dɛn ne anansesɛm?",
            "Dɛn nti na Akanfoɔ ka anansesɛm?",
        ],
    ),

    make_item(
        "Ananse",
        "Ananse",
        "oral tradition",
        "Ananse yɛ akyekyedeɛ a ɔwɔ dwuma titire wɔ Akan anansesɛm mu.",
        "Ananse is a spider character prominent in Akan storytelling traditions.",
        "Ananse ho nsɛm pii de nyansa, anifere, ɔbrasɛeɛ ne asetenam adesua kyerɛ.",
        ["Ananse yɛ onipa titire wɔ anansesɛm pii mu."],
        ["Ananse is a central character in many folktales."],
        ["Ananse", "anansesɛm", "akyekyedeɛ"],
        ["Ananse", "spider character", "folktale character"],
        [
            "Hwan ne Ananse?",
            "Dɛn nti na Ananse wɔ anansesɛm mu?",
        ],
    ),

    make_item(
        "Anansesɛm ka",
        "Storytelling",
        "oral tradition",
        "Anansesɛm ka yɛ sɛnea wɔka anansesɛm kyerɛ afoforo de ma wɔnya anigyeɛ ne adesua.",
        "Storytelling is the practice of telling stories for entertainment, education, and cultural transmission.",
        "Mpanyimfoɔ betumi aka anansesɛm akyerɛ mmofra ma wɔasua suban ne nyansa.",
        ["Mpanyimfoɔ ka anansesɛm anwummere."],
        ["Elders may tell stories in the evening."],
        ["anansesɛm ka", "anansesɛm", "mpanyimfoɔ"],
        ["storytelling", "oral storytelling", "folktales"],
        [
            "Dɛn ne anansesɛm ka?",
            "Dɛn nti na storytelling ho hia?",
        ],
    ),

    make_item(
        "Anansesɛm mu adesua",
        "Lessons in folktales",
        "oral tradition",
        "Anansesɛm mu adesua yɛ nyansa ne afotuo a wɔnya firi anansesɛm mu.",
        "Lessons in folktales are the wisdom and guidance communicated through traditional stories.",
        "Anansesɛm betumi akyerɛ mmofra nokware, nyansa, ntoboaseɛ ne ɔbra pa.",
        ["Mmofra nya adesua firi anansesɛm mu."],
        ["Children can learn lessons from folktales."],
        ["anansesɛm", "adesua", "afotuo"],
        ["folktale lessons", "moral lessons", "story lessons"],
        [
            "Dɛn na yɛsua firi anansesɛm mu?",
        ],
    ),

    # ========================================================
    # 13. PROVERBS
    # ========================================================

    make_item(
        "Mmebusɛm",
        "Akan proverbs",
        "oral tradition",
        "Mmebusɛm yɛ nsɛm tiawa a wɔde nyansa ne asetena mu nokware bi kyerɛ.",
        "Akan proverbs are concise expressions used to communicate wisdom and life lessons.",
        "Mmebusɛm wɔ dwuma wɔ afotuo, ɔkasa, asɛnka ne nkitahodie mu.",
        ["Mpanyimfoɔ de mmebusɛm ma afotuo."],
        ["Elders use proverbs to give advice."],
        ["mmebusɛm", "bɛ", "nyansa nsɛm"],
        ["Akan proverbs", "proverbs", "wisdom sayings"],
        [
            "Dɛn ne mmebusɛm?",
            "Dɛn nti na mmebusɛm ho hia?",
        ],
    ),

    make_item(
        "Bɛ",
        "Proverb",
        "oral tradition",
        "Bɛ yɛ asɛm tiawa a ɛwɔ nkyerɛaseɛ anaa nyansa a wɔde kyerɛ adwene bi.",
        "A proverb is a short expression carrying a lesson or wisdom.",
        "Bɛ betumi ama ɔkasafoɔ ada asɛm tenten bi adi wɔ nsɛm kakraa bi mu.",
        ["Ɔpanyin de bɛ maa mmofra."],
        ["The elder used a proverb when advising the children."],
        ["bɛ", "mmebusɛm", "nyansa"],
        ["proverb", "wisdom saying"],
        [
            "Dɛn ne bɛ?",
            "Dɛn na bɛ kyerɛ?",
        ],
    ),

    make_item(
        "Mmebusɛm ne nyansa",
        "Proverbs and wisdom",
        "oral tradition",
        "Mmebusɛm ne nyansa yɛ abusuabɔ a ɛda Akan mmebusɛm ne asetena mu nyansa ntam.",
        "Proverbs and wisdom describes how proverbs communicate lessons and practical wisdom.",
        "Mpanyimfoɔ de mmebusɛm tumi kyerɛ adwene bi a anka ɛbɛhia nsɛm pii.",
        ["Mmebusɛm tumi kyerɛ nyansa wɔ nsɛm tiawa mu."],
        ["Proverbs can express wisdom in short statements."],
        ["mmebusɛm", "nyansa", "bɛ"],
        ["proverbs", "wisdom", "life lessons"],
        [
            "Ɔkwan bɛn so na mmebusɛm kyerɛ nyansa?",
        ],
    ),

    # ========================================================
    # 14. MUSIC AND DANCE
    # ========================================================

    make_item(
        "Akan nnwom",
        "Akan music",
        "music and dance",
        "Akan nnwom yɛ nnwom a wɔde nne, ntintim ne amammerɛ mu nsɛm ka.",
        "Akan music includes musical traditions using voice, rhythm, instruments, and cultural themes.",
        "Nnwom wɔ dwuma wɔ afahyɛ, ayie, awareɛ, ɔsom ne anigyeɛ mu.",
        ["Wɔto nnwom wɔ afahyɛ ase."],
        ["People sing during festivals."],
        ["Akan nnwom", "nnwom", "ntintim"],
        ["Akan music", "traditional music", "songs"],
        [
            "Dɛn ne Akan nnwom?",
            "Ɛhe na Akanfoɔ de nnwom di dwuma?",
        ],
    ),

    make_item(
        "Asaw",
        "Traditional dance",
        "music and dance",
        "Asaw yɛ nipadua mu nkitahodie a wɔde nnwom ne ntintim ka ho.",
        "Traditional dance is cultural expression through body movement, rhythm, and music.",
        "Akan asaw betumi ayɛ afahyɛ, ayie, awareɛ anaa anigyeɛ mu dwumadie.",
        ["Wɔasaw wɔ afahyɛ ase."],
        ["People dance during festivals."],
        ["asaw", "Akan asaw", "nnwom"],
        ["traditional dance", "Akan dance", "dance"],
        [
            "Dɛn ne asaw?",
            "Dɛn nti na Akanfoɔ asaw?",
        ],
    ),

    make_item(
        "Ntwom",
        "Rhythm or drumming pattern",
        "music and dance",
        "Ntwom yɛ ntintim anaa nnwom mu nhyehyɛeɛ a ɛma nnyegyeeɛ di akyi wɔ bere ne nhyehyɛeɛ mu.",
        "Rhythm refers to the organized pattern of beats in music or drumming.",
        "Ntintim ne asaw taa di akɔnnɔ wɔ amammerɛ mu dwumadie mu.",
        ["Ntintim ma asaw nya nhyehyɛeɛ."],
        ["Rhythm gives structure to dance."],
        ["ntwom", "ntintim", "nnwom"],
        ["rhythm", "drumming pattern", "musical rhythm"],
        [
            "Dɛn ne ntwom?",
            "Dɛn ne ntintim dwuma?",
        ],
    ),

    make_item(
        "Ntintim",
        "Drumming",
        "music and dance",
        "Ntintim yɛ nnwinnadeɛ a wɔde wɔn nsa anaa nnwinnadeɛ foforɔ bɔ de yɛ nnyegyeeɛ.",
        "Drumming is the practice of producing rhythmic sounds with drums or related instruments.",
        "Ntintim yɛ Akan amammerɛ mu nnwom ne asaw ho adeɛ a ɛho hia wɔ dwumadie pii mu.",
        ["Wɔbɔ mpintin wɔ afahyɛ ase."],
        ["Drums may be played during festivals."],
        ["ntintim", "mpintin", "nnwom"],
        ["drumming", "drums", "rhythm"],
        [
            "Dɛn ne ntintim?",
            "Dɛn nti na ntintim ho hia?",
        ],
    ),

    # ========================================================
    # 15. GREETINGS AND SOCIAL ETIQUETTE
    # ========================================================

    make_item(
        "Nkyea",
        "Greetings",
        "social etiquette",
        "Nkyea yɛ kasa ne nneyɛeɛ a wɔde kyerɛ obu, anigyeɛ ne ɔmanfoɔ ho anigyeɛ bere a wɔhyia.",
        "Greetings are verbal and social expressions showing respect, acknowledgement, and goodwill.",
        "Nkyea ho hia wɔ Akan asetena mu na mmofra sua sɛ wɔnkyea mpanyimfoɔ.",
        ["Abofra kyea ne panyin."],
        ["A child greets an elder."],
        ["nkyea", "kyea", "Akan nkyea"],
        ["greetings", "Akan greetings", "social etiquette"],
        [
            "Dɛn ne nkyea?",
            "Dɛn nti na nkyea ho hia?",
        ],
    ),

    make_item(
        "Kyea",
        "To greet",
        "social etiquette",
        "Kyea yɛ sɛ obi de kasa anaa nneyɛeɛ kyerɛ sɛ wahu obi na obu no.",
        "To greet is to acknowledge another person respectfully when meeting them.",
        "Akanfoɔ taa bu nkyea sɛ ɛyɛ nkitahodie pa no mfitiaseɛ.",
        ["Abofra kyea mpanyimfoɔ."],
        ["A child greets elders."],
        ["kyea", "nkyea", "obu"],
        ["greet", "greeting", "respect"],
        [
            "Dɛn ne kyea?",
            "Ɔkwan bɛn so na wɔkyea mpanyimfoɔ?",
        ],
    ),

    make_item(
        "Ahɔhoyɛ",
        "Hospitality",
        "social etiquette",
        "Ahɔhoyɛ yɛ suban a obi de gye ahɔhoɔ na ɔma wɔte nka sɛ wɔagye wɔn atom.",
        "Hospitality is the practice of welcoming and treating guests kindly.",
        "Ahɔhoyɛ yɛ suban a ɛboa ma ayɔnkofa ne nkitahodie yɛ den.",
        ["Abusua no gye ahɔhoɔ fɛw so."],
        ["The family welcomes guests warmly."],
        ["ahɔhoyɛ", "ahɔhoɔ", "gye ahɔhoɔ"],
        ["hospitality", "welcome", "guest care"],
        [
            "Dɛn ne ahɔhoyɛ?",
            "Dɛn nti na ahɔhoyɛ ho hia?",
        ],
    ),

    make_item(
        "Ahɔhoɔ gye",
        "Welcoming guests",
        "social etiquette",
        "Ahɔhoɔ gye yɛ ɔkwan a wɔfa so ma ahɔhoɔ te nka sɛ wɔagye wɔn atom.",
        "Welcoming guests refers to practices used to make visitors feel accepted and comfortable.",
        "Ahɔhoɔ gye betumi ayɛ nkyea, nkɔmmɔ, aduane anaa mmoa.",
        ["Abusua no gye ahɔhoɔ fɛw so."],
        ["The family welcomes guests warmly."],
        ["ahɔhoɔ", "gye", "ahɔhoyɛ"],
        ["welcoming guests", "hospitality", "guest welcome"],
        [
            "Ɔkwan bɛn so na Akanfoɔ gye ahɔhoɔ?",
        ],
    ),

    # ========================================================
    # 16. COMMUNITY LIFE
    # ========================================================

    make_item(
        "Nkabom",
        "Community solidarity",
        "community life",
        "Nkabom yɛ nnipa a wɔbom yɛ adwuma, boa wɔn ho na wɔdi wɔn botaeɛ ho dwuma.",
        "Community solidarity is people working together and supporting one another for shared goals.",
        "Nkabom ho hia wɔ ayie, awareɛ, afahyɛ ne mpɔtam mu nsɛnnennen mu.",
        ["Mpɔtamfoɔ boa wɔn ho wɔ ayie ase."],
        ["Community members support one another during funerals."],
        ["nkabom", "mpɔtam nkabom", "boa wɔn ho"],
        ["community solidarity", "communal life", "cooperation"],
        [
            "Dɛn ne nkabom?",
            "Dɛn nti na nkabom ho hia?",
        ],
    ),

    make_item(
        "Boa wɔn ho",
        "Mutual support",
        "community life",
        "Boa wɔn ho yɛ sɛ nnipa boa wɔn ho wɔ asɛyɛdeɛ, ɔhaw anaa botaeɛ bi ho.",
        "Mutual support means people helping one another with responsibilities, difficulties, or shared goals.",
        "Akan mpɔtam mu nnipa betumi aboaboa wɔn ano de boa abusua anaa mpɔtamfoɔ.",
        ["Nkurɔfoɔ boa wɔn ho wɔ adwuma mu."],
        ["People help one another with work."],
        ["boa wɔn ho", "nkabom", "ɔboa"],
        ["mutual support", "helping one another", "cooperation"],
        [
            "Dɛn ne boa wɔn ho?",
            "Ɔkwan bɛn so na Akanfoɔ boa wɔn ho?",
        ],
    ),

    make_item(
        "Mpɔtam",
        "Community",
        "community life",
        "Mpɔtam yɛ beaeɛ a nnipa tena na wɔne wɔn ho wɔn ho di nkitaho wɔ asetena mu.",
        "A community is a place or social group where people live and interact.",
        "Mpɔtam mu asetena ka abusua, adwuma, amanneɛ ne nkabom ho.",
        ["Mpɔtamfoɔ hyia wɔ mpɔtam dwumadie ase."],
        ["Community members gather for community activities."],
        ["mpɔtam", "mpɔtamfoɔ", "asetena"],
        ["community", "neighborhood", "community life"],
        [
            "Dɛn ne mpɔtam?",
            "Dɛn ne mpɔtamfoɔ dwuma?",
        ],
    ),

    make_item(
        "Mpɔtamfoɔ",
        "Community members",
        "community life",
        "Mpɔtamfoɔ yɛ nnipa a wɔte mpɔtam baako anaa wɔka mpɔtam no ho.",
        "Community members are people who live in or belong to a community.",
        "Mpɔtamfoɔ betumi ayɛ adwuma bom wɔ nneɛma a ɛfa wɔn mpɔtam ho.",
        ["Mpɔtamfoɔ yɛ adwuma bom."],
        ["Community members work together."],
        ["mpɔtamfoɔ", "mpɔtam", "nkabom"],
        ["community members", "residents", "community"],
        [
            "Hwan ne mpɔtamfoɔ?",
            "Dɛn na mpɔtamfoɔ yɛ?",
        ],
    ),

    # ========================================================
    # 17. TRADITIONAL EDUCATION
    # ========================================================

    make_item(
        "Asetena mu adesua",
        "Traditional education",
        "traditional education",
        "Asetena mu adesua yɛ nimdeɛ ne suban a mmofra sua firi abusua, mpanyimfoɔ, adwuma ne asetena mu.",
        "Traditional education refers to knowledge, skills, and values learned through family, elders, work, stories, and community life.",
        "Akanfoɔ tete mu adesua nyɛ sukuu dan mu adesua nko.",
        ["Mmofra sua adwuma firi wɔn awofoɔ hɔ."],
        ["Children learn skills from their parents."],
        ["asetena mu adesua", "tete adesua", "mpanyimfoɔ adesua"],
        ["traditional education", "indigenous education", "Akan education"],
        [
            "Dɛn ne Akan tete adesua?",
            "Ɔkwan bɛn so na Akanfoɔ tete kyerɛkyerɛ mmofra?",
        ],
    ),

    make_item(
        "Awofoɔ adesua",
        "Parental teaching",
        "traditional education",
        "Awofoɔ adesua yɛ sɛnea awofoɔ de wɔn nimdeɛ ne osuahunu kyerɛkyerɛ wɔn mma.",
        "Parental teaching is the passing of knowledge and experience from parents to children.",
        "Awofoɔ tumi kyerɛ mmofra kasa, adwuma, obu, ahobrɛaseɛ ne asetena mu nyansa.",
        ["Awofoɔ kyerɛkyerɛ wɔn mma suban pa."],
        ["Parents teach their children good behaviour."],
        ["awofoɔ", "adesua", "mmofra"],
        ["parental teaching", "family education", "child education"],
        [
            "Dɛn ne awofoɔ adesua?",
            "Dɛn na awofoɔ kyerɛ mmofra?",
        ],
    ),

    make_item(
        "Mpanyimfoɔ afotuo",
        "Elders' advice",
        "traditional education",
        "Mpanyimfoɔ afotuo yɛ afotuo a mpanyimfoɔ de wɔn osuahunu ne nyansa ma mmofra anaa mpɔtamfoɔ.",
        "Elders' advice is guidance based on the experience and wisdom of older community members.",
        "Afotuo yɛ ɔkwan a wɔfa so de nimdeɛ kɔ awoɔ ntoatoasoɔ so.",
        ["Mpanyimfoɔ de afotuo ma mmofra."],
        ["Elders give advice to younger people."],
        ["mpanyimfoɔ afotuo", "afotuo", "nyansa"],
        ["elders' advice", "guidance", "wisdom"],
        [
            "Dɛn ne mpanyimfoɔ afotuo?",
            "Dɛn nti na mpanyimfoɔ afotuo ho hia?",
        ],
    ),

    make_item(
        "Adwuma mu adesua",
        "Learning through work",
        "traditional education",
        "Adwuma mu adesua yɛ nimdeɛ ne ahokeka a obi nya denam adwuma a ɔyɛ so.",
        "Learning through work is the acquisition of knowledge and practical skills through doing work.",
        "Tete Akan asetena mu no, mmofra betumi asua nnwuma bi denam wɔn awofoɔ anaa mpanyimfoɔ a wɔhwɛ wɔn so no so.",
        ["Abofra sua adwuma denam ɔhwɛ ne ɔyɛ so."],
        ["A child can learn a skill by observing and practising it."],
        ["adwuma mu adesua", "adesua", "adwuma"],
        ["learning through work", "practical learning", "apprenticeship"],
        [
            "Dɛn ne adwuma mu adesua?",
            "Ɔkwan bɛn so na nnipa sua adwuma?",
        ],
    ),

    # ========================================================
    # 18. OCCUPATIONS
    # ========================================================

    make_item(
        "Kuadwuma",
        "Farming",
        "traditional occupations",
        "Kuadwuma yɛ asase so adwuma a wɔyɛ de dua nnɔbaeɛ na nya nnuane anaa sika.",
        "Farming is the cultivation of land to produce crops for food, trade, or other purposes.",
        "Kuadwuma yɛ adwuma a ɛho hia wɔ mpɔtam pii na ɛma abusua nya nnuane.",
        ["Ɔkuafoɔ dua bankye."],
        ["A farmer grows cassava."],
        ["kuadwuma", "ɔkuafoɔ", "kuayɛ"],
        ["farming", "agriculture", "farmer"],
        [
            "Dɛn ne kuadwuma?",
            "Dɛn nti na kuadwuma ho hia?",
        ],
    ),

    make_item(
        "Ɔkuafoɔ",
        "Farmer",
        "traditional occupations",
        "Ɔkuafoɔ yɛ obi a ɔyɛ kuadwuma de dua nnɔbaeɛ anaa yɛ nneɛma a ɛfa kuayɛ ho.",
        "A farmer is a person who cultivates land or engages in agricultural activities.",
        "Ɔkuafoɔ betumi dua nnɔbaeɛ ahodoɔ a abusua ne mpɔtam de di anaa wɔtɔn.",
        ["Ɔkuafoɔ dua nnɔbaeɛ wɔ ne kurom."],
        ["The farmer grows crops in the community."],
        ["ɔkuafoɔ", "kuadwuma", "kuayɛ"],
        ["farmer", "agricultural worker", "agriculture"],
        [
            "Hwan ne ɔkuafoɔ?",
            "Dɛn na ɔkuafoɔ yɛ?",
        ],
    ),

    make_item(
        "Adwumayɛ",
        "Work and occupation",
        "traditional occupations",
        "Adwumayɛ yɛ dwumadie a obi yɛ de nya nea ɔhia anaa di botaeɛ bi ho dwuma.",
        "Work refers to activities or occupations performed to meet needs or achieve purposes.",
        "Akan asetena mu adwumayɛ wɔ nkitahodie wɔ abusua, mpɔtam ne sikasɛm ho.",
        ["Adwumayɛ boa abusua ma wɔnya nea wɔhia."],
        ["Work helps families obtain what they need."],
        ["adwumayɛ", "adwuma", "ɔyɛ adwuma"],
        ["work", "occupation", "employment"],
        [
            "Dɛn ne adwumayɛ?",
            "Dɛn nti na adwuma ho hia?",
        ],
    ),

    make_item(
        "Nwenefoɔ",
        "Weaver",
        "traditional occupations",
        "Nwenefoɔ yɛ obi a ɔnwene ntoma anaa nneɛma foforɔ a wɔde nwene yɛ.",
        "A weaver is a person who produces cloth or other woven items.",
        "Nwenefoɔ betumi anya nimdeɛ wɔ ntoma nwene mu na wɔde yɛ amammerɛ mu nneɛma.",
        ["Nwenefoɔ nwene ntoma."],
        ["The weaver produces cloth."],
        ["nwenefoɔ", "nwene", "ntoma"],
        ["weaver", "weaving", "textile worker"],
        [
            "Hwan ne nwenefoɔ?",
            "Dɛn na nwenefoɔ yɛ?",
        ],
    ),

    # ========================================================
    # 19. INHERITANCE AND HERITAGE
    # ========================================================

    make_item(
        "Agyapadeɛ",
        "Inheritance and heritage",
        "family and inheritance",
        "Agyapadeɛ yɛ adeɛ, hokwan, asɛyɛdeɛ anaa amammerɛ a wɔde kɔ awoɔ ntoatoasoɔ so.",
        "Inheritance can include property, rights, responsibilities, and cultural heritage passed between generations.",
        "Agyapadeɛ nyɛ sika anaa asase nko; ɛtumi ka amammerɛ ne asɛyɛdeɛ ho.",
        ["Agyapadeɛ betumi ayɛ amammerɛ a awofoɔ de ma wɔn mma."],
        ["Inheritance can include cultural traditions passed to children."],
        ["agyapadeɛ", "abusua agyapadeɛ", "agyapadeɛ mu"],
        ["inheritance", "heritage", "family property"],
        [
            "Dɛn ne agyapadeɛ?",
            "Agyapadeɛ yɛ dɛn?",
        ],
    ),

    make_item(
        "Abusua agyapadeɛ",
        "Family inheritance",
        "family and inheritance",
        "Abusua agyapadeɛ yɛ adeɛ a ɛyɛ abusua dea na wɔde kɔ awoɔ ntoatoasoɔ so.",
        "Family inheritance refers to property, rights, or responsibilities associated with a family and passed across generations.",
        "Abusua agyapadeɛ ho nhyehyɛeɛ betumi ayɛ soronko wɔ mpɔtam ne abusua ahodoɔ mu.",
        ["Abusua no hwɛ wɔn agyapadeɛ so."],
        ["The family manages its inheritance."],
        ["abusua agyapadeɛ", "agyapadeɛ", "abusua"],
        ["family inheritance", "family property", "inheritance"],
        [
            "Dɛn ne abusua agyapadeɛ?",
            "Ɔkwan bɛn so na abusua agyapadeɛ kɔ awoɔ ntoatoasoɔ so?",
        ],
    ),

    make_item(
        "Amammerɛ agyapadeɛ",
        "Cultural heritage",
        "heritage",
        "Amammerɛ agyapadeɛ yɛ amammerɛ, kasa, amanneɛ, abakɔsɛm ne nimdeɛ a awoɔ ntoatoasoɔ de ma wɔn a wɔba akyiri.",
        "Cultural heritage is the language, customs, history, knowledge, and traditions passed between generations.",
        "Amammerɛ agyapadeɛ ma awoɔ ntoatoasoɔ foforɔ nya kwan sua wɔn abusua ne mpɔtam ho nneɛma.",
        ["Kasa ne mmebusɛm yɛ amammerɛ agyapadeɛ ho nhwɛsoɔ."],
        ["Language and proverbs can be examples of cultural heritage."],
        ["amammerɛ agyapadeɛ", "agyapadeɛ", "amammerɛ"],
        ["cultural heritage", "heritage", "cultural inheritance"],
        [
            "Dɛn ne amammerɛ agyapadeɛ?",
            "Dɛn na yɛfrɛ cultural heritage?",
        ],
    ),

    # ========================================================
    # 20. LANGUAGE AND IDENTITY
    # ========================================================

    make_item(
        "Akan kasa",
        "Akan language",
        "language and identity",
        "Akan kasa yɛ kasa a Akanfoɔ de di nkitahodie na ɛyɛ wɔn amammerɛ ne nipasu no fã.",
        "Akan is a language group used by Akan communities and is an important part of cultural identity.",
        "Akan kasa boa ma wɔde abakɔsɛm, mmebusɛm, nnwom, anansesɛm ne nimdeɛ kɔ awoɔ ntoatoasoɔ so.",
        ["Akan kasa boa ma amammerɛ tena hɔ."],
        ["Akan language helps preserve culture."],
        ["Akan kasa", "Twi", "Akan"],
        ["Akan language", "Twi", "Akan languages"],
        [
            "Dɛn ne Akan kasa?",
            "Twi yɛ Akan kasa anaa?",
        ],
    ),

    make_item(
        "Twi",
        "Twi",
        "language and identity",
        "Twi yɛ Akan kasa ahodoɔ mu kasa a nnipa pii ka wɔ Ghana.",
        "Twi is an Akan language variety spoken widely in Ghana.",
        "Twi wɔ kasa mu nsonsonoeɛ ne mpɔtam mu nneyɛeɛ ahodoɔ.",
        ["Nnipa pii ka Twi wɔ Ghana."],
        ["Many people speak Twi in Ghana."],
        ["Twi", "Akan kasa", "kasa"],
        ["Twi", "Akan language", "Ghanaian language"],
        [
            "Dɛn ne Twi?",
            "Twi yɛ Akan kasa anaa?",
        ],
    ),

    make_item(
        "Kasa ne nipasu",
        "Language and identity",
        "language and identity",
        "Kasa ne nipasu yɛ abusuabɔ a ɛda kasa a nnipa ka ne wɔn amammerɛ mu nipasu ntam.",
        "Language and identity describes the relationship between language and cultural identity.",
        "Kasa boa ma nnipa de wɔn abakɔsɛm, amammerɛ ne gyinapɛn da adi.",
        ["Kasa yɛ amammerɛ mu nipasu no fã."],
        ["Language is part of cultural identity."],
        ["kasa", "nipasu", "Akan kasa"],
        ["language", "identity", "cultural identity"],
        [
            "Ɔkwan bɛn so na kasa ne nipasu wɔ abusuabɔ?",
        ],
    ),

    make_item(
        "Kasa kora amammerɛ",
        "Language as cultural preservation",
        "language and identity",
        "Kasa kora amammerɛ yɛ sɛnea kasa boa ma wɔde amammerɛ, abakɔsɛm ne nyansa kɔ awoɔ ntoatoasoɔ so.",
        "Language as cultural preservation describes how language helps transmit culture, history, and wisdom.",
        "Mmebusɛm, anansesɛm ne nkyea yɛ nneɛma a kasa betumi de akora.",
        ["Kasa boa ma mmebusɛm tena hɔ."],
        ["Language helps preserve proverbs."],
        ["kasa", "amammerɛ", "mmebusɛm"],
        ["language preservation", "culture", "oral tradition"],
        [
            "Ɔkwan bɛn so na kasa kora amammerɛ?",
        ],
    ),

    # ========================================================
    # 21. CHILDHOOD AND UPBRINGING
    # ========================================================

    make_item(
        "Mmofra nteteeɛ",
        "Child upbringing",
        "childhood and upbringing",
        "Mmofra nteteeɛ yɛ ɔkwan a abusua ne mpɔtam fa so kyerɛkyerɛ mmofra suban, asɛyɛdeɛ ne asetena.",
        "Child upbringing is the process through which families and communities teach children behaviour, responsibility, and social values.",
        "Mmofra nteteeɛ ka obu, ahobrɛaseɛ, adwuma, kasa ne afoforo ho nidi ho.",
        ["Awofoɔ de mmofra nteteeɛ kyerɛ wɔn mma suban pa."],
        ["Parents teach children good behaviour through upbringing."],
        ["mmofra nteteeɛ", "mmofra", "awofoɔ"],
        ["child upbringing", "child development", "parenting"],
        [
            "Dɛn ne mmofra nteteeɛ?",
            "Ɔkwan bɛn so na Akanfoɔ tete mmofra?",
        ],
    ),

    make_item(
        "Mmofra suban",
        "Children's behaviour",
        "childhood and upbringing",
        "Mmofra suban yɛ nneyɛeɛ ne suban a mmofra da no adi wɔ abusua ne mpɔtam mu.",
        "Children's behaviour refers to the conduct children display within family and community life.",
        "Akan abusua betumi akyerɛ mmofra sɛ wɔnyɛ nokwafoɔ, wɔntie na wɔmmu mpanyimfoɔ.",
        ["Wɔkyerɛ mmofra suban pa."],
        ["Children are taught good behaviour."],
        ["mmofra suban", "suban pa", "mmofra"],
        ["children's behaviour", "good behaviour", "child conduct"],
        [
            "Dɛn ne mmofra suban?",
            "Ɔkwan bɛn so na wɔkyerɛ mmofra suban pa?",
        ],
    ),

    make_item(
        "Mmofra ne mpanyimfoɔ",
        "Children and elders",
        "childhood and upbringing",
        "Mmofra ne mpanyimfoɔ abusuabɔ yɛ nkitahodie a ɛda mmofra ne mpanyimfoɔ ntam wɔ abusua ne mpɔtam mu.",
        "The relationship between children and elders concerns interaction between younger and older members of the family or community.",
        "Abusuabɔ yi betumi ama mmofra anya afotuo ne amammerɛ ho nimdeɛ.",
        ["Mmofra sua afotuo firi mpanyimfoɔ hɔ."],
        ["Children learn guidance from elders."],
        ["mmofra", "mpanyimfoɔ", "afotuo"],
        ["children and elders", "intergenerational relationship"],
        [
            "Dɛn ne mmofra ne mpanyimfoɔ abusuabɔ?",
        ],
    ),

    # ========================================================
    # 22. SOCIAL VALUES
    # ========================================================

    make_item(
        "Nokware",
        "Truthfulness",
        "social values",
        "Nokware yɛ suban a obi ka nea ɛyɛ nokware na ɔnnnaadaa afoforo.",
        "Truthfulness is the value of speaking honestly and avoiding deception.",
        "Nokware yɛ gyinapɛn a ɛboa ma nkurɔfoɔ nya wɔn ho wɔn ho mu ahotosoɔ.",
        ["Nokware boa ma ahotosoɔ yɛ den."],
        ["Truthfulness helps build trust."],
        ["nokware", "nokwaredie", "ahotosoɔ"],
        ["truthfulness", "honesty", "trust"],
        [
            "Dɛn ne nokware?",
            "Dɛn nti na nokware ho hia?",
        ],
    ),

    make_item(
        "Ayɛyie",
        "Appreciation",
        "social values",
        "Ayɛyie yɛ sɛ obi da anigyeɛ ne anisɔ adi wɔ adeɛ pa a obi ayɛ ho.",
        "Appreciation is expressing gratitude or recognition for something good someone has done.",
        "Ayɛyie betumi hyɛ nkabom ne ayɔnkofa den wɔ abusua ne mpɔtam mu.",
        ["Wɔde ayɛyie ma obi a ɔaboa wɔn."],
        ["They show appreciation to someone who helped them."],
        ["ayɛyie", "anisɔ", "aseda"],
        ["appreciation", "gratitude", "thankfulness"],
        [
            "Dɛn ne ayɛyie?",
            "Ɔkwan bɛn so na yɛda ayɛyie adi?",
        ],
    ),

    make_item(
        "Aseda",
        "Thankfulness",
        "social values",
        "Aseda yɛ sɛ obi da anisɔ adi wɔ mmoa, adom anaa adeɛ pa bi a wanya ho.",
        "Thankfulness is expressing gratitude for help, favour, or something good received.",
        "Aseda betumi ada adi wɔ kasa, nneyɛeɛ anaa amammerɛ mu dwumadie.",
        ["Ɔdaa aseda adi wɔ mmoa no ho."],
        ["He expressed thanks for the help."],
        ["aseda", "anisɔ", "ayɛyie"],
        ["thankfulness", "gratitude", "thanks"],
        [
            "Dɛn ne aseda?",
            "Dɛn nti na aseda ho hia?",
        ],
    ),

    make_item(
        "Nokwaredie",
        "Honesty",
        "social values",
        "Nokwaredie yɛ suban a obi yɛ nokware wɔ ne kasa ne ne nneyɛeɛ mu.",
        "Honesty is the practice of being truthful in speech and conduct.",
        "Nokwaredie betumi aboa ma nnipa anya wɔn ho wɔn ho mu ahotosoɔ.",
        ["Nokwaredie yɛ suban pa."],
        ["Honesty is considered a good quality."],
        ["nokwaredie", "nokware", "ahotosoɔ"],
        ["honesty", "truthfulness", "trust"],
        [
            "Dɛn ne nokwaredie?",
            "Dɛn nti na honesty ho hia?",
        ],
    ),

    make_item(
        "Ahotosoɔ",
        "Trust",
        "social values",
        "Ahotosoɔ yɛ gyidi a obi wɔ wɔ obi foforɔ anaa nkitahodie bi mu sɛ ɔbɛyɛ adeɛ a ɛyɛ.",
        "Trust is confidence in another person or relationship.",
        "Ahotosoɔ betumi ayɛ den denam nokwaredie, nokwafoɔyɛ ne asɛyɛdeɛ so.",
        ["Nokwaredie ma ahotosoɔ yɛ den."],
        ["Honesty can strengthen trust."],
        ["ahotosoɔ", "nokwaredie", "nkitahodie"],
        ["trust", "confidence", "social trust"],
        [
            "Dɛn ne ahotosoɔ?",
            "Dɛn na ɛma ahotosoɔ yɛ den?",
        ],
    ),

    # ========================================================
    # 23. CULTURAL PRESERVATION
    # ========================================================

    make_item(
        "Amammerɛ ahwɛyiyeɛ",
        "Cultural preservation",
        "cultural preservation",
        "Amammerɛ ahwɛyiyeɛ yɛ mmɔden a nnipa yɛ de bɔ amammerɛ, kasa, abakɔsɛm ne amanneɛ ho ban.",
        "Cultural preservation is the effort to protect language, history, customs, and traditions for future generations.",
        "Kasa, nwoma, anansesɛm, mmebusɛm, nnwom ne afahyɛ betumi aboa ma amammerɛ tena hɔ.",
        ["Akan kasa sua ne kyerɛwtohɔ betumi aboa amammerɛ ahwɛyiyeɛ."],
        ["Learning and documenting Akan can support cultural preservation."],
        ["amammerɛ ahwɛyiyeɛ", "amammerɛ", "kasa"],
        ["cultural preservation", "heritage preservation", "culture protection"],
        [
            "Dɛn ne amammerɛ ahwɛyiyeɛ?",
            "Ɔkwan bɛn so na yɛbɛbɔ Akan amammerɛ ho ban?",
        ],
    ),

    make_item(
        "Akan kasa kora",
        "Akan language preservation",
        "cultural preservation",
        "Akan kasa kora yɛ mmɔden a wɔyɛ de ma Akan kasa tena hɔ na awoɔ ntoatoasoɔ sua no.",
        "Akan language preservation is the effort to maintain and transmit Akan language across generations.",
        "Kasa kyerɛkyerɛ, nwoma, audio ne dijitaal nnwinnadeɛ betumi aboa kasa kora.",
        ["Akan kasa kyerɛkyerɛ betumi aboa kasa kora."],
        ["Akan language education can support language preservation."],
        ["Akan kasa", "kora", "amammerɛ"],
        ["Akan language preservation", "language maintenance"],
        [
            "Ɔkwan bɛn so na yɛbɛkora Akan kasa?",
        ],
    ),

    make_item(
        "Amammerɛ kyerɛwtohɔ",
        "Cultural documentation",
        "cultural preservation",
        "Amammerɛ kyerɛwtohɔ yɛ amammerɛ, abakɔsɛm, kasa ne amanneɛ ho nsɛm a wɔkyerɛw anaa wɔde sie wɔ kwan ahodoɔ so.",
        "Cultural documentation is the recording and preservation of cultural knowledge, history, language, and traditions.",
        "Kyerɛwtohɔ betumi ama awoɔ ntoatoasoɔ a ɛreba anya kwan ahu amammerɛ ho nimdeɛ.",
        ["Wɔkyerɛw Akan mmebusɛm de sie."],
        ["Akan proverbs may be documented for future generations."],
        ["amammerɛ kyerɛwtohɔ", "kyerɛwtohɔ", "amammerɛ"],
        ["cultural documentation", "documentation", "heritage records"],
        [
            "Dɛn ne amammerɛ kyerɛwtohɔ?",
            "Dɛn nti na ɛho hia sɛ yɛkyerɛw amammerɛ?",
        ],
    ),

    # ========================================================
    # 24. MODERN AKAN SOCIETY
    # ========================================================

    make_item(
        "Akan amammerɛ wɔ nnɛ",
        "Akan culture in modern society",
        "modern culture",
        "Akan amammerɛ wɔ nnɛ yɛ sɛnea Akan gyinapɛn, kasa ne amanneɛ da so ara wɔ nnɛyi asetena mu bere a wɔresesa wɔ mmeaeɛ bi.",
        "Akan culture in modern society describes how Akan values, language, and traditions continue while adapting to contemporary life.",
        "Nnɛyi sukuu, mfiridwuma ne nkurow akɛseɛ ama asetena asesa wɔ mmeaeɛ bi, nanso amammerɛ pii da so wɔ hɔ.",
        ["Akan kasa da so yɛ adwuma wɔ nnɛyi asetena mu."],
        ["Akan language continues to be used in modern life."],
        ["Akan amammerɛ wɔ nnɛ", "nnɛyi Akan amammerɛ", "Akan asetena nnɛ"],
        ["modern Akan culture", "Akan culture today", "contemporary Akan society"],
        [
            "Akan amammerɛ te sɛn nnɛ?",
            "So Akan amammerɛ da so wɔ hɔ?",
        ],
    ),

    make_item(
        "Akan amammerɛ ne mfiridwuma",
        "Akan culture and technology",
        "modern culture",
        "Akan amammerɛ ne mfiridwuma yɛ sɛnea nnɛyi mfiridwuma betumi aboa ma wɔde Akan kasa ne amammerɛ akyerɛkyerɛ na wɔahwɛ so.",
        "Akan culture and technology concerns how modern technology can support the teaching and preservation of Akan language and culture.",
        "Intanɛt, dijitaal nwoma, mobile application ne audio betumi aboa ma nnipa sua Akan amammerɛ.",
        ["Mfiridwuma betumi aboa ma mmofra sua Akan amammerɛ."],
        ["Technology can help children learn Akan culture."],
        ["Akan amammerɛ", "mfiridwuma", "dijitaal"],
        ["Akan culture and technology", "digital culture", "technology"],
        [
            "Ɔkwan bɛn so na mfiridwuma betumi aboa Akan amammerɛ?",
        ],
    ),

    make_item(
        "Dijitaal Akan",
        "Digital Akan culture",
        "modern culture",
        "Dijitaal Akan yɛ sɛnea wɔde dijitaal mfiridwuma de Akan kasa ne amammerɛ sie, kyerɛkyerɛ na wɔkyɛ.",
        "Digital Akan culture refers to using digital technology to preserve, teach, and share Akan language and culture.",
        "Dijitaal nhoma, audio, video ne application betumi ayɛ nnwinnadeɛ wɔ amammerɛ mu adesua mu.",
        ["Application betumi aboa ma nnipa sua Akan kasa."],
        ["An application can help people learn Akan language."],
        ["dijitaal Akan", "Akan", "mfiridwuma"],
        ["digital Akan", "digital culture", "Akan technology"],
        [
            "Dɛn ne dijitaal Akan?",
            "Ɔkwan bɛn so na technology betumi aboa Akan?",
        ],
    ),

    # ========================================================
    # 25. COMMUNITY VALUES
    # ========================================================

    make_item(
        "Nkabom ne asɛyɛdeɛ",
        "Community cooperation and responsibility",
        "community values",
        "Nkabom ne asɛyɛdeɛ yɛ sɛnea nnipa bom di wɔn mpɔtam mu asɛyɛdeɛ ho dwuma.",
        "Community cooperation and responsibility describe people working together to fulfil community responsibilities.",
        "Mpɔtam mu nkabom betumi ama wɔadi ɔhaw ahodoɔ ho dwuma wɔ ɔkwan a ɛyɛ adwuma so.",
        ["Mpɔtamfoɔ yɛ adwuma bom de siesie mpɔtam."],
        ["Community members work together to improve their community."],
        ["nkabom", "asɛyɛdeɛ", "mpɔtam"],
        ["community cooperation", "responsibility", "community service"],
        [
            "Dɛn ne nkabom ne asɛyɛdeɛ?",
        ],
    ),

    make_item(
        "Mpɔtam mu asɛyɛdeɛ",
        "Community responsibility",
        "community values",
        "Mpɔtam mu asɛyɛdeɛ yɛ nneɛma a ɛsɛ sɛ mpɔtamfoɔ yɛ de boa wɔn mpɔtam.",
        "Community responsibility refers to duties people have toward their community.",
        "Asɛyɛdeɛ betumi ayɛ ahwɛyiyeɛ, mmoa, ahotɔ ne mpɔtam mu nkabom.",
        ["Mpɔtamfoɔ wɔ asɛyɛdeɛ sɛ wɔhwɛ wɔn mpɔtam so."],
        ["Community members have responsibilities toward their community."],
        ["mpɔtam mu asɛyɛdeɛ", "asɛyɛdeɛ", "mpɔtam"],
        ["community responsibility", "civic responsibility", "community duty"],
        [
            "Dɛn ne mpɔtam mu asɛyɛdeɛ?",
            "Dɛn na mpɔtamfoɔ wɔ asɛyɛdeɛ sɛ wɔyɛ?",
        ],
    ),

    # ========================================================
    # 26. CULTURAL CHANGE
    # ========================================================

    make_item(
        "Amammerɛ nsakraeɛ",
        "Cultural change",
        "modern culture",
        "Amammerɛ nsakraeɛ yɛ nsakraeɛ a ɛba amammerɛ mu bere a asetena ne bere sesa.",
        "Cultural change refers to changes that occur in cultural practices as society and circumstances change.",
        "Nnɛyi mfiridwuma, sukuu, nkurow ne nkitahodie betumi ama amammerɛ mu nneɛma bi asesa.",
        ["Amammerɛ bi sesa bere a asetena sesa."],
        ["Some cultural practices change as society changes."],
        ["amammerɛ nsakraeɛ", "amammerɛ", "nsakraeɛ"],
        ["cultural change", "social change", "changing traditions"],
        [
            "Dɛn ne amammerɛ nsakraeɛ?",
            "Dɛn nti na amammerɛ sesa?",
        ],
    ),

    make_item(
        "Amammerɛ ne nnɛyi asetena",
        "Culture and modern life",
        "modern culture",
        "Amammerɛ ne nnɛyi asetena yɛ sɛnea amammerɛ ne nnɛyi sukuu, adwuma, mfiridwuma ne nkitahodie di nkitaho.",
        "Culture and modern life describes the interaction between cultural traditions and contemporary living.",
        "Nnipa betumi akora amammerɛ mu gyinapɛn bi so bere a wɔde nnɛyi mfiridwuma ne asetena di dwuma.",
        ["Nnipa betumi de technology akora amammerɛ so."],
        ["People can use technology to preserve cultural practices."],
        ["amammerɛ", "nnɛyi asetena", "mfiridwuma"],
        ["culture and modern life", "modern society", "tradition and technology"],
        [
            "Ɔkwan bɛn so na amammerɛ ne nnɛyi asetena di nkitaho?",
        ],
    ),
]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """
    Generate structured Akan cultural knowledge records.

    Each intermediate CULTURE item is converted into the
    project's shared Akan schema.
    """

    records: list[dict] = []

    for record_number, item in enumerate(CULTURE, start=1):

        record = create_akan_record(
            record_id=f"AKAN-CULTURE-{record_number:04d}",
            akan_term=item["akan_term"],
            english_term=item["english_term"],
            category="culture",
            subcategory=item["subcategory"],
            definition_akan=item["definition_akan"],
            definition_english=item["definition_english"],
            explanation_akan=item["explanation_akan"],
            examples_akan=item["examples_akan"],
            examples_english=item["examples_english"],
            keywords_akan=item["keywords_akan"],
            keywords_english=item["keywords_english"],
            question_patterns=item["question_patterns"],
        )

        records.append(record)

    return records


# ============================================================
# PUBLIC API
# ============================================================

__all__ = ["generate"]

