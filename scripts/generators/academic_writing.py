"""
==============================================================
ACADEMIC WRITING KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations

from .common import build_knowledge_family

CATEGORY = "Academic Writing"

CONCEPTS = [
    ("Academic Writing", ["scholarly writing"]),
    ("Academic Essay", ["essay writing"]),
    ("Essay Introduction", ["introduction paragraph"]),
    ("Essay Body", ["body paragraphs"]),
    ("Essay Conclusion", ["conclusion paragraph"]),
    ("Thesis Statement", ["thesis"]),
    ("Topic Sentence", ["paragraph topic sentence"]),
    ("Supporting Evidence", ["evidence"]),
    ("Argument", ["academic argument"]),
    ("Counterargument", ["opposing argument"]),
    ("Paragraph", ["academic paragraph"]),
    ("Paragraph Structure", ["paragraph organization"]),
    ("Coherence", ["writing coherence"]),
    ("Cohesion", ["writing cohesion"]),
    ("Academic Vocabulary", ["scholarly vocabulary"]),
    ("Formal Language", ["formal academic language"]),
    ("Proofreading", ["proofreading"]),
    ("Editing", ["academic editing"]),
    ("Grammar", ["academic grammar"]),
    ("Punctuation", ["academic punctuation"]),
    ("Paraphrasing", ["paraphrase"]),
    ("Summarizing", ["summary writing"]),
    ("Quotation", ["direct quotation"]),
    ("Citation", ["academic citation"]),
    ("Referencing", ["academic referencing"]),
    ("APA Style", ["APA referencing"]),
    ("MLA Style", ["MLA referencing"]),
    ("Harvard Referencing", ["Harvard citation"]),
    ("IEEE Referencing", ["IEEE citation"]),
    ("Bibliography", ["bibliography"]),
    ("Reference List", ["references"]),
    ("Plagiarism", ["academic plagiarism"]),
    ("Academic Integrity", ["academic honesty"]),
    ("Research Paper", ["academic paper"]),
    ("Technical Report", ["technical writing"]),
    ("Project Report", ["final year project report"]),
    ("Literature Review", ["literature review"]),
    ("Abstract", ["research abstract"]),
    ("Methodology Section", ["research methodology section"]),
    ("Results Section", ["research results"]),
    ("Discussion Section", ["research discussion"]),
    ("Conclusion Section", ["research conclusion"]),
    ("Recommendation", ["research recommendations"]),
    ("Table of Contents", ["TOC"]),
    ("Appendix", ["appendices"]),
    ("Figure Caption", ["figure description"]),
    ("Table Caption", ["table description"]),
]

def generate():
    records = []

    for topic, aliases in CONCEPTS:
        records.extend(
            build_knowledge_family(
                topic,
                CATEGORY,
                aliases
            )
        )

    return records