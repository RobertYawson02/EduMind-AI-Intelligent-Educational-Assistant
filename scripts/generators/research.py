"""
==============================================================
RESEARCH METHODS KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations

from .common import build_knowledge_family

CATEGORY = "Research Methods"

CONCEPTS = [
    ("Research", ["academic research"]),
    ("Research Method", ["research methodology"]),
    ("Research Methodology", ["methodology"]),
    ("Research Problem", ["research problem"]),
    ("Research Question", ["research questions"]),
    ("Research Objective", ["research objectives"]),
    ("Research Aim", ["research aim"]),
    ("Research Topic", ["research topic"]),
    ("Research Proposal", ["proposal"]),
    ("Research Design", ["study design"]),
    ("Qualitative Research", ["qualitative study"]),
    ("Quantitative Research", ["quantitative study"]),
    ("Mixed Methods Research", ["mixed methods"]),
    ("Experimental Research", ["experiment"]),
    ("Descriptive Research", ["descriptive study"]),
    ("Exploratory Research", ["exploratory study"]),
    ("Case Study", ["case study research"]),
    ("Survey Research", ["survey"]),
    ("Literature Review", ["literature study"]),
    ("Systematic Review", ["systematic literature review"]),
    ("Primary Data", ["first-hand data"]),
    ("Secondary Data", ["existing data"]),
    ("Data Collection", ["collecting data"]),
    ("Questionnaire", ["survey questionnaire"]),
    ("Interview", ["research interview"]),
    ("Observation", ["observational research"]),
    ("Sampling", ["sample selection"]),
    ("Population", ["research population"]),
    ("Sample", ["research sample"]),
    ("Random Sampling", ["probability sampling"]),
    ("Stratified Sampling", ["stratified sample"]),
    ("Systematic Sampling", ["systematic sample"]),
    ("Convenience Sampling", ["convenience sample"]),
    ("Purposive Sampling", ["purposive sample"]),
    ("Sample Size", ["research sample size"]),
    ("Variable", ["research variable"]),
    ("Independent Variable", ["predictor variable"]),
    ("Dependent Variable", ["outcome variable"]),
    ("Control Variable", ["controlled variable"]),
    ("Hypothesis", ["research hypothesis"]),
    ("Null Hypothesis", ["H0"]),
    ("Alternative Hypothesis", ["H1"]),
    ("Validity", ["research validity"]),
    ("Reliability", ["research reliability"]),
    ("Ethical Research", ["research ethics"]),
    ("Informed Consent", ["participant consent"]),
    ("Confidentiality", ["research confidentiality"]),
    ("Data Analysis", ["research data analysis"]),
    ("Statistical Analysis", ["statistics"]),
    ("Correlation", ["correlation analysis"]),
    ("Regression", ["regression analysis"]),
    ("Hypothesis Testing", ["statistical testing"]),
    ("P Value", ["p-value"]),
    ("Confidence Interval", ["confidence interval"]),
    ("Research Findings", ["findings"]),
    ("Research Conclusion", ["conclusion"]),
    ("Research Recommendation", ["recommendations"]),
    ("Citation", ["source citation"]),
    ("Reference", ["references"]),
    ("Plagiarism", ["academic plagiarism"]),
    ("Research Report", ["research paper"]),
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