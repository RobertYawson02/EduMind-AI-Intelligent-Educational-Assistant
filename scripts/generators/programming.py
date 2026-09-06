"""
==============================================================
PROGRAMMING KNOWLEDGE GENERATOR
Version 3.0
==============================================================
"""

from __future__ import annotations

from .common import build_knowledge_family


CATEGORY = "Programming"


CONCEPTS = [

    # Programming foundations
    ("Programming", ["computer programming", "coding"]),
    ("Programming Language", ["programming languages"]),
    ("Source Code", ["source program"]),
    ("Machine Code", ["machine language"]),
    ("Object Code", ["object program"]),
    ("Programming Paradigm", ["programming paradigms"]),
    ("Procedural Programming", ["procedural programming"]),
    ("Object Oriented Programming", ["OOP", "object-oriented programming"]),
    ("Functional Programming", ["functional programming"]),
    ("Event Driven Programming", ["event-driven programming"]),
    ("Declarative Programming", ["declarative programming"]),

    # Python
    ("Python", ["Python programming", "Python language"]),
    ("Python Variable", ["Python variables"]),
    ("Python Data Types", ["Python types"]),
    ("Python List", ["Python lists"]),
    ("Python Tuple", ["Python tuples"]),
    ("Python Set", ["Python sets"]),
    ("Python Dictionary", ["Python dict"]),
    ("Python Function", ["Python functions"]),
    ("Python Module", ["Python modules"]),
    ("Python Package", ["Python packages"]),
    ("Python Exception Handling", ["Python exceptions"]),
    ("Python Class", ["Python classes"]),
    ("Python Object", ["Python objects"]),
    ("Python Loop", ["Python loops"]),
    ("Python Conditional", ["Python if statement"]),
    ("Python Comprehension", ["list comprehension"]),
    ("Python Virtual Environment", ["Python venv", "virtual environment"]),
    ("Python Package Manager", ["pip", "Python pip"]),

    # PHP
    ("PHP", ["PHP programming", "PHP language"]),
    ("PHP Variable", ["PHP variables"]),
    ("PHP Data Types", ["PHP types"]),
    ("PHP Function", ["PHP functions"]),
    ("PHP Array", ["PHP arrays"]),
    ("PHP Associative Array", ["PHP associative arrays"]),
    ("PHP Conditional Statement", ["PHP if statement"]),
    ("PHP Loop", ["PHP loops"]),
    ("PHP Form Processing", ["PHP forms"]),
    ("PHP Session", ["PHP sessions"]),
    ("PHP Cookie", ["PHP cookies"]),
    ("PHP Include", ["PHP include"]),
    ("PHP Require", ["PHP require"]),
    ("PHP Exception Handling", ["PHP exceptions"]),
    ("PHP Object Oriented Programming", ["PHP OOP"]),
    ("PHP Class", ["PHP classes"]),

    # JavaScript
    ("JavaScript", ["JS", "JavaScript programming"]),
    ("JavaScript Variable", ["JavaScript variables"]),
    ("JavaScript Data Types", ["JavaScript types"]),
    ("JavaScript Function", ["JavaScript functions"]),
    ("JavaScript Array", ["JavaScript arrays"]),
    ("JavaScript Object", ["JavaScript objects"]),
    ("JavaScript Promise", ["JavaScript promises"]),
    ("JavaScript Async Await", ["async await"]),
    ("JavaScript Event", ["JavaScript events"]),
    ("JavaScript DOM", ["DOM manipulation"]),
    ("JavaScript Event Listener", ["event listener"]),
    ("JavaScript JSON", ["JSON JavaScript"]),
    ("JavaScript Fetch API", ["fetch API"]),
    ("JavaScript Error Handling", ["JavaScript exceptions"]),
    ("JavaScript Class", ["JavaScript classes"]),

    # Java
    ("Java Programming", ["Java"]),
    ("Java Variable", ["Java variables"]),
    ("Java Data Types", ["Java types"]),
    ("Java Method", ["Java methods"]),
    ("Java Class", ["Java classes"]),
    ("Java Object", ["Java objects"]),
    ("Java Constructor", ["Java constructors"]),
    ("Java Inheritance", ["Java inheritance"]),
    ("Java Polymorphism", ["Java polymorphism"]),
    ("Java Encapsulation", ["Java encapsulation"]),
    ("Java Interface", ["Java interfaces"]),
    ("Java Exception Handling", ["Java exceptions"]),
    ("Java Package", ["Java packages"]),
    ("Java Array", ["Java arrays"]),
    ("Java Collection Framework", ["Java collections"]),

    # C / C++
    ("C Programming", ["C language", "C programming"]),
    ("C Variable", ["C variables"]),
    ("C Data Types", ["C types"]),
    ("C Function", ["C functions"]),
    ("C Pointer", ["C pointers"]),
    ("C Array", ["C arrays"]),
    ("C Structure", ["C structs"]),
    ("C File Handling", ["C files"]),
    ("C Memory Management", ["C memory"]),
    ("C++ Programming", ["C plus plus", "C++"]),
    ("C++ Class", ["C++ classes"]),
    ("C++ Object", ["C++ objects"]),
    ("C++ Constructor", ["C++ constructors"]),
    ("C++ Inheritance", ["C++ inheritance"]),
    ("C++ Polymorphism", ["C++ polymorphism"]),
    ("C++ Template", ["C++ templates"]),
    ("C++ STL", ["standard template library"]),

    # Core language concepts
    ("Variable", ["variables"]),
    ("Constant", ["constants"]),
    ("Literal", ["programming literals"]),
    ("Identifier", ["programming identifier"]),
    ("Keyword", ["reserved keyword"]),
    ("Data Type", ["data types"]),
    ("Integer", ["integer data type"]),
    ("Float", ["floating point"]),
    ("String", ["string data type"]),
    ("Boolean", ["boolean data type"]),
    ("Character", ["character data type"]),
    ("Null Value", ["null", "None"]),
    ("Type Conversion", ["type casting", "casting"]),
    ("Operator", ["programming operators"]),
    ("Arithmetic Operator", ["arithmetic operators"]),
    ("Relational Operator", ["comparison operators"]),
    ("Logical Operator", ["logical operators"]),
    ("Assignment Operator", ["assignment"]),
    ("Expression", ["programming expression"]),
    ("Statement", ["programming statement"]),
    ("Block", ["code block"]),

    # Control flow
    ("Conditional Statement", ["condition"]),
    ("If Statement", ["if"]),
    ("If Else Statement", ["if else"]),
    ("Nested If Statement", ["nested if"]),
    ("Switch Statement", ["switch case"]),
    ("For Loop", ["for loop"]),
    ("While Loop", ["while loop"]),
    ("Do While Loop", ["do while"]),
    ("Nested Loop", ["nested loops"]),
    ("Break Statement", ["break"]),
    ("Continue Statement", ["continue"]),
    ("Pass Statement", ["pass statement"]),

    # Functions
    ("Function", ["functions"]),
    ("Function Declaration", ["function declaration"]),
    ("Function Definition", ["function definition"]),
    ("Function Call", ["function invocation"]),
    ("Parameter", ["function parameter"]),
    ("Argument", ["function argument"]),
    ("Return Statement", ["return"]),
    ("Default Parameter", ["default arguments"]),
    ("Optional Parameter", ["optional arguments"]),
    ("Anonymous Function", ["lambda function", "anonymous function"]),
    ("Recursive Function", ["recursion function"]),

    # Errors
    ("Programming Error", ["software programming error"]),
    ("Syntax Error", ["syntax errors"]),
    ("Runtime Error", ["runtime errors"]),
    ("Logical Error", ["logic errors"]),
    ("Semantic Error", ["semantic errors"]),
    ("Compilation Error", ["compile error"]),
    ("Exception", ["programming exception"]),
    ("Exception Handling", ["exception handling"]),
    ("Error Handling", ["error handling"]),
    ("Debugging", ["debugging code"]),
    ("Debugger", ["debugger"]),
    ("Logging", ["application logging"]),

    # OOP
    ("Class", ["programming class"]),
    ("Object", ["programming object"]),
    ("Constructor", ["constructor"]),
    ("Destructor", ["destructor"]),
    ("Method", ["object method"]),
    ("Attribute", ["object attribute"]),
    ("Property", ["object property"]),
    ("Encapsulation", ["data encapsulation"]),
    ("Inheritance", ["class inheritance"]),
    ("Polymorphism", ["polymorphism"]),
    ("Abstraction", ["abstraction"]),
    ("Interface", ["programming interface"]),
    ("Abstract Class", ["abstract class"]),
    ("Method Overloading", ["overloading"]),
    ("Method Overriding", ["overriding"]),

    # Data structures
    ("Array", ["array"]),
    ("List", ["list"]),
    ("Tuple", ["tuple"]),
    ("Set", ["set"]),
    ("Dictionary", ["map", "dictionary"]),
    ("Stack", ["stack"]),
    ("Queue", ["queue"]),
    ("Linked List", ["linked list"]),
    ("Tree", ["tree"]),
    ("Graph", ["graph"]),
    ("Hash Table", ["hash table"]),
    ("Heap", ["heap"]),

    # Algorithms
    ("Algorithm", ["algorithms"]),
    ("Algorithm Design", ["algorithm design"]),
    ("Algorithm Analysis", ["algorithm analysis"]),
    ("Searching Algorithm", ["search algorithms"]),
    ("Sorting Algorithm", ["sorting algorithms"]),
    ("Linear Search", ["sequential search"]),
    ("Binary Search", ["binary search"]),
    ("Bubble Sort", ["bubble sort"]),
    ("Selection Sort", ["selection sort"]),
    ("Insertion Sort", ["insertion sort"]),
    ("Merge Sort", ["merge sort"]),
    ("Quick Sort", ["quick sort"]),
    ("Heap Sort", ["heap sort"]),
    ("Recursion", ["recursive programming"]),
    ("Iteration", ["iterative programming"]),
    ("Divide and Conquer", ["divide-and-conquer"]),
    ("Greedy Algorithm", ["greedy algorithms"]),
    ("Dynamic Programming", ["dynamic programming"]),
    ("Backtracking Algorithm", ["backtracking"]),

    # Complexity
    ("Time Complexity", ["algorithm complexity"]),
    ("Space Complexity", ["memory complexity"]),
    ("Big O Notation", ["Big O"]),
    ("Big Omega Notation", ["Big Omega"]),
    ("Big Theta Notation", ["Big Theta"]),
    ("Constant Time", ["O(1)"]),
    ("Linear Time", ["O(n)"]),
    ("Logarithmic Time", ["O(log n)"]),
    ("Quadratic Time", ["O(n squared)"]),

    # Software development
    ("Integrated Development Environment", ["IDE"]),
    ("Compiler", ["compiler"]),
    ("Interpreter", ["interpreter"]),
    ("Assembler", ["assembler"]),
    ("Library", ["programming library"]),
    ("Framework", ["software framework"]),
    ("Package", ["software package"]),
    ("Module", ["software module"]),
    ("API", ["application programming interface"]),
    ("SDK", ["software development kit"]),
    ("Dependency", ["software dependency"]),
    ("Package Manager", ["package management"]),
    ("Version Control", ["source control"]),
    ("Git", ["Git version control"]),
    ("GitHub", ["GitHub repository"]),
    ("Code Repository", ["source repository"]),
    ("Code Review", ["software code review"]),
    ("Unit Testing", ["unit tests"]),
    ("Test Driven Development", ["TDD"]),

    # Web programming
    ("Server Side Programming", ["server-side programming"]),
    ("Client Side Programming", ["client-side programming"]),
    ("API Programming", ["API development"]),
    ("REST API", ["RESTful API"]),
    ("JSON", ["JavaScript Object Notation"]),
    ("XML", ["Extensible Markup Language"]),
    ("HTTP Request", ["HTTP requests"]),
    ("Form Handling", ["web form processing"]),
    ("Authentication Programming", ["programmatic authentication"]),
    ("Database Programming", ["database application programming"]),

    # Advanced concepts
    ("Concurrency", ["concurrent programming"]),
    ("Parallel Programming", ["parallel computing"]),
    ("Multithreading", ["multi-threading"]),
    ("Asynchronous Programming", ["async programming"]),
    ("Synchronous Programming", ["synchronous execution"]),
    ("Memory Management", ["program memory management"]),
    ("Garbage Collection", ["automatic memory management"]),
    ("Pointer", ["memory pointer"]),
    ("Reference", ["object reference"]),
    ("Memory Leak", ["memory leaks"]),
    ("Race Condition", ["race conditions"]),
    ("Deadlock", ["programming deadlock"]),
    ("Software Design Pattern", ["design patterns"]),
    ("Model View Controller", ["MVC"]),
    ("Dependency Injection", ["DI"]),
    ("Clean Code", ["clean programming"]),
]


def generate() -> list[dict]:
    """Generate the Programming knowledge family."""

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


if __name__ == "__main__":

    records = generate()

    print("=" * 60)
    print("PROGRAMMING GENERATOR")
    print("=" * 60)
    print(f"Concepts : {len(CONCEPTS)}")
    print(f"Records  : {len(records)}")
    print("=" * 60)