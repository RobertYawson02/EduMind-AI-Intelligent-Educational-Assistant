"""
==============================================================
BUSINESS KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY = "Business"

CONCEPTS = [

    # Business foundations
    ("Business", ["business studies"]),
    ("Entrepreneurship", ["entrepreneur"]),
    ("Business Plan", ["business planning"]),
    ("Startup", ["new business"]),
    ("Innovation", ["business innovation"]),

    # Management
    ("Management", ["business management"]),
    ("Leadership", ["organizational leadership"]),
    ("Planning", ["management planning"]),
    ("Organizing", ["organization"]),
    ("Staffing", ["human resources"]),
    ("Directing", ["management direction"]),
    ("Controlling", ["management control"]),
    ("Decision Making", ["business decision making"]),

    # Marketing
    ("Marketing", ["business marketing"]),
    ("Market Research", ["marketing research"]),
    ("Target Market", ["customer target"]),
    ("Branding", ["brand management"]),
    ("Advertising", ["business advertising"]),
    ("Promotion", ["sales promotion"]),
    ("Digital Marketing", ["online marketing"]),

    # Accounting
    ("Accounting", ["financial accounting"]),
    ("Bookkeeping", ["financial records"]),
    ("Asset", ["business asset"]),
    ("Liability", ["business liability"]),
    ("Equity", ["owner equity"]),
    ("Income Statement", ["profit and loss"]),
    ("Balance Sheet", ["financial position"]),
    ("Cash Flow", ["cash flow statement"]),

    # Economics
    ("Economics", ["economic studies"]),
    ("Supply", ["market supply"]),
    ("Demand", ["market demand"]),
    ("Inflation", ["price inflation"]),
    ("Deflation", ["price deflation"]),
    ("Gross Domestic Product", ["GDP"]),
    ("Opportunity Cost", ["economic opportunity cost"]),
    ("Market Economy", ["free market"]),

    # Finance
    ("Finance", ["business finance"]),
    ("Budget", ["financial budget"]),
    ("Investment", ["business investment"]),
    ("Profit", ["business profit"]),
    ("Revenue", ["business revenue"]),
    ("Expense", ["business expense"]),
    ("Break Even Point", ["break-even analysis"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records