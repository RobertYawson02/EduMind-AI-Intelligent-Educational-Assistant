"""
==============================================================
CAREER AND PROFESSIONAL DEVELOPMENT GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations

from .common import build_knowledge_family

CATEGORY = "Career Development"

CONCEPTS = [
    ("Career Development", ["career planning"]),
    ("Career Planning", ["professional planning"]),
    ("Career Goal", ["career goals"]),
    ("Career Choice", ["choosing a career"]),
    ("Employability Skills", ["job skills"]),
    ("Soft Skills", ["interpersonal skills"]),
    ("Technical Skills", ["professional technical skills"]),
    ("Communication Skills", ["workplace communication"]),
    ("Teamwork", ["team collaboration"]),
    ("Leadership Skills", ["leadership"]),
    ("Problem Solving", ["workplace problem solving"]),
    ("Critical Thinking", ["professional critical thinking"]),
    ("Time Management", ["work time management"]),
    ("Professionalism", ["professional conduct"]),
    ("Workplace Ethics", ["professional ethics"]),
    ("Networking", ["professional networking"]),
    ("Internship", ["industrial attachment"]),
    ("Industrial Training", ["work placement"]),
    ("National Service", ["national service"]),
    ("Job Search", ["finding jobs"]),
    ("Job Application", ["employment application"]),
    ("Curriculum Vitae", ["CV"]),
    ("Resume", ["résumé"]),
    ("Cover Letter", ["application letter"]),
    ("Job Interview", ["interview"]),
    ("Interview Preparation", ["interview preparation"]),
    ("Interview Question", ["interview questions"]),
    ("Personal Branding", ["professional brand"]),
    ("LinkedIn Profile", ["LinkedIn"]),
    ("Portfolio", ["professional portfolio"]),
    ("GitHub Portfolio", ["coding portfolio"]),
    ("Professional Certification", ["certification"]),
    ("Work Experience", ["professional experience"]),
    ("Volunteer Experience", ["volunteering"]),
    ("Career Mentor", ["mentorship"]),
    ("Entrepreneurship", ["starting a business"]),
    ("Freelancing", ["freelance work"]),
    ("Remote Work", ["working remotely"]),
    ("Workplace Safety", ["occupational safety"]),
    ("Workplace Communication", ["professional communication"]),
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