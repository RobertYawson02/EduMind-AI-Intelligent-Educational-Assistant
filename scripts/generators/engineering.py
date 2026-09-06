"""
==============================================================
ENGINEERING KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY = "Engineering"

CONCEPTS = [

    ("Engineering", ["engineering discipline"]),

    # Electrical
    ("Electrical Engineering", ["electrical systems"]),
    ("Voltage", ["electrical voltage"]),
    ("Current", ["electric current"]),
    ("Resistance", ["electrical resistance"]),
    ("Power", ["electrical power"]),
    ("Ohm's Law", ["V=IR"]),
    ("Transformer", ["electrical transformer"]),

    # Electronics
    ("Electronics", ["electronic systems"]),
    ("Resistor", ["electronic resistor"]),
    ("Capacitor", ["electronic capacitor"]),
    ("Inductor", ["electronic inductor"]),
    ("Diode", ["semiconductor diode"]),
    ("Transistor", ["electronic transistor"]),
    ("Integrated Circuit", ["IC"]),
    ("Logic Gate", ["digital logic gate"]),
    ("Microcontroller", ["MCU"]),
    ("Arduino", ["Arduino board"]),

    # Computer Engineering
    ("Computer Engineering", ["computer hardware engineering"]),
    ("CPU", ["processor"]),
    ("Memory", ["RAM"]),
    ("Storage", ["computer storage"]),
    ("Motherboard", ["system board"]),

    # Mechanical
    ("Mechanical Engineering", ["mechanical systems"]),
    ("Torque", ["rotational force"]),
    ("Machine", ["mechanical machine"]),
    ("Gear", ["gear mechanism"]),
    ("Bearing", ["mechanical bearing"]),

    # Civil
    ("Civil Engineering", ["civil structures"]),
    ("Bridge", ["bridge engineering"]),
    ("Concrete", ["cement concrete"]),
    ("Beam", ["structural beam"]),
    ("Foundation", ["building foundation"]),

    # General
    ("Engineering Drawing", ["technical drawing"]),
    ("Blueprint", ["engineering blueprint"]),
    ("Measurement", ["engineering measurement"]),
    ("Tolerance", ["engineering tolerance"]),
    ("Safety Engineering", ["engineering safety"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records