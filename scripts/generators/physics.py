"""
==============================================================
PHYSICS KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY="Physics"

CONCEPTS=[

("Physics",["physical science"]),
("Measurement",["scientific measurement"]),
("SI Unit",["international system of units"]),
("Scalar Quantity",["scalar"]),
("Vector Quantity",["vector"]),

("Motion",["kinematics"]),
("Distance",["distance travelled"]),
("Displacement",["displacement"]),
("Speed",["average speed"]),
("Velocity",["velocity"]),
("Acceleration",["acceleration"]),
("Uniform Motion",["constant velocity"]),
("Projectile Motion",["projectile"]),

("Force",["force"]),
("Newton's First Law",["law of inertia"]),
("Newton's Second Law",["F=ma"]),
("Newton's Third Law",["action and reaction"]),
("Momentum",["linear momentum"]),
("Impulse",["impulse"]),

("Work",["mechanical work"]),
("Energy",["energy"]),
("Kinetic Energy",["KE"]),
("Potential Energy",["PE"]),
("Power",["mechanical power"]),

("Gravitation",["gravity"]),
("Gravitational Field",["gravitational field"]),
("Weight",["weight force"]),

("Pressure",["pressure"]),
("Density",["density"]),
("Buoyancy",["Archimedes principle"]),

("Heat",["thermal energy"]),
("Temperature",["temperature"]),
("Specific Heat Capacity",["specific heat"]),
("Heat Transfer",["conduction","convection","radiation"]),

("Wave",["waves"]),
("Frequency",["wave frequency"]),
("Wavelength",["wave wavelength"]),
("Amplitude",["wave amplitude"]),
("Sound",["sound waves"]),
("Light",["light waves"]),

("Reflection",["light reflection"]),
("Refraction",["light refraction"]),
("Lens",["optical lens"]),
("Mirror",["optical mirror"]),

("Electric Charge",["electricity"]),
("Electric Current",["current"]),
("Voltage",["potential difference"]),
("Resistance",["electrical resistance"]),
("Ohm's Law",["V=IR"]),
("Electric Circuit",["electrical circuit"]),

("Magnetic Field",["magnetism"]),
("Electromagnet",["electromagnetic field"]),
("Electromagnetic Induction",["Faraday's law"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records