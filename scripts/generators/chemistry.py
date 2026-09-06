"""
==============================================================
CHEMISTRY KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY="Chemistry"

CONCEPTS=[

("Chemistry",["chemical science"]),
("Matter",["matter"]),
("Atom",["atoms"]),
("Molecule",["molecules"]),
("Element",["chemical element"]),
("Compound",["chemical compound"]),
("Mixture",["mixtures"]),

("Periodic Table",["periodic table"]),
("Atomic Number",["proton number"]),
("Mass Number",["nucleon number"]),
("Isotope",["isotopes"]),
("Ion",["charged atom"]),
("Cation",["positive ion"]),
("Anion",["negative ion"]),

("Chemical Bond",["bond"]),
("Ionic Bond",["ionic bonding"]),
("Covalent Bond",["covalent bonding"]),
("Metallic Bond",["metallic bonding"]),

("Chemical Reaction",["reaction"]),
("Balancing Chemical Equations",["chemical balancing"]),
("Oxidation",["oxidation"]),
("Reduction",["reduction"]),
("Redox Reaction",["redox"]),

("Acid",["acid"]),
("Base",["alkali"]),
("Salt",["salt"]),
("pH Scale",["pH"]),
("Neutralization",["neutralization"]),

("States of Matter",["solid","liquid","gas"]),
("Evaporation",["evaporation"]),
("Condensation",["condensation"]),
("Melting",["melting"]),
("Freezing",["freezing"]),

("Organic Chemistry",["organic compounds"]),
("Hydrocarbon",["hydrocarbons"]),
("Alkane",["alkanes"]),
("Alkene",["alkenes"]),
("Alcohol",["alcohol compounds"]),

("Chemical Equilibrium",["equilibrium"]),
("Catalyst",["catalysis"]),
("Reaction Rate",["rate of reaction"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records