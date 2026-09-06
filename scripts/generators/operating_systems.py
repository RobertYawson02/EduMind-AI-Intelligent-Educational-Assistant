"""
==============================================================
OPERATING SYSTEMS GENERATOR
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY="Operating Systems"

CONCEPTS=[

("Operating System",["OS"]),
("Windows",["Microsoft Windows"]),
("Linux",["Linux OS"]),
("Ubuntu",["Ubuntu Linux"]),
("macOS",["Apple macOS"]),

("Kernel",["OS kernel"]),
("Process",["computer process"]),
("Thread",["execution thread"]),
("Process Scheduling",["CPU scheduling"]),
("Memory Management",["memory allocation"]),
("Virtual Memory",["virtual memory"]),
("Paging",["memory paging"]),
("Segmentation",["memory segmentation"]),
("File System",["filesystem"]),
("Device Management",["device control"]),

("Boot Process",["system boot"]),
("Boot Loader",["bootloader"]),
("Command Line Interface",["CLI"]),
("Graphical User Interface",["GUI"]),
("System Call",["system calls"]),
("Multitasking",["task switching"]),
("Multiprocessing",["multiple processors"]),
("Deadlock",["deadlock"]),
("Semaphore",["process synchronization"]),
("Mutex",["mutual exclusion"]),
("Shell",["command shell"]),
("Bash",["Bash shell"]),
("PowerShell",["Microsoft PowerShell"]),
("Permission",["file permissions"]),
("User Account",["system user"]),
("Administrator",["admin account"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records