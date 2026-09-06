"""
==============================================================
SOFTWARE ENGINEERING GENERATOR
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY="Software Engineering"

CONCEPTS=[

("Software Engineering",["software development"]),
("Software Development Life Cycle",["SDLC"]),
("Requirement Analysis",["requirements"]),
("Functional Requirement",["functional requirements"]),
("Non Functional Requirement",["non-functional requirements"]),

("Waterfall Model",["waterfall"]),
("Agile Methodology",["Agile"]),
("Scrum",["Scrum framework"]),
("Sprint",["Scrum sprint"]),
("Kanban",["Kanban board"]),
("Prototype Model",["prototype"]),
("Spiral Model",["spiral development"]),

("Software Architecture",["system architecture"]),
("Software Design",["software design"]),
("UML",["Unified Modeling Language"]),
("Use Case Diagram",["use case"]),
("Class Diagram",["class diagram"]),
("Sequence Diagram",["sequence diagram"]),
("Activity Diagram",["activity diagram"]),
("Data Flow Diagram",["DFD"]),

("Version Control",["Git"]),
("GitHub",["GitHub repository"]),
("Code Review",["code review"]),
("Continuous Integration",["CI"]),
("Continuous Deployment",["CD"]),

("Unit Testing",["unit tests"]),
("Integration Testing",["integration tests"]),
("System Testing",["system tests"]),
("Acceptance Testing",["acceptance tests"]),
("Regression Testing",["regression tests"]),

("Software Maintenance",["maintenance"]),
("Software Documentation",["documentation"]),
("Bug Tracking",["issue tracking"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records