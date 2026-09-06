"""
==============================================================
COMPUTING KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Generate structured educational knowledge covering
    general computing concepts, computer architecture,
    computational thinking, digital systems, and modern
    computing technologies.

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

CATEGORY = "Computing"


# ============================================================
# COMPUTING TOPICS
# ============================================================

TOPICS = [

    # --------------------------------------------------------
    # Foundations of Computing
    # --------------------------------------------------------

    ("Computing", ["computer science", "computational studies"]),
    ("Computer", ["computing device", "digital computer"]),
    ("Information", ["digital information", "data"]),
    ("Data", ["digital data", "information"]),
    ("Information Processing", ["data processing"]),
    ("Information Technology", ["IT", "information technology"]),
    ("Computer Technology", ["computing technology"]),
    ("Digital Technology", ["digital systems", "digital technologies"]),
    ("Digital Transformation", ["digitalization", "digital change"]),
    ("Automation", ["computer automation", "automated systems"]),
    ("Computational Thinking", ["computational problem solving"]),
    ("Algorithmic Thinking", ["algorithmic reasoning"]),
    ("Problem Decomposition", ["decomposition", "problem breakdown"]),
    ("Pattern Recognition", ["pattern identification"]),
    ("Abstraction", ["computational abstraction"]),
    ("Logical Reasoning", ["logical thinking", "reasoning"]),
    ("Decision Making", ["computational decision making"]),

    # --------------------------------------------------------
    # Computer Architecture
    # --------------------------------------------------------

    ("Computer Architecture", ["computer organization"]),
    ("Computer Organization", ["computer structure"]),
    ("Central Processing Unit", ["CPU", "processor"]),
    ("Arithmetic Logic Unit", ["ALU"]),
    ("Control Unit", ["CU", "processor control unit"]),
    ("Registers", ["CPU registers", "processor registers"]),
    ("Cache Memory", ["CPU cache", "processor cache"]),
    ("Main Memory", ["primary memory", "RAM"]),
    ("Random Access Memory", ["RAM", "volatile memory"]),
    ("Read Only Memory", ["ROM", "non-volatile memory"]),
    ("Secondary Storage", ["secondary memory", "storage"]),
    ("Motherboard", ["mainboard", "system board"]),
    ("Bus", ["computer bus", "system bus"]),
    ("Data Bus", ["data transfer bus"]),
    ("Address Bus", ["memory address bus"]),
    ("Control Bus", ["control signal bus"]),
    ("Input Device", ["computer input device"]),
    ("Output Device", ["computer output device"]),
    ("Input and Output System", ["I/O system", "input output"]),
    ("Computer Peripheral", ["peripheral device"]),
    ("Expansion Card", ["adapter card", "expansion board"]),
    ("Power Supply Unit", ["PSU", "computer power supply"]),

    # --------------------------------------------------------
    # Processing
    # --------------------------------------------------------

    ("Processor", ["CPU", "microprocessor"]),
    ("Microprocessor", ["processor chip"]),
    ("Microcontroller", ["MCU", "embedded controller"]),
    ("Multicore Processor", ["multicore CPU"]),
    ("Parallel Processing", ["parallel computation"]),
    ("Sequential Processing", ["sequential computation"]),
    ("Concurrent Processing", ["concurrent computation"]),
    ("Distributed Processing", ["distributed computation"]),
    ("Pipelining", ["instruction pipeline"]),
    ("Instruction Cycle", ["fetch decode execute cycle"]),
    ("Machine Instruction", ["CPU instruction"]),
    ("Instruction Set", ["instruction set architecture"]),
    ("Instruction Set Architecture", ["ISA"]),
    ("Clock Speed", ["CPU clock frequency"]),
    ("Processing Speed", ["computer processing performance"]),

    # --------------------------------------------------------
    # Memory and Storage
    # --------------------------------------------------------

    ("Memory Hierarchy", ["computer memory hierarchy"]),
    ("Volatile Memory", ["temporary memory"]),
    ("Nonvolatile Memory", ["persistent memory"]),
    ("Dynamic RAM", ["DRAM"]),
    ("Static RAM", ["SRAM"]),
    ("Flash Memory", ["flash storage"]),
    ("Solid State Drive", ["SSD"]),
    ("Hard Disk Drive", ["HDD"]),
    ("Optical Storage", ["optical disk"]),
    ("Magnetic Storage", ["magnetic disk"]),
    ("Cloud Storage", ["online storage", "remote storage"]),
    ("Memory Addressing", ["memory addresses"]),
    ("Virtual Memory", ["virtual memory management"]),
    ("Memory Management", ["RAM management"]),

    # --------------------------------------------------------
    # Operating Environment
    # --------------------------------------------------------

    ("Computing Environment", ["computer environment"]),
    ("Desktop Computing", ["desktop environment"]),
    ("Mobile Computing", ["mobile technology"]),
    ("Personal Computing", ["personal computer technology"]),
    ("Server Computing", ["server-based computing"]),
    ("High Performance Computing", ["HPC"]),
    ("Scientific Computing", ["scientific computation"]),
    ("Enterprise Computing", ["enterprise technology"]),
    ("Edge Computing", ["edge technology"]),
    ("Fog Computing", ["fog architecture"]),

    # --------------------------------------------------------
    # Computational Models
    # --------------------------------------------------------

    ("Computational Model", ["model of computation"]),
    ("Computational Complexity", ["complexity of computation"]),
    ("Computability", ["computability theory"]),
    ("Finite State Machine", ["FSM"]),
    ("Automata Theory", ["theory of computation"]),
    ("Turing Machine", ["Turing computation"]),
    ("Formal Language", ["formal languages"]),
    ("Grammar", ["formal grammar", "computational grammar"]),
    ("Boolean Logic", ["Boolean algebra", "logical algebra"]),
    ("Binary Logic", ["binary computation"]),

    # --------------------------------------------------------
    # Number Systems
    # --------------------------------------------------------

    ("Number System", ["numeral system"]),
    ("Binary Number System", ["binary system", "base 2"]),
    ("Decimal Number System", ["decimal system", "base 10"]),
    ("Octal Number System", ["octal system", "base 8"]),
    ("Hexadecimal Number System", ["hexadecimal", "base 16"]),
    ("Binary Conversion", ["number system conversion"]),
    ("Binary Arithmetic", ["binary calculations"]),
    ("Bit", ["binary digit"]),
    ("Byte", ["8-bit unit"]),
    ("Kilobyte", ["KB", "computer storage unit"]),
    ("Megabyte", ["MB", "computer storage unit"]),
    ("Gigabyte", ["GB", "computer storage unit"]),
    ("Terabyte", ["TB", "computer storage unit"]),

    # --------------------------------------------------------
    # Digital Representation
    # --------------------------------------------------------

    ("Data Representation", ["digital representation"]),
    ("Character Encoding", ["text encoding"]),
    ("ASCII", ["American Standard Code for Information Interchange"]),
    ("Unicode", ["Unicode encoding"]),
    ("UTF-8", ["Unicode Transformation Format"]),
    ("Digital Image Representation", ["image data representation"]),
    ("Digital Audio Representation", ["audio data representation"]),
    ("Digital Video Representation", ["video data representation"]),
    ("Data Compression", ["compression"]),
    ("Lossless Compression", ["lossless data compression"]),
    ("Lossy Compression", ["lossy data compression"]),

    # --------------------------------------------------------
    # Computational Problem Solving
    # --------------------------------------------------------

    ("Problem Solving", ["computational problem solving"]),
    ("Algorithm", ["computational procedure"]),
    ("Algorithm Design", ["algorithm development"]),
    ("Pseudocode", ["algorithm pseudocode"]),
    ("Flowchart", ["process flowchart", "algorithm flowchart"]),
    ("Decision Structure", ["conditional structure"]),
    ("Iteration", ["looping", "repetition"]),
    ("Recursion", ["recursive computation"]),
    ("Search Algorithm", ["searching algorithm"]),
    ("Sorting Algorithm", ["sorting method"]),
    ("Optimization", ["computational optimization"]),
    ("Heuristic", ["heuristic method"]),
    ("Brute Force", ["brute-force method"]),
    ("Divide and Conquer", ["divide-and-conquer algorithm"]),
    ("Dynamic Programming", ["dynamic programming method"]),

    # --------------------------------------------------------
    # Software Concepts
    # --------------------------------------------------------

    ("Software", ["computer software"]),
    ("System Software", ["system-level software"]),
    ("Application Software", ["application program"]),
    ("Utility Software", ["system utility"]),
    ("Firmware", ["embedded software"]),
    ("Driver", ["device driver"]),
    ("Middleware", ["software middleware"]),
    ("Open Source Software", ["open-source software"]),
    ("Proprietary Software", ["closed-source software"]),
    ("Free Software", ["software freedom"]),
    ("Software License", ["software licensing"]),
    ("Software Update", ["software upgrade"]),
    ("Software Patch", ["program patch"]),
    ("Software Installation", ["program installation"]),
    ("Software Configuration", ["software setup"]),

    # --------------------------------------------------------
    # Human Computer Interaction
    # --------------------------------------------------------

    ("Human Computer Interaction", ["HCI"]),
    ("User Interface", ["UI"]),
    ("Graphical User Interface", ["GUI"]),
    ("Command Line Interface", ["CLI"]),
    ("User Experience", ["UX"]),
    ("Usability", ["system usability"]),
    ("Accessibility", ["digital accessibility"]),
    ("Interaction Design", ["interface interaction design"]),
    ("User-Centered Design", ["user-centered computing"]),
    ("Human Factors", ["human-computer factors"]),
    ("Ergonomics", ["computer ergonomics"]),

    # --------------------------------------------------------
    # Internet and Digital Society
    # --------------------------------------------------------

    ("Internet", ["global computer network"]),
    ("World Wide Web", ["WWW", "web"]),
    ("Digital Society", ["digital community"]),
    ("Digital Citizenship", ["responsible digital participation"]),
    ("Digital Identity", ["online identity"]),
    ("Digital Footprint", ["online footprint"]),
    ("Digital Communication", ["electronic communication"]),
    ("Social Computing", ["social technology"]),
    ("Ubiquitous Computing", ["pervasive computing"]),
    ("Ambient Computing", ["context-aware computing"]),

    # --------------------------------------------------------
    # Emerging Computing
    # --------------------------------------------------------

    ("Quantum Computing", ["quantum computer"]),
    ("Quantum Information", ["quantum information science"]),
    ("Neuromorphic Computing", ["brain-inspired computing"]),
    ("Biocomputing", ["biological computing"]),
    ("DNA Computing", ["DNA-based computation"]),
    ("Optical Computing", ["photonic computing"]),
    ("Green Computing", ["sustainable computing"]),
    ("Cloud Computing", ["cloud technology"]),
    ("Edge Computing Architecture", ["edge architecture"]),
    ("Internet Computing", ["network-based computing"]),
    ("Autonomous Computing", ["self-managing computing"]),
    ("Cognitive Computing", ["cognitive systems"]),

    # --------------------------------------------------------
    # Computing Ethics and Society
    # --------------------------------------------------------

    ("Computer Ethics", ["computing ethics"]),
    ("Technology Ethics", ["technology ethics"]),
    ("Digital Privacy", ["online privacy"]),
    ("Data Privacy", ["information privacy"]),
    ("Digital Rights", ["technology rights"]),
    ("Technology and Society", ["computing and society"]),
    ("Digital Divide", ["technology access gap"]),
    ("Technology Accessibility", ["accessible technology"]),
    ("Responsible Computing", ["responsible technology"]),
    ("Sustainable Technology", ["sustainable computing technology"]),

    # --------------------------------------------------------
    # Professional Computing
    # --------------------------------------------------------

    ("Computing Profession", ["computing career"]),
    ("Computer Professional", ["IT professional", "computing professional"]),
    ("Technical Skills", ["technology skills"]),
    ("Digital Skills", ["digital competencies"]),
    ("Computing Competency", ["computing competence"]),
    ("Professional Certification", ["technical certification"]),
    ("Technology Career", ["computing career"]),
    ("Computing Research", ["computer research"]),
    ("Technology Innovation", ["computing innovation"]),
    ("Technology Entrepreneurship", ["technology business"]),

]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """
    Generate the complete Computing knowledge base.
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