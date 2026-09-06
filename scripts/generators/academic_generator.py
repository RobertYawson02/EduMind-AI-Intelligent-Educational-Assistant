"""
==============================================================
ACADEMIC KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate structured educational knowledge relating to
    academic studies, education, learning, teaching,
    assessment, curriculum, and higher education.

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

CATEGORY = "Academic Studies"


# ============================================================
# ACADEMIC TOPICS
# ============================================================

TOPICS = [

    # --------------------------------------------------------
    # Education and Learning
    # --------------------------------------------------------

    (
        "Education",
        ["schooling", "learning", "formal education"]
    ),

    (
        "Learning",
        ["knowledge acquisition", "skill development"]
    ),

    (
        "Teaching",
        ["instruction", "education"]
    ),

    (
        "Pedagogy",
        ["teaching methods", "instructional practice"]
    ),

    (
        "Andragogy",
        ["adult learning", "adult education"]
    ),

    (
        "Educational Psychology",
        ["psychology of learning", "learning psychology"]
    ),

    (
        "Learning Theory",
        ["theories of learning"]
    ),

    (
        "Behaviorism",
        ["behavioral learning theory"]
    ),

    (
        "Cognitivism",
        ["cognitive learning theory"]
    ),

    (
        "Constructivism",
        ["constructivist learning"]
    ),

    (
        "Experiential Learning",
        ["learning by experience"]
    ),

    (
        "Collaborative Learning",
        ["group learning", "cooperative learning"]
    ),

    (
        "Active Learning",
        ["student-centered learning"]
    ),

    (
        "Self-Directed Learning",
        ["independent learning", "autonomous learning"]
    ),

    (
        "Lifelong Learning",
        ["continuous learning", "continuing education"]
    ),

    (
        "Critical Thinking",
        ["analytical thinking", "reasoning"]
    ),

    (
        "Problem Solving",
        ["problem-solving skills"]
    ),

    (
        "Creativity in Education",
        ["creative learning", "educational creativity"]
    ),

    (
        "Metacognition",
        ["thinking about thinking", "self-regulated learning"]
    ),

    (
        "Academic Motivation",
        ["student motivation", "learning motivation"]
    ),

    # --------------------------------------------------------
    # Curriculum
    # --------------------------------------------------------

    (
        "Curriculum",
        ["academic curriculum", "course curriculum"]
    ),

    (
        "Curriculum Development",
        ["curriculum design"]
    ),

    (
        "Curriculum Planning",
        ["academic planning", "course planning"]
    ),

    (
        "Curriculum Evaluation",
        ["curriculum assessment"]
    ),

    (
        "Syllabus",
        ["course outline", "course content"]
    ),

    (
        "Course Objectives",
        ["learning objectives", "academic objectives"]
    ),

    (
        "Learning Outcomes",
        ["educational outcomes", "course outcomes"]
    ),

    (
        "Competency-Based Education",
        ["competency-based learning"]
    ),

    (
        "Outcome-Based Education",
        ["OBE", "outcome-based learning"]
    ),

    (
        "Bloom's Taxonomy",
        ["learning taxonomy", "educational objectives"]
    ),

    # --------------------------------------------------------
    # Assessment
    # --------------------------------------------------------

    (
        "Academic Assessment",
        ["educational assessment", "student assessment"]
    ),

    (
        "Formative Assessment",
        ["continuous assessment", "assessment for learning"]
    ),

    (
        "Summative Assessment",
        ["final assessment", "assessment of learning"]
    ),

    (
        "Diagnostic Assessment",
        ["diagnostic testing"]
    ),

    (
        "Assessment Criteria",
        ["grading criteria", "evaluation criteria"]
    ),

    (
        "Academic Grading",
        ["grading system", "student grades"]
    ),

    (
        "Examination",
        ["exam", "academic examination"]
    ),

    (
        "Quiz",
        ["academic quiz", "short assessment"]
    ),

    (
        "Assignment",
        ["academic assignment", "student task"]
    ),

    (
        "Project-Based Learning",
        ["project learning", "learning through projects"]
    ),

    # --------------------------------------------------------
    # Academic Performance
    # --------------------------------------------------------

    (
        "Academic Performance",
        ["student performance", "academic achievement"]
    ),

    (
        "Grade Point Average",
        ["GPA", "academic average"]
    ),

    (
        "Cumulative Grade Point Average",
        ["CGPA", "cumulative GPA"]
    ),

    (
        "Academic Achievement",
        ["educational achievement", "student achievement"]
    ),

    (
        "Study Habits",
        ["learning habits", "academic habits"]
    ),

    (
        "Time Management",
        ["academic time management", "study planning"]
    ),

    (
        "Note Taking",
        ["note-taking", "study notes"]
    ),

    (
        "Revision",
        ["exam revision", "review"]
    ),

    (
        "Academic Reading",
        ["study reading", "scholarly reading"]
    ),

    (
        "Academic Listening",
        ["lecture listening", "learning through listening"]
    ),

    # --------------------------------------------------------
    # Higher Education
    # --------------------------------------------------------

    (
        "Higher Education",
        ["tertiary education", "university education"]
    ),

    (
        "University",
        ["higher institution", "tertiary institution"]
    ),

    (
        "College",
        ["higher education institution"]
    ),

    (
        "Polytechnic Education",
        ["technical higher education"]
    ),

    (
        "Technical Education",
        ["technical training", "technical studies"]
    ),

    (
        "Vocational Education",
        ["vocational training", "skills training"]
    ),

    (
        "Undergraduate Education",
        ["bachelor's education", "undergraduate studies"]
    ),

    (
        "Postgraduate Education",
        ["graduate education", "advanced studies"]
    ),

    (
        "Master's Degree",
        ["masters degree", "graduate degree"]
    ),

    (
        "Doctoral Degree",
        ["PhD", "doctorate"]
    ),

    (
        "Academic Degree",
        ["qualification", "educational degree"]
    ),

    # --------------------------------------------------------
    # Academic Structure
    # --------------------------------------------------------

    (
        "Academic Department",
        ["university department", "academic department"]
    ),

    (
        "Faculty",
        ["academic faculty", "school within university"]
    ),

    (
        "Academic Programme",
        ["degree programme", "study programme"]
    ),

    (
        "Academic Course",
        ["university course", "academic subject"]
    ),

    (
        "Credit Hour",
        ["academic credit", "course credit"]
    ),

    (
        "Semester",
        ["academic semester", "academic term"]
    ),

    (
        "Academic Year",
        ["school year", "academic session"]
    ),

    (
        "Lecture",
        ["academic lecture", "class lecture"]
    ),

    (
        "Tutorial",
        ["academic tutorial", "tutorial class"]
    ),

    (
        "Laboratory Session",
        ["lab session", "practical class"]
    ),

    # --------------------------------------------------------
    # Academic Quality
    # --------------------------------------------------------

    (
        "Educational Quality",
        ["quality education", "education quality"]
    ),

    (
        "Quality Assurance in Education",
        ["academic quality assurance", "education QA"]
    ),

    (
        "Academic Accreditation",
        ["educational accreditation", "institutional accreditation"]
    ),

    (
        "Academic Standards",
        ["educational standards", "academic requirements"]
    ),

    (
        "Educational Policy",
        ["education policy", "academic policy"]
    ),

    (
        "Academic Governance",
        ["educational governance", "university governance"]
    ),

    (
        "Student Support Services",
        ["academic support", "student services"]
    ),

    (
        "Academic Advising",
        ["academic counselling", "student advising"]
    ),

    # --------------------------------------------------------
    # Academic Integrity
    # --------------------------------------------------------

    (
        "Academic Integrity",
        ["academic honesty", "scholarly integrity"]
    ),

    (
        "Plagiarism",
        ["academic plagiarism", "copying academic work"]
    ),

    (
        "Citation",
        ["academic citation", "source citation"]
    ),

    (
        "Referencing",
        ["academic referencing", "source referencing"]
    ),

    (
        "Academic Ethics",
        ["educational ethics", "scholarly ethics"]
    ),

    (
        "Research Ethics",
        ["ethical research", "research conduct"]
    ),

    (
        "Academic Misconduct",
        ["academic dishonesty", "academic violations"]
    ),

    # --------------------------------------------------------
    # Digital Education
    # --------------------------------------------------------

    (
        "Online Learning",
        ["e-learning", "digital learning"]
    ),

    (
        "Distance Education",
        ["distance learning", "remote education"]
    ),

    (
        "Blended Learning",
        ["hybrid learning", "mixed-mode learning"]
    ),

    (
        "Virtual Classroom",
        ["online classroom", "digital classroom"]
    ),

    (
        "Learning Management System",
        ["LMS", "online learning platform"]
    ),

    (
        "Educational Technology",
        ["EdTech", "technology in education"]
    ),

    (
        "Digital Literacy",
        ["digital skills", "technology literacy"]
    ),

    (
        "Computer-Assisted Learning",
        ["computer-based learning", "CAL"]
    ),

    # --------------------------------------------------------
    # Student Development
    # --------------------------------------------------------

    (
        "Student Development",
        ["learner development", "student growth"]
    ),

    (
        "Leadership in Education",
        ["student leadership", "educational leadership"]
    ),

    (
        "Communication Skills",
        ["academic communication", "communication ability"]
    ),

    (
        "Presentation Skills",
        ["academic presentation", "presentation ability"]
    ),

    (
        "Teamwork",
        ["team collaboration", "group work"]
    ),

    (
        "Professional Skills",
        ["employability skills", "career skills"]
    ),

    (
        "Employability",
        ["career readiness", "work readiness"]
    ),

    (
        "Academic Career Development",
        ["student career development", "career planning"]
    ),
]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """
    Generate the complete Academic Studies knowledge base.
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