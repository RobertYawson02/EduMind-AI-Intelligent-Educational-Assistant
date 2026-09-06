"""
==============================================================
DATA SCIENCE & DATA ANALYTICS GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate structured educational knowledge for:
    - Data Science
    - Data Analysis
    - Statistics
    - Data Engineering
    - Data Visualization
    - Big Data
    - Business Intelligence
    - Machine Learning data preparation

Architecture:
    Uses common.py to generate educational knowledge
    while preserving the existing JSON schema.
"""

from __future__ import annotations

from .common import build_knowledge_family


CATEGORY = "Data Science and Data Analytics"


CONCEPTS = [

    # ========================================================
    # DATA SCIENCE FOUNDATIONS
    # ========================================================

    ("Data Science", ["data science"]),
    ("Data Analytics", ["data analytics"]),
    ("Data Analysis", ["data analysis"]),
    ("Data", ["information"]),
    ("Dataset", ["data set"]),
    ("Data Point", ["observation"]),
    ("Data Attribute", ["data feature"]),
    ("Data Variable", ["variable"]),
    ("Target Variable", ["dependent variable"]),
    ("Independent Variable", ["predictor variable"]),
    ("Dependent Variable", ["response variable"]),
    ("Data Science Lifecycle", ["data science process"]),
    ("Data Science Project", ["data project"]),
    ("Data Scientist", ["data science professional"]),
    ("Data Analyst", ["data analyst"]),
    ("Data Engineer", ["data engineering"]),
    ("Data Architect", ["data architecture"]),
    ("Data Professional", ["data specialist"]),

    # ========================================================
    # TYPES OF DATA
    # ========================================================

    ("Structured Data", ["structured dataset"]),
    ("Unstructured Data", ["unstructured dataset"]),
    ("Semi Structured Data", ["semi-structured data"]),
    ("Quantitative Data", ["numerical data"]),
    ("Qualitative Data", ["categorical information"]),
    ("Discrete Data", ["discrete variable"]),
    ("Continuous Data", ["continuous variable"]),
    ("Categorical Data", ["categorical variable"]),
    ("Nominal Data", ["nominal variable"]),
    ("Ordinal Data", ["ordinal variable"]),
    ("Time Series Data", ["time-series"]),
    ("Spatial Data", ["geospatial data"]),
    ("Text Data", ["textual data"]),
    ("Image Data", ["visual data"]),
    ("Audio Data", ["sound data"]),
    ("Video Data", ["video dataset"]),

    # ========================================================
    # DATA COLLECTION
    # ========================================================

    ("Data Collection", ["data gathering"]),
    ("Data Source", ["source of data"]),
    ("Primary Data", ["primary dataset"]),
    ("Secondary Data", ["secondary dataset"]),
    ("Survey Data", ["survey dataset"]),
    ("Questionnaire", ["data collection questionnaire"]),
    ("Interview Data", ["interview research"]),
    ("Observation Data", ["observational data"]),
    ("Experimental Data", ["experimental dataset"]),
    ("Web Data", ["internet data"]),
    ("Web Scraping", ["data scraping"]),
    ("API Data Collection", ["API data"]),
    ("Sensor Data", ["IoT sensor data"]),
    ("Database Data", ["database records"]),

    # ========================================================
    # DATA QUALITY
    # ========================================================

    ("Data Quality", ["quality of data"]),
    ("Data Accuracy", ["accurate data"]),
    ("Data Completeness", ["complete data"]),
    ("Data Consistency", ["consistent data"]),
    ("Data Validity", ["valid data"]),
    ("Data Timeliness", ["current data"]),
    ("Duplicate Data", ["duplicate records"]),
    ("Missing Data", ["missing values"]),
    ("Data Error", ["data errors"]),
    ("Data Noise", ["noisy data"]),
    ("Data Integrity", ["data integrity"]),
    ("Data Governance", ["data governance"]),

    # ========================================================
    # DATA CLEANING
    # ========================================================

    ("Data Cleaning", ["data cleansing"]),
    ("Data Preprocessing", ["data preprocessing"]),
    ("Missing Value Handling", ["missing value treatment"]),
    ("Missing Value Imputation", ["data imputation"]),
    ("Mean Imputation", ["mean value imputation"]),
    ("Median Imputation", ["median imputation"]),
    ("Mode Imputation", ["mode imputation"]),
    ("Duplicate Removal", ["removing duplicate records"]),
    ("Data Validation", ["data validation process"]),
    ("Data Transformation", ["data transformation"]),
    ("Data Standardization", ["data standardization"]),
    ("Data Normalization", ["data normalization"]),
    ("Outlier Detection", ["detecting outliers"]),
    ("Outlier Treatment", ["handling outliers"]),

    # ========================================================
    # EXPLORATORY DATA ANALYSIS
    # ========================================================

    ("Exploratory Data Analysis", ["EDA"]),
    ("Data Profiling", ["data profile"]),
    ("Descriptive Statistics", ["descriptive analysis"]),
    ("Summary Statistics", ["statistical summary"]),
    ("Frequency Distribution", ["frequency table"]),
    ("Cross Tabulation", ["crosstab"]),
    ("Data Distribution", ["distribution analysis"]),
    ("Pattern Detection", ["pattern analysis"]),
    ("Trend Analysis", ["trend detection"]),
    ("Relationship Analysis", ["relationship between variables"]),

    # ========================================================
    # STATISTICS
    # ========================================================

    ("Statistics", ["statistical science"]),
    ("Population", ["statistical population"]),
    ("Sample", ["statistical sample"]),
    ("Parameter", ["population parameter"]),
    ("Statistic", ["sample statistic"]),
    ("Mean", ["arithmetic mean", "average"]),
    ("Median", ["middle value"]),
    ("Mode", ["most frequent value"]),
    ("Range", ["statistical range"]),
    ("Variance", ["statistical variance"]),
    ("Standard Deviation", ["statistical standard deviation"]),
    ("Quartile", ["quartiles"]),
    ("Percentile", ["percentiles"]),
    ("Interquartile Range", ["IQR"]),
    ("Z Score", ["standard score"]),
    ("Coefficient of Variation", ["CV"]),
    ("Skewness", ["distribution skewness"]),
    ("Kurtosis", ["distribution kurtosis"]),

    # ========================================================
    # PROBABILITY
    # ========================================================

    ("Probability", ["probability theory"]),
    ("Random Variable", ["random variables"]),
    ("Probability Distribution", ["probability model"]),
    ("Normal Distribution", ["Gaussian distribution"]),
    ("Binomial Distribution", ["binomial probability"]),
    ("Poisson Distribution", ["Poisson probability"]),
    ("Uniform Distribution", ["uniform probability"]),
    ("Conditional Probability", ["conditional probability"]),
    ("Independent Events", ["independent probability"]),
    ("Dependent Events", ["dependent probability"]),
    ("Expected Value", ["mathematical expectation"]),
    ("Bayes Theorem", ["Bayesian theorem"]),
    ("Probability Density Function", ["PDF"]),
    ("Cumulative Distribution Function", ["CDF"]),

    # ========================================================
    # CORRELATION
    # ========================================================

    ("Correlation", ["statistical correlation"]),
    ("Pearson Correlation", ["Pearson coefficient"]),
    ("Spearman Correlation", ["Spearman rank correlation"]),
    ("Correlation Coefficient", ["correlation value"]),
    ("Positive Correlation", ["direct correlation"]),
    ("Negative Correlation", ["inverse correlation"]),
    ("Zero Correlation", ["no correlation"]),
    ("Correlation Matrix", ["correlation table"]),

    # ========================================================
    # REGRESSION
    # ========================================================

    ("Regression Analysis", ["regression"]),
    ("Linear Regression", ["simple linear regression"]),
    ("Multiple Linear Regression", ["multiple regression"]),
    ("Polynomial Regression", ["polynomial model"]),
    ("Logistic Regression", ["logistic model"]),
    ("Regression Coefficient", ["regression coefficient"]),
    ("Regression Line", ["best fit line"]),
    ("Least Squares Method", ["ordinary least squares"]),
    ("Residual", ["regression residual"]),
    ("Residual Analysis", ["residual analysis"]),

    # ========================================================
    # HYPOTHESIS TESTING
    # ========================================================

    ("Hypothesis Testing", ["statistical hypothesis testing"]),
    ("Null Hypothesis", ["H0"]),
    ("Alternative Hypothesis", ["H1"]),
    ("P Value", ["p-value"]),
    ("Significance Level", ["alpha level"]),
    ("Confidence Interval", ["confidence intervals"]),
    ("Type I Error", ["false positive"]),
    ("Type II Error", ["false negative"]),
    ("Statistical Significance", ["significant result"]),
    ("T Test", ["Student t-test"]),
    ("Z Test", ["z-test"]),
    ("Chi Square Test", ["chi-squared test"]),
    ("ANOVA", ["analysis of variance"]),

    # ========================================================
    # DATA VISUALIZATION
    # ========================================================

    ("Data Visualization", ["data visualisation"]),
    ("Chart", ["data chart"]),
    ("Graph", ["data graph"]),
    ("Bar Chart", ["bar graph"]),
    ("Line Chart", ["line graph"]),
    ("Pie Chart", ["pie graph"]),
    ("Histogram", ["frequency histogram"]),
    ("Scatter Plot", ["scatter graph"]),
    ("Box Plot", ["box-and-whisker plot"]),
    ("Area Chart", ["area graph"]),
    ("Heat Map", ["heatmap"]),
    ("Bubble Chart", ["bubble graph"]),
    ("Radar Chart", ["spider chart"]),
    ("Tree Map", ["treemap"]),
    ("Geographical Map", ["map visualization"]),
    ("Dashboard", ["data dashboard"]),
    ("Interactive Dashboard", ["interactive data dashboard"]),
    ("Data Storytelling", ["data storytelling"]),

    # ========================================================
    # PYTHON DATA SCIENCE
    # ========================================================

    ("Python for Data Science", ["Python data analysis"]),
    ("Pandas", ["Python pandas"]),
    ("Pandas DataFrame", ["DataFrame"]),
    ("Pandas Series", ["Series"]),
    ("NumPy", ["numerical Python"]),
    ("NumPy Array", ["numpy array"]),
    ("Matplotlib", ["Python visualization"]),
    ("Seaborn", ["statistical visualization"]),
    ("Scikit Learn", ["sklearn"]),
    ("Jupyter Notebook", ["Jupyter"]),
    ("Python Data Analysis", ["data analysis with Python"]),

    # ========================================================
    # DATA ANALYSIS OPERATIONS
    # ========================================================

    ("Data Filtering", ["filtering data"]),
    ("Data Sorting", ["sorting data"]),
    ("Data Grouping", ["grouping data"]),
    ("Data Aggregation", ["aggregating data"]),
    ("Data Merging", ["merging datasets"]),
    ("Data Joining", ["joining datasets"]),
    ("Data Pivoting", ["pivot table"]),
    ("Data Reshaping", ["reshape data"]),
    ("Data Sampling", ["sampling data"]),
    ("Random Sampling", ["random sample"]),
    ("Stratified Sampling", ["stratified sample"]),
    ("Systematic Sampling", ["systematic sample"]),
    ("Cluster Sampling", ["cluster sample"]),
    ("Convenience Sampling", ["convenience sample"]),

    # ========================================================
    # BIG DATA
    # ========================================================

    ("Big Data", ["large-scale data"]),
    ("Big Data Analytics", ["large data analytics"]),
    ("Big Data Processing", ["large-scale data processing"]),
    ("Hadoop", ["Apache Hadoop"]),
    ("HDFS", ["Hadoop Distributed File System"]),
    ("MapReduce", ["Hadoop MapReduce"]),
    ("YARN", ["Yet Another Resource Negotiator"]),
    ("Apache Spark", ["Spark"]),
    ("Spark DataFrame", ["Spark dataframe"]),
    ("Spark SQL", ["distributed SQL"]),
    ("Data Lake", ["data lake architecture"]),
    ("Data Lakehouse", ["lakehouse"]),
    ("Data Warehouse", ["data warehouse"]),
    ("Data Mart", ["data mart"]),

    # ========================================================
    # BUSINESS INTELLIGENCE
    # ========================================================

    ("Business Intelligence", ["BI"]),
    ("Business Analytics", ["business data analytics"]),
    ("Power BI", ["Microsoft Power BI"]),
    ("Power BI Dashboard", ["BI dashboard"]),
    ("Power Query", ["data transformation Power Query"]),
    ("DAX", ["Data Analysis Expressions"]),
    ("DAX Measure", ["Power BI measure"]),
    ("DAX Calculated Column", ["calculated column"]),
    ("Key Performance Indicator", ["KPI"]),
    ("Business Metric", ["business metrics"]),
    ("Reporting", ["business reporting"]),
    ("Data Driven Decision Making", ["data-driven decisions"]),

    # ========================================================
    # DATA ENGINEERING
    # ========================================================

    ("Data Engineering", ["data engineer"]),
    ("Data Pipeline", ["data processing pipeline"]),
    ("ETL", ["extract transform load"]),
    ("ELT", ["extract load transform"]),
    ("Extract Transform Load", ["ETL process"]),
    ("Data Integration", ["data integration"]),
    ("Data Ingestion", ["data ingestion"]),
    ("Batch Processing", ["batch data processing"]),
    ("Stream Processing", ["real-time data processing"]),
    ("Real Time Analytics", ["real-time analytics"]),
    ("Data Workflow", ["data workflow"]),
    ("Workflow Orchestration", ["data orchestration"]),
    ("Apache Airflow", ["Airflow"]),
    ("Data Pipeline Monitoring", ["pipeline monitoring"]),

    # ========================================================
    # DATA STORAGE
    # ========================================================

    ("Data Storage", ["storing data"]),
    ("Relational Data Storage", ["relational storage"]),
    ("NoSQL Data Storage", ["NoSQL storage"]),
    ("Cloud Data Storage", ["cloud storage"]),
    ("Object Storage", ["object-based storage"]),
    ("Data Warehouse Architecture", ["warehouse architecture"]),
    ("Data Lake Architecture", ["lake architecture"]),
    ("Columnar Storage", ["column storage"]),
    ("Distributed Storage", ["distributed data storage"]),

    # ========================================================
    # DATA SECURITY
    # ========================================================

    ("Data Security", ["data protection"]),
    ("Data Privacy", ["privacy protection"]),
    ("Data Encryption", ["encrypted data"]),
    ("Access Control for Data", ["data access control"]),
    ("Data Masking", ["masking sensitive data"]),
    ("Data Anonymization", ["anonymized data"]),
    ("Data De Identification", ["de-identification"]),
    ("Sensitive Data", ["sensitive information"]),
    ("Personally Identifiable Information", ["PII"]),
    ("Data Breach", ["data security breach"]),

    # ========================================================
    # DATA SCIENCE APPLICATIONS
    # ========================================================

    ("Predictive Analytics", ["predictive data analysis"]),
    ("Descriptive Analytics", ["descriptive data analysis"]),
    ("Diagnostic Analytics", ["diagnostic data analysis"]),
    ("Prescriptive Analytics", ["prescriptive data analysis"]),
    ("Customer Analytics", ["customer data analysis"]),
    ("Healthcare Analytics", ["health data analytics"]),
    ("Financial Analytics", ["finance analytics"]),
    ("Educational Analytics", ["education data analytics"]),
    ("Sports Analytics", ["sports data analysis"]),
    ("Marketing Analytics", ["marketing data analysis"]),
    ("Fraud Detection", ["data-driven fraud detection"]),
    ("Risk Analytics", ["risk data analysis"]),
    ("Forecasting", ["data forecasting"]),
    ("Demand Forecasting", ["demand prediction"]),
    ("Time Series Forecasting", ["time-series prediction"]),

    # ========================================================
    # DATA SCIENCE PROJECT PRACTICE
    # ========================================================

    ("Data Science Project", ["data science workflow"]),
    ("Problem Definition", ["define analytical problem"]),
    ("Data Understanding", ["understand dataset"]),
    ("Data Preparation", ["prepare data"]),
    ("Model Development", ["develop analytical model"]),
    ("Model Evaluation", ["evaluate model"]),
    ("Data Science Reporting", ["analytical report"]),
    ("Reproducible Data Analysis", ["reproducible analysis"]),
    ("Data Documentation", ["documenting data"]),
]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """
    Generate Data Science and Data Analytics records.
    """

    records = []

    for topic, aliases in CONCEPTS:

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


# ============================================================
# DIRECT EXECUTION
# ============================================================

if __name__ == "__main__":

    records = generate()

    print("=" * 60)
    print("DATA SCIENCE GENERATOR")
    print("=" * 60)
    print(f"Concepts : {len(CONCEPTS)}")
    print(f"Records  : {len(records)}")
    print("=" * 60)