"""
==============================================================
CLOUD COMPUTING GENERATOR
==============================================================
"""

from __future__ import annotations
from .common import build_knowledge_family

CATEGORY = "Cloud Computing"

CONCEPTS = [

    ("Cloud Computing", ["cloud"]),
    ("Infrastructure as a Service", ["IaaS"]),
    ("Platform as a Service", ["PaaS"]),
    ("Software as a Service", ["SaaS"]),
    ("Public Cloud", ["public cloud"]),
    ("Private Cloud", ["private cloud"]),
    ("Hybrid Cloud", ["hybrid cloud"]),
    ("Community Cloud", ["community cloud"]),

    ("Virtual Machine", ["VM"]),
    ("Virtualization", ["virtualisation"]),
    ("Container", ["software container"]),
    ("Docker", ["Docker container"]),
    ("Kubernetes", ["K8s"]),
    ("Serverless Computing", ["serverless"]),

    ("Cloud Storage", ["online storage"]),
    ("Cloud Database", ["cloud database"]),
    ("Load Balancer", ["load balancing"]),
    ("Auto Scaling", ["autoscaling"]),
    ("Cloud Security", ["cloud protection"]),

    ("Amazon Web Services", ["AWS"]),
    ("Microsoft Azure", ["Azure"]),
    ("Google Cloud Platform", ["GCP"]),
    ("Cloud Deployment", ["deployment"]),
    ("Edge Computing", ["edge cloud"]),
    ("Cloud Backup", ["cloud backup"]),
    ("Cloud Disaster Recovery", ["cloud recovery"])
]

def generate():
    records=[]
    for topic, aliases in CONCEPTS:
        records.extend(build_knowledge_family(topic,CATEGORY,aliases))
    return records