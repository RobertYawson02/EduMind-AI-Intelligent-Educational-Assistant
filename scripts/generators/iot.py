"""
==============================================================
INTERNET OF THINGS GENERATOR
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY="Internet of Things"

CONCEPTS=[

("Internet of Things",["IoT"]),
("IoT Device",["smart device"]),
("Sensor",["electronic sensor"]),
("Actuator",["electronic actuator"]),
("Embedded System",["embedded systems"]),
("Microcontroller",["MCU"]),
("Arduino",["Arduino board"]),
("Raspberry Pi",["Raspberry Pi board"]),

("MQTT",["MQTT protocol"]),
("CoAP",["Constrained Application Protocol"]),
("ZigBee",["Zigbee"]),
("Bluetooth",["Bluetooth communication"]),
("WiFi",["wireless networking"]),
("6LoWPAN",["IPv6 over Low Power Wireless Personal Area Networks"]),

("Wireless Sensor Network",["WSN"]),
("Smart Home",["home automation"]),
("Smart Agriculture",["precision agriculture"]),
("Smart City",["intelligent city"]),
("Industrial IoT",["IIoT"]),

("IoT Gateway",["gateway"]),
("IoT Cloud",["cloud IoT"]),
("IoT Security",["IoT protection"]),
("IoT Communication",["device communication"]),
("IoT Data Analytics",["IoT analytics"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records