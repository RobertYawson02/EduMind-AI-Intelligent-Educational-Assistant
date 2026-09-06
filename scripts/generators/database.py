"""
==============================================================
DATABASE KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY = "Database Systems"

CONCEPTS = [

    ("Database", ["database system"]),
    ("Database Management System", ["DBMS"]),
    ("Relational Database", ["RDBMS"]),
    ("NoSQL Database", ["non-relational database"]),
    ("SQL", ["Structured Query Language"]),
    ("MySQL", ["MySQL database"]),
    ("PostgreSQL", ["Postgres"]),
    ("SQLite", ["SQLite database"]),
    ("MongoDB", ["document database"]),

    ("Table", ["database table"]),
    ("Record", ["row"]),
    ("Field", ["column"]),
    ("Primary Key", ["PK"]),
    ("Foreign Key", ["FK"]),
    ("Candidate Key", ["database key"]),
    ("Composite Key", ["combined key"]),
    ("Unique Key", ["unique constraint"]),

    ("Entity Relationship Diagram", ["ERD"]),
    ("Entity", ["database entity"]),
    ("Attribute", ["entity attribute"]),
    ("Relationship", ["entity relationship"]),
    ("Cardinality", ["relationship cardinality"]),

    ("Normalization", ["database normalization"]),
    ("First Normal Form", ["1NF"]),
    ("Second Normal Form", ["2NF"]),
    ("Third Normal Form", ["3NF"]),
    ("Boyce Codd Normal Form", ["BCNF"]),

    ("SQL SELECT", ["SELECT statement"]),
    ("SQL INSERT", ["INSERT statement"]),
    ("SQL UPDATE", ["UPDATE statement"]),
    ("SQL DELETE", ["DELETE statement"]),
    ("SQL WHERE", ["WHERE clause"]),
    ("SQL ORDER BY", ["sorting query"]),
    ("SQL GROUP BY", ["grouping query"]),
    ("SQL HAVING", ["HAVING clause"]),
    ("SQL JOIN", ["join operation"]),
    ("Inner Join", ["inner join"]),
    ("Left Join", ["left join"]),
    ("Right Join", ["right join"]),
    ("Full Join", ["full outer join"]),

    ("Database Transaction", ["transaction"]),
    ("ACID Properties", ["ACID"]),
    ("Database Index", ["index"]),
    ("Stored Procedure", ["stored procedures"]),
    ("Trigger", ["database trigger"]),
    ("View", ["database view"]),
    ("Schema", ["database schema"]),
    ("Backup", ["database backup"]),
    ("Recovery", ["database recovery"]),
    ("Database Security", ["DB security"])
]

def generate():
    records = []
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic, CATEGORY, aliases))
    return records