"""
==============================================================
STUDY SKILLS KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations

from .common import build_knowledge_family

CATEGORY = "Study Skills"

CONCEPTS = [
    ("Study Skills", ["learning skills"]),
    ("Effective Studying", ["study techniques"]),
    ("Time Management", ["managing study time"]),
    ("Study Schedule", ["study timetable"]),
    ("Goal Setting", ["learning goals"]),
    ("SMART Goals", ["SMART objectives"]),
    ("Note Taking", ["taking notes"]),
    ("Cornell Note Taking", ["Cornell notes"]),
    ("Mind Mapping", ["mind map"]),
    ("Concept Mapping", ["concept map"]),
    ("Active Recall", ["active recall"]),
    ("Spaced Repetition", ["spaced learning"]),
    ("Practice Testing", ["retrieval practice"]),
    ("Flashcards", ["study cards"]),
    ("Pomodoro Technique", ["Pomodoro"]),
    ("Concentration", ["focus"]),
    ("Memory", ["learning memory"]),
    ("Memory Techniques", ["memorization"]),
    ("Revision", ["revision techniques"]),
    ("Exam Preparation", ["exam revision"]),
    ("Examination", ["exam"]),
    ("Multiple Choice Questions", ["MCQ"]),
    ("Short Answer Question", ["short answer"]),
    ("Essay Question", ["essay exam"]),
    ("Problem Solving", ["problem solving skills"]),
    ("Critical Thinking", ["critical thinking skills"]),
    ("Creative Thinking", ["creativity"]),
    ("Logical Thinking", ["logical reasoning"]),
    ("Reading Skills", ["academic reading"]),
    ("Active Reading", ["effective reading"]),
    ("Comprehension", ["reading comprehension"]),
    ("Academic Listening", ["listening skills"]),
    ("Group Study", ["study group"]),
    ("Independent Learning", ["self-directed learning"]),
    ("Online Learning", ["e-learning"]),
    ("Research Skills", ["academic research skills"]),
    ("Information Literacy", ["information literacy"]),
    ("Digital Literacy", ["digital skills"]),
    ("Academic Motivation", ["study motivation"]),
    ("Procrastination", ["delaying study"]),
    ("Study Environment", ["learning environment"]),
    ("Exam Anxiety", ["test anxiety"]),
    ("Academic Stress", ["study stress"]),
    ("Sleep and Learning", ["sleep study"]),
    ("Healthy Study Habits", ["study habits"]),
    ("Learning Style", ["learning preferences"]),
    ("Self Assessment", ["self evaluation"]),
    ("Peer Learning", ["peer study"]),
    ("Academic Planning", ["education planning"]),
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