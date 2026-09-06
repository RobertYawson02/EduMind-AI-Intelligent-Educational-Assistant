"""
==============================================================
MATHEMATICS KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY = "Mathematics"

CONCEPTS = [

    # Arithmetic
    ("Mathematics", ["math", "mathematics"]),
    ("Number", ["numbers"]),
    ("Integer", ["whole number"]),
    ("Natural Number", ["counting number"]),
    ("Prime Number", ["prime"]),
    ("Composite Number", ["composite"]),
    ("Fraction", ["fractions"]),
    ("Decimal", ["decimals"]),
    ("Percentage", ["percent"]),
    ("Ratio", ["ratios"]),
    ("Proportion", ["proportions"]),

    # Algebra
    ("Algebra", ["algebraic mathematics"]),
    ("Variable", ["algebra variable"]),
    ("Constant", ["algebra constant"]),
    ("Expression", ["algebraic expression"]),
    ("Equation", ["mathematical equation"]),
    ("Linear Equation", ["linear equations"]),
    ("Quadratic Equation", ["quadratic"]),
    ("Polynomial", ["polynomials"]),
    ("Factorization", ["factoring"]),
    ("Simultaneous Equation", ["system of equations"]),

    # Functions
    ("Function", ["mathematical function"]),
    ("Domain", ["function domain"]),
    ("Range", ["function range"]),
    ("Graph of a Function", ["function graph"]),
    ("Inverse Function", ["inverse"]),
    ("Exponential Function", ["exponential"]),
    ("Logarithm", ["logarithms"]),

    # Geometry
    ("Geometry", ["geometric mathematics"]),
    ("Triangle", ["triangles"]),
    ("Circle", ["circles"]),
    ("Rectangle", ["rectangles"]),
    ("Square", ["squares"]),
    ("Polygon", ["polygons"]),
    ("Perimeter", ["shape perimeter"]),
    ("Area", ["surface area"]),
    ("Volume", ["3D volume"]),
    ("Pythagorean Theorem", ["Pythagoras theorem"]),

    # Trigonometry
    ("Trigonometry", ["trig"]),
    ("Sine", ["sin"]),
    ("Cosine", ["cos"]),
    ("Tangent", ["tan"]),
    ("Unit Circle", ["unit circle"]),
    ("Trigonometric Identity", ["trig identity"]),

    # Calculus
    ("Calculus", ["calculus mathematics"]),
    ("Limit", ["limits"]),
    ("Derivative", ["differentiation"]),
    ("Integration", ["integral"]),
    ("Differential Equation", ["ODE"]),
    ("Partial Derivative", ["multivariable derivative"]),

    # Statistics
    ("Statistics", ["statistical mathematics"]),
    ("Mean", ["average"]),
    ("Median", ["middle value"]),
    ("Mode", ["most frequent value"]),
    ("Variance", ["statistical variance"]),
    ("Standard Deviation", ["standard deviation"]),
    ("Probability", ["probability theory"]),
    ("Normal Distribution", ["Gaussian distribution"]),
    ("Z Score", ["standard score"]),

    # Linear Algebra
    ("Matrix", ["matrices"]),
    ("Vector", ["vectors"]),
    ("Determinant", ["matrix determinant"]),
    ("Eigenvalue", ["eigenvalues"]),
    ("Eigenvector", ["eigenvectors"]),
    ("Linear Transformation", ["linear transformations"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records

if __name__ == "__main__":
    print(f"Mathematics Records: {len(generate())}")

# Advanced Mathematics
("Complex Number",["complex numbers"]),
("Imaginary Number",["imaginary numbers"]),
("Sequence",["mathematical sequence"]),
("Arithmetic Sequence",["AP"]),
("Geometric Sequence",["GP"]),
("Series",["mathematical series"]),
("Binomial Theorem",["binomial expansion"]),
("Coordinate Geometry",["analytic geometry"]),
("Vector Space",["vector spaces"]),
("Dot Product",["scalar product"]),
("Cross Product",["vector product"]),
("Determinant",["matrix determinant"]),
("Probability Distribution",["statistical distribution"]),
("Normal Distribution",["Gaussian distribution"]),
("Standard Error",["sampling error"]),
("Hypothesis Testing",["statistical hypothesis testing"]),
("Confidence Interval",["confidence intervals"]),
("Permutation",["permutations"]),
("Combination",["combinations"])