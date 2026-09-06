"""
==============================================================
WEB DEVELOPMENT KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations

from .common import build_knowledge_family

CATEGORY = "Web Development"

CONCEPTS = [

    # HTML
    ("HTML", ["HyperText Markup Language"]),
    ("HTML Element", ["HTML tag"]),
    ("HTML Attribute", ["HTML attributes"]),
    ("Semantic HTML", ["semantic markup"]),
    ("HTML Form", ["web form"]),
    ("HTML Input", ["input element"]),
    ("HTML Table", ["table element"]),
    ("HTML List", ["ordered list", "unordered list"]),

    # CSS
    ("CSS", ["Cascading Style Sheets"]),
    ("CSS Selector", ["selectors"]),
    ("CSS Box Model", ["box model"]),
    ("CSS Flexbox", ["flex layout"]),
    ("CSS Grid", ["grid layout"]),
    ("Responsive Web Design", ["responsive design"]),
    ("Media Query", ["media queries"]),
    ("CSS Animation", ["web animation"]),

    # JavaScript
    ("JavaScript", ["JS"]),
    ("DOM", ["Document Object Model"]),
    ("Event Handling", ["JavaScript events"]),
    ("AJAX", ["Asynchronous JavaScript and XML"]),
    ("JSON", ["JavaScript Object Notation"]),
    ("Fetch API", ["fetch"]),
    ("Promise", ["JavaScript Promise"]),
    ("Async Await", ["asynchronous JavaScript"]),

    # Frontend
    ("Frontend Development", ["client-side development"]),
    ("Frontend Framework", ["frontend frameworks"]),
    ("Bootstrap", ["Bootstrap framework"]),
    ("React", ["ReactJS"]),
    ("Single Page Application", ["SPA"]),

    # Backend
    ("Backend Development", ["server-side development"]),
    ("PHP", ["PHP language"]),
    ("Flask", ["Python Flask"]),
    ("Laravel", ["Laravel framework"]),
    ("Web Server", ["server"]),
    ("Apache Server", ["Apache HTTP Server"]),
    ("XAMPP", ["XAMPP server"]),

    # APIs
    ("REST API", ["RESTful API"]),
    ("API Endpoint", ["endpoint"]),
    ("HTTP Request", ["request"]),
    ("HTTP Response", ["response"]),
    ("GET Request", ["GET"]),
    ("POST Request", ["POST"]),
    ("PUT Request", ["PUT"]),
    ("DELETE Request", ["DELETE"]),

    # Security
    ("Web Security", ["website security"]),
    ("HTTPS", ["secure HTTP"]),
    ("Authentication", ["web authentication"]),
    ("Session", ["web session"]),
    ("Cookie", ["browser cookie"]),
    ("Cross Site Scripting", ["XSS"]),
    ("Cross Site Request Forgery", ["CSRF"]),
    ("SQL Injection", ["SQLi"]),

    # Deployment
    ("Web Hosting", ["hosting"]),
    ("Domain Name", ["website domain"]),
    ("URL", ["Uniform Resource Locator"]),
    ("DNS", ["Domain Name System"]),
    ("Deployment", ["website deployment"]),
    ("Version Control", ["Git"]),
    ("GitHub Pages", ["GitHub hosting"]),
    ("SEO", ["Search Engine Optimization"])
]


def generate():
    records = []

    for topic, aliases in CONCEPTS:

        records.extend(
            build_knowledge_family(
                topic=topic,
                category=CATEGORY,
                aliases=aliases,
                education_level="university",
                difficulty="intermediate"
            )
        )

    return records


if __name__ == "__main__":

    print(f"Web Development Records: {len(generate())}")