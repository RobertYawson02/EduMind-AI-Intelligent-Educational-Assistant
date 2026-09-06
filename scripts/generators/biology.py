"""
==============================================================
BIOLOGY KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY="Biology"

CONCEPTS=[

("Biology",["life science"]),
("Cell",["cells"]),
("Animal Cell",["animal cells"]),
("Plant Cell",["plant cells"]),
("Cell Membrane",["plasma membrane"]),
("Nucleus",["cell nucleus"]),
("Mitochondria",["mitochondrion"]),
("Chloroplast",["chloroplast"]),
("Ribosome",["ribosomes"]),

("DNA",["deoxyribonucleic acid"]),
("RNA",["ribonucleic acid"]),
("Gene",["genes"]),
("Chromosome",["chromosomes"]),
("Genetics",["genetics"]),
("Inheritance",["genetic inheritance"]),
("Mutation",["mutations"]),

("Photosynthesis",["photosynthesis"]),
("Respiration",["cellular respiration"]),
("Diffusion",["diffusion"]),
("Osmosis",["osmosis"]),
("Active Transport",["active transport"]),

("Human Body",["human anatomy"]),
("Digestive System",["digestion"]),
("Respiratory System",["respiration system"]),
("Circulatory System",["blood circulation"]),
("Nervous System",["nervous system"]),
("Immune System",["immunity"]),
("Endocrine System",["hormonal system"]),

("Blood",["blood"]),
("Heart",["human heart"]),
("Brain",["human brain"]),

("Ecosystem",["ecosystems"]),
("Food Chain",["food chains"]),
("Food Web",["food web"]),
("Biodiversity",["biological diversity"]),
("Ecology",["ecology"]),
("Habitat",["habitats"]),
("Population",["biological population"]),
("Community",["ecological community"]),

("Evolution",["biological evolution"]),
("Natural Selection",["Darwinian selection"]),
("Adaptation",["adaptation"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records