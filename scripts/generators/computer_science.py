"""
==============================================================
COMPUTER SCIENCE KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Curated Computer Science concepts for the Intelligent
    Educational Assistant.

Architecture:
    This module uses common.py to generate structured
    educational knowledge families.

Output records remain compatible with the existing
educational_knowledge.json retrieval architecture.
"""

from __future__ import annotations

from .common import build_knowledge_family


CATEGORY = "Computer Science"


# ============================================================
# CURATED COMPUTER SCIENCE CONCEPTS
# ============================================================

CONCEPTS = [

    # --------------------------------------------------------
    # FOUNDATIONS
    # --------------------------------------------------------

    ("Computer Science", ["computing", "computer science"]),
    ("Computational Thinking", ["computational thinking"]),
    ("Information Technology", ["IT", "information technology"]),
    ("Computer", ["computing device", "computer system"]),
    ("Computer System", ["computing system"]),
    ("Computer Architecture", ["computer organization"]),
    ("Computer Organization", ["computer architecture"]),
    ("Hardware", ["computer hardware"]),
    ("Software", ["computer software"]),
    ("System Software", ["system software"]),
    ("Application Software", ["application software"]),
    ("Utility Software", ["utility program"]),
    ("Firmware", ["embedded software", "firmware"]),
    ("Input Device", ["input hardware"]),
    ("Output Device", ["output hardware"]),
    ("Storage Device", ["storage hardware"]),
    ("Peripheral Device", ["computer peripheral"]),
    ("Central Processing Unit", ["CPU", "processor"]),
    ("Arithmetic Logic Unit", ["ALU"]),
    ("Control Unit", ["CU"]),
    ("Registers", ["CPU registers"]),
    ("Cache Memory", ["CPU cache"]),
    ("Main Memory", ["primary memory"]),
    ("Secondary Storage", ["secondary memory"]),
    ("Random Access Memory", ["RAM"]),
    ("Read Only Memory", ["ROM"]),
    ("Virtual Memory", ["virtual memory"]),

    # --------------------------------------------------------
    # ALGORITHMS AND PROBLEM SOLVING
    # --------------------------------------------------------

    ("Algorithm", ["algorithm", "problem solving algorithm"]),
    ("Algorithm Design", ["algorithm design"]),
    ("Algorithm Analysis", ["algorithm analysis"]),
    ("Pseudocode", ["pseudo code"]),
    ("Flowchart", ["flow chart"]),
    ("Decision Table", ["decision table"]),
    ("Problem Solving", ["computational problem solving"]),
    ("Divide and Conquer", ["divide and conquer"]),
    ("Greedy Algorithm", ["greedy method"]),
    ("Dynamic Programming", ["dynamic programming"]),
    ("Backtracking", ["backtracking algorithm"]),
    ("Brute Force Algorithm", ["brute force"]),
    ("Recursive Algorithm", ["recursion algorithm"]),
    ("Iterative Algorithm", ["iteration algorithm"]),
    ("Searching Algorithm", ["search algorithm"]),
    ("Sorting Algorithm", ["sort algorithm"]),

    # --------------------------------------------------------
    # DATA STRUCTURES
    # --------------------------------------------------------

    ("Data Structure", ["data structures"]),
    ("Array", ["array data structure"]),
    ("Linked List", ["linked list"]),
    ("Singly Linked List", ["single linked list"]),
    ("Doubly Linked List", ["double linked list"]),
    ("Circular Linked List", ["circular list"]),
    ("Stack", ["stack data structure"]),
    ("Queue", ["queue data structure"]),
    ("Circular Queue", ["circular queue"]),
    ("Priority Queue", ["priority queue"]),
    ("Deque", ["double ended queue"]),
    ("Tree", ["tree data structure"]),
    ("Binary Tree", ["binary tree"]),
    ("Binary Search Tree", ["BST"]),
    ("AVL Tree", ["AVL"]),
    ("Heap", ["heap data structure"]),
    ("Min Heap", ["minimum heap"]),
    ("Max Heap", ["maximum heap"]),
    ("Graph", ["graph data structure"]),
    ("Directed Graph", ["directed graph"]),
    ("Undirected Graph", ["undirected graph"]),
    ("Hash Table", ["hash table", "hash map"]),
    ("Hash Function", ["hashing"]),
    ("Set Data Structure", ["set"]),

    # --------------------------------------------------------
    # SEARCHING AND SORTING
    # --------------------------------------------------------

    ("Linear Search", ["sequential search"]),
    ("Binary Search", ["binary search"]),
    ("Bubble Sort", ["bubble sorting"]),
    ("Selection Sort", ["selection sorting"]),
    ("Insertion Sort", ["insertion sorting"]),
    ("Merge Sort", ["merge sorting"]),
    ("Quick Sort", ["quick sorting"]),
    ("Heap Sort", ["heap sorting"]),
    ("Counting Sort", ["counting sort"]),
    ("Radix Sort", ["radix sorting"]),

    # --------------------------------------------------------
    # COMPLEXITY
    # --------------------------------------------------------

    ("Time Complexity", ["algorithm time complexity"]),
    ("Space Complexity", ["algorithm space complexity"]),
    ("Big O Notation", ["Big O", "O notation"]),
    ("Big Omega Notation", ["Big Omega", "Ω notation"]),
    ("Big Theta Notation", ["Big Theta", "Θ notation"]),
    ("Constant Time Complexity", ["O(1)"]),
    ("Linear Time Complexity", ["O(n)"]),
    ("Logarithmic Time Complexity", ["O(log n)"]),
    ("Quadratic Time Complexity", ["O(n²)"]),

    # --------------------------------------------------------
    # PROGRAMMING CONCEPTS
    # --------------------------------------------------------

    ("Programming", ["computer programming"]),
    ("Programming Language", ["programming languages"]),
    ("Source Code", ["source program"]),
    ("Machine Code", ["machine language"]),
    ("Object Code", ["object program"]),
    ("Compiler", ["compiler"]),
    ("Interpreter", ["interpreter"]),
    ("Assembler", ["assembly translator"]),
    ("Syntax", ["programming syntax"]),
    ("Syntax Error", ["syntax error"]),
    ("Runtime Error", ["runtime error"]),
    ("Logical Error", ["logic error"]),
    ("Debugging", ["debug"]),
    ("Integrated Development Environment", ["IDE"]),

    # --------------------------------------------------------
    # OPERATING SYSTEMS
    # --------------------------------------------------------

    ("Operating System", ["OS", "operating systems"]),
    ("Kernel", ["OS kernel"]),
    ("Process", ["computer process"]),
    ("Thread", ["execution thread"]),
    ("Process Management", ["process management"]),
    ("Thread Management", ["thread management"]),
    ("CPU Scheduling", ["processor scheduling"]),
    ("Process Scheduling", ["process scheduler"]),
    ("Memory Management", ["OS memory management"]),
    ("File Management", ["file system management"]),
    ("Device Management", ["device management"]),
    ("System Call", ["system calls"]),
    ("Deadlock", ["deadlock in operating systems"]),
    ("Process Synchronization", ["process synchronization"]),
    ("Multitasking", ["multitasking OS"]),
    ("Multiprocessing", ["multiprocessing"]),
    ("Multiprogramming", ["multiprogramming"]),
    ("Batch Processing", ["batch operating system"]),
    ("Real Time Operating System", ["RTOS"]),
    ("Distributed Operating System", ["distributed OS"]),
    ("Command Line Interface", ["CLI"]),
    ("Graphical User Interface", ["GUI"]),

    # --------------------------------------------------------
    # SOFTWARE ENGINEERING
    # --------------------------------------------------------

    ("Software Engineering", ["software engineering"]),
    ("Software Development", ["software development"]),
    ("Software Development Life Cycle", ["SDLC"]),
    ("Software Requirement", ["software requirements"]),
    ("Requirement Analysis", ["requirements engineering"]),
    ("Functional Requirement", ["functional requirements"]),
    ("Non Functional Requirement", ["non-functional requirements"]),
    ("System Design", ["software system design"]),
    ("Software Architecture", ["software architecture"]),
    ("Software Testing", ["software tests"]),
    ("Unit Testing", ["unit test"]),
    ("Integration Testing", ["integration test"]),
    ("System Testing", ["system test"]),
    ("Acceptance Testing", ["acceptance test"]),
    ("Regression Testing", ["regression test"]),
    ("Software Maintenance", ["software maintenance"]),
    ("Software Documentation", ["software documentation"]),
    ("Version Control", ["version control system"]),
    ("Git", ["git version control"]),
    ("GitHub", ["github"]),
    ("Agile Methodology", ["agile"]),
    ("Scrum", ["scrum framework"]),
    ("Sprint", ["scrum sprint"]),
    ("Kanban", ["kanban"]),
    ("Waterfall Model", ["waterfall software model"]),
    ("Prototype Model", ["prototype development model"]),
    ("Spiral Model", ["spiral software model"]),

    # --------------------------------------------------------
    # OBJECT ORIENTED PROGRAMMING
    # --------------------------------------------------------

    ("Object Oriented Programming", ["OOP"]),
    ("Class", ["programming class"]),
    ("Object", ["programming object"]),
    ("Encapsulation", ["OOP encapsulation"]),
    ("Inheritance", ["OOP inheritance"]),
    ("Polymorphism", ["OOP polymorphism"]),
    ("Abstraction", ["OOP abstraction"]),
    ("Constructor", ["class constructor"]),
    ("Method", ["object method"]),
    ("Interface", ["programming interface"]),
    ("Association", ["object association"]),
    ("Aggregation", ["object aggregation"]),
    ("Composition", ["object composition"]),

    # --------------------------------------------------------
    # DATABASE AND INFORMATION SYSTEMS
    # --------------------------------------------------------

    ("Database", ["database system"]),
    ("Database Management System", ["DBMS"]),
    ("Information System", ["information systems"]),
    ("Database System", ["database architecture"]),
    ("Data Model", ["database model"]),
    ("Relational Model", ["relational database model"]),
    ("Entity", ["database entity"]),
    ("Attribute", ["database attribute"]),
    ("Relationship", ["database relationship"]),
    ("Primary Key", ["primary key"]),
    ("Foreign Key", ["foreign key"]),
    ("Database Schema", ["database schema"]),
    ("Database Transaction", ["database transaction"]),
    ("Database Index", ["database indexing"]),
    ("Database Security", ["database security"]),
    ("Database Backup", ["database backup"]),
    ("Database Recovery", ["database recovery"]),

    # --------------------------------------------------------
    # NETWORKING FOUNDATIONS
    # --------------------------------------------------------

    ("Computer Network", ["computer networking"]),
    ("Network Protocol", ["network protocols"]),
    ("Network Topology", ["network topology"]),
    ("Local Area Network", ["LAN"]),
    ("Wide Area Network", ["WAN"]),
    ("Metropolitan Area Network", ["MAN"]),
    ("Personal Area Network", ["PAN"]),
    ("Wireless Local Area Network", ["WLAN"]),
    ("Internet", ["global network"]),
    ("Intranet", ["private network"]),
    ("Extranet", ["business extranet"]),
    ("Router", ["network router"]),
    ("Switch", ["network switch"]),
    ("Hub", ["network hub"]),
    ("Bridge", ["network bridge"]),
    ("Gateway", ["network gateway"]),
    ("Repeater", ["network repeater"]),
    ("Modem", ["network modem"]),
    ("Access Point", ["wireless access point"]),
    ("Network Interface Card", ["NIC"]),
    ("IP Address", ["internet protocol address"]),
    ("MAC Address", ["MAC"]),
    ("IPv4", ["internet protocol version 4"]),
    ("IPv6", ["internet protocol version 6"]),
    ("DNS", ["domain name system"]),
    ("DHCP", ["dynamic host configuration protocol"]),

    # --------------------------------------------------------
    # COMPUTING ETHICS AND SOCIETY
    # --------------------------------------------------------

    ("Computer Ethics", ["computing ethics"]),
    ("Digital Citizenship", ["digital citizenship"]),
    ("Privacy", ["data privacy"]),
    ("Data Protection", ["personal data protection"]),
    ("Intellectual Property", ["IP rights"]),
    ("Copyright", ["copyright law"]),
    ("Software Licensing", ["software license"]),
    ("Open Source Software", ["open source"]),
    ("Digital Divide", ["technology access gap"]),
    ("Accessibility", ["computer accessibility"]),
    ("Artificial Intelligence", ["AI"]),
    ("Cybersecurity", ["computer security"]),
]


# ============================================================
# GENERATE KNOWLEDGE
# ============================================================

def generate() -> list[dict]:
    """
    Generate the complete Computer Science knowledge family.
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
# DIRECT TEST
# ============================================================

if __name__ == "__main__":

    records = generate()

    print("=" * 60)
    print("COMPUTER SCIENCE GENERATOR")
    print("=" * 60)
    print(f"Concepts : {len(CONCEPTS)}")
    print(f"Records  : {len(records)}")
    print("=" * 60)