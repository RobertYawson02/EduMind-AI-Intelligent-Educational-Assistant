"""
==============================================================
CYBERSECURITY KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Curated cybersecurity concepts for the Intelligent
    Educational Assistant.

Architecture:
    Uses common.py to generate structured educational
    knowledge families.

Safety:
    Content is educational and defensive. It does not provide
    instructions for unauthorized access, exploitation, malware
    deployment, credential theft, or evasion.
"""

from __future__ import annotations

from .common import build_knowledge_family


CATEGORY = "Cybersecurity"


CONCEPTS = [

    # ========================================================
    # CYBERSECURITY FOUNDATIONS
    # ========================================================

    ("Cybersecurity", ["cyber security", "information security"]),
    ("Information Security", ["InfoSec"]),
    ("Computer Security", ["computer protection"]),
    ("Network Security", ["network protection"]),
    ("Application Security", ["application protection"]),
    ("Data Security", ["data protection"]),
    ("Digital Security", ["digital protection"]),
    ("Cyber Risk", ["cybersecurity risk"]),
    ("Cyber Threat", ["security threat"]),
    ("Cyber Attack", ["cyberattack"]),
    ("Cyber Crime", ["cybercrime"]),
    ("Cyber Defense", ["cyber defence"]),
    ("Security Awareness", ["security awareness training"]),
    ("Cyber Hygiene", ["digital hygiene"]),
    ("Security Best Practice", ["security practices"]),

    # ========================================================
    # CIA TRIAD AND SECURITY PRINCIPLES
    # ========================================================

    ("Confidentiality", ["information confidentiality"]),
    ("Integrity", ["data integrity"]),
    ("Availability", ["system availability"]),
    ("CIA Triad", ["confidentiality integrity availability"]),
    ("Non Repudiation", ["nonrepudiation"]),
    ("Accountability", ["security accountability"]),
    ("Authenticity", ["data authenticity"]),
    ("Least Privilege", ["principle of least privilege"]),
    ("Defense in Depth", ["layered security"]),
    ("Security by Design", ["secure by design"]),
    ("Privacy by Design", ["privacy protection by design"]),
    ("Zero Trust", ["zero trust security"]),
    ("Security Policy", ["information security policy"]),
    ("Security Control", ["security controls"]),
    ("Security Governance", ["cybersecurity governance"]),

    # ========================================================
    # THREATS AND VULNERABILITIES
    # ========================================================

    ("Security Threat", ["information security threat"]),
    ("Security Vulnerability", ["cyber vulnerability"]),
    ("Security Risk", ["information security risk"]),
    ("Attack Surface", ["cyber attack surface"]),
    ("Threat Actor", ["attacker"]),
    ("Insider Threat", ["internal threat"]),
    ("External Threat", ["external attacker"]),
    ("Advanced Persistent Threat", ["APT"]),
    ("Zero Day Vulnerability", ["zero-day vulnerability"]),
    ("Security Weakness", ["system weakness"]),
    ("Exploit", ["security exploit"]),
    ("Security Exposure", ["exposure"]),
    ("Risk Assessment", ["cyber risk assessment"]),
    ("Risk Management", ["cyber risk management"]),
    ("Threat Modeling", ["security threat modeling"]),

    # ========================================================
    # MALWARE
    # ========================================================

    ("Malware", ["malicious software"]),
    ("Computer Virus", ["virus"]),
    ("Computer Worm", ["worm"]),
    ("Trojan Horse", ["trojan"]),
    ("Ransomware", ["ransomware attack"]),
    ("Spyware", ["spy software"]),
    ("Adware", ["advertising malware"]),
    ("Rootkit", ["rootkit malware"]),
    ("Keylogger", ["keystroke logger"]),
    ("Botnet", ["bot network"]),
    ("Backdoor", ["malicious backdoor"]),
    ("Fileless Malware", ["memory-based malware"]),
    ("Malware Detection", ["malware identification"]),
    ("Malware Prevention", ["malware protection"]),
    ("Malware Analysis", ["malicious software analysis"]),

    # ========================================================
    # SOCIAL ENGINEERING
    # ========================================================

    ("Social Engineering", ["social engineering attack"]),
    ("Phishing", ["phishing attack"]),
    ("Spear Phishing", ["targeted phishing"]),
    ("Whaling", ["executive phishing"]),
    ("Smishing", ["SMS phishing"]),
    ("Vishing", ["voice phishing"]),
    ("Pharming", ["pharming attack"]),
    ("Pretexting", ["pretext attack"]),
    ("Baiting", ["baiting attack"]),
    ("Tailgating", ["physical social engineering"]),
    ("Impersonation", ["identity impersonation"]),
    ("Security Awareness Against Phishing", ["phishing awareness"]),

    # ========================================================
    # PASSWORD AND ACCOUNT SECURITY
    # ========================================================

    ("Password Security", ["secure passwords"]),
    ("Strong Password", ["password strength"]),
    ("Password Policy", ["password requirements"]),
    ("Password Manager", ["password management"]),
    ("Password Hashing", ["hashed passwords"]),
    ("Password Salting", ["password salt"]),
    ("Brute Force Attack", ["brute-force attack"]),
    ("Credential Stuffing", ["credential reuse attack"]),
    ("Password Spraying", ["password spray"]),
    ("Account Lockout", ["login lockout"]),
    ("Credential Security", ["credential protection"]),
    ("Account Security", ["user account security"]),

    # ========================================================
    # AUTHENTICATION AND AUTHORIZATION
    # ========================================================

    ("Authentication", ["user authentication"]),
    ("Authorization", ["access authorization"]),
    ("Identity Management", ["identity management"]),
    ("Identity and Access Management", ["IAM"]),
    ("Multi Factor Authentication", ["MFA"]),
    ("Two Factor Authentication", ["2FA"]),
    ("Single Sign On", ["SSO"]),
    ("Biometric Authentication", ["biometric security"]),
    ("Token Authentication", ["authentication token"]),
    ("Session Authentication", ["session security"]),
    ("Role Based Access Control", ["RBAC"]),
    ("Attribute Based Access Control", ["ABAC"]),
    ("Access Control List", ["ACL"]),
    ("Privileged Access Management", ["PAM"]),
    ("User Access Review", ["access review"]),

    # ========================================================
    # CRYPTOGRAPHY
    # ========================================================

    ("Cryptography", ["cryptographic security"]),
    ("Encryption", ["data encryption"]),
    ("Decryption", ["data decryption"]),
    ("Plaintext", ["cleartext"]),
    ("Ciphertext", ["encrypted data"]),
    ("Cryptographic Key", ["encryption key"]),
    ("Key Management", ["cryptographic key management"]),
    ("Symmetric Encryption", ["symmetric cryptography"]),
    ("Asymmetric Encryption", ["public key cryptography"]),
    ("Public Key", ["public encryption key"]),
    ("Private Key", ["private encryption key"]),
    ("Digital Signature", ["electronic signature"]),
    ("Digital Certificate", ["security certificate"]),
    ("Certificate Authority", ["CA"]),
    ("Public Key Infrastructure", ["PKI"]),
    ("Hash Function", ["cryptographic hash"]),
    ("Message Digest", ["hash digest"]),
    ("SHA 256", ["SHA-256"]),
    ("SHA 3", ["SHA-3"]),
    ("AES", ["Advanced Encryption Standard"]),
    ("RSA", ["RSA cryptography"]),
    ("Transport Layer Security", ["TLS"]),
    ("Secure Sockets Layer", ["SSL"]),
    ("End to End Encryption", ["E2EE"]),

    # ========================================================
    # NETWORK SECURITY
    # ========================================================

    ("Network Security Architecture", ["secure network architecture"]),
    ("Firewall", ["network firewall"]),
    ("Hardware Firewall", ["network firewall appliance"]),
    ("Software Firewall", ["host firewall"]),
    ("Stateful Firewall", ["stateful inspection"]),
    ("Stateless Firewall", ["packet filtering firewall"]),
    ("Web Application Firewall", ["WAF"]),
    ("Intrusion Detection System", ["IDS"]),
    ("Intrusion Prevention System", ["IPS"]),
    ("Security Information and Event Management", ["SIEM"]),
    ("Network Monitoring", ["security monitoring"]),
    ("Network Segmentation", ["security segmentation"]),
    ("Network Access Control", ["NAC"]),
    ("Virtual Private Network", ["VPN"]),
    ("Secure Remote Access", ["remote access security"]),
    ("Demilitarized Zone", ["DMZ"]),
    ("Proxy Server Security", ["proxy security"]),
    ("DNS Security", ["domain security"]),
    ("Email Security", ["secure email"]),

    # ========================================================
    # COMMON ATTACK TYPES
    # ========================================================

    ("Denial of Service", ["DoS"]),
    ("Distributed Denial of Service", ["DDoS"]),
    ("Man in the Middle Attack", ["MITM"]),
    ("Man in the Browser Attack", ["MITB"]),
    ("Replay Attack", ["replay security attack"]),
    ("Session Hijacking", ["session attack"]),
    ("Spoofing", ["identity spoofing"]),
    ("IP Spoofing", ["IP address spoofing"]),
    ("Email Spoofing", ["email address spoofing"]),
    ("DNS Spoofing", ["DNS poisoning"]),
    ("ARP Spoofing", ["ARP poisoning"]),
    ("Evil Twin Attack", ["rogue WiFi access point"]),
    ("Drive By Download", ["drive-by download"]),
    ("Malicious Attachment", ["email attachment threat"]),

    # ========================================================
    # WEB SECURITY
    # ========================================================

    ("Web Application Security", ["web security"]),
    ("SQL Injection", ["SQLi"]),
    ("Cross Site Scripting", ["XSS"]),
    ("Cross Site Request Forgery", ["CSRF"]),
    ("Broken Authentication", ["authentication vulnerability"]),
    ("Broken Access Control", ["authorization vulnerability"]),
    ("Security Misconfiguration", ["misconfiguration"]),
    ("Insecure Direct Object Reference", ["IDOR"]),
    ("Input Validation", ["input sanitization"]),
    ("Output Encoding", ["output escaping"]),
    ("Secure Cookie", ["cookie security"]),
    ("HTTP Security Headers", ["web security headers"]),
    ("Content Security Policy", ["CSP"]),
    ("HTTP Strict Transport Security", ["HSTS"]),
    ("Secure Web Session", ["web session security"]),
    ("API Security", ["application programming interface security"]),
    ("API Authentication", ["API access security"]),
    ("API Authorization", ["API permissions"]),

    # ========================================================
    # SECURE SOFTWARE DEVELOPMENT
    # ========================================================

    ("Secure Software Development", ["secure coding"]),
    ("Secure Coding", ["secure programming"]),
    ("Software Security", ["application security"]),
    ("Security Requirements", ["secure requirements"]),
    ("Security Testing", ["application security testing"]),
    ("Static Application Security Testing", ["SAST"]),
    ("Dynamic Application Security Testing", ["DAST"]),
    ("Software Composition Analysis", ["SCA"]),
    ("Dependency Security", ["software dependency security"]),
    ("Code Review Security", ["secure code review"]),
    ("DevSecOps", ["security development operations"]),
    ("Security Testing Lifecycle", ["secure testing lifecycle"]),
    ("Vulnerability Scanning", ["security vulnerability scanning"]),
    ("Patch Management", ["security patching"]),
    ("Security Update", ["software security update"]),

    # ========================================================
    # DATA SECURITY
    # ========================================================

    ("Data Protection", ["data security"]),
    ("Data Privacy", ["privacy"]),
    ("Sensitive Data", ["sensitive information"]),
    ("Personal Data", ["personal information"]),
    ("Personally Identifiable Information", ["PII"]),
    ("Financial Data Security", ["financial information security"]),
    ("Data Loss Prevention", ["DLP"]),
    ("Data Classification", ["information classification"]),
    ("Data Retention", ["data retention policy"]),
    ("Secure Data Storage", ["data storage security"]),
    ("Database Security", ["database protection"]),
    ("Data Masking", ["data masking"]),
    ("Data Anonymization", ["anonymization"]),
    ("Data Backup Security", ["secure backup"]),

    # ========================================================
    # INCIDENT RESPONSE
    # ========================================================

    ("Incident Response", ["cyber incident response"]),
    ("Security Incident", ["information security incident"]),
    ("Incident Detection", ["security incident detection"]),
    ("Incident Analysis", ["incident analysis"]),
    ("Incident Containment", ["security containment"]),
    ("Incident Eradication", ["threat eradication"]),
    ("Incident Recovery", ["security recovery"]),
    ("Incident Reporting", ["cyber incident reporting"]),
    ("Incident Response Plan", ["IR plan"]),
    ("Computer Security Incident Response Team", ["CSIRT"]),
    ("Digital Forensics", ["computer forensics"]),
    ("Forensic Investigation", ["cyber forensic investigation"]),
    ("Evidence Preservation", ["digital evidence preservation"]),
    ("Security Incident Documentation", ["incident documentation"]),

    # ========================================================
    # BUSINESS CONTINUITY
    # ========================================================

    ("Business Continuity", ["business continuity planning"]),
    ("Disaster Recovery", ["IT disaster recovery"]),
    ("Disaster Recovery Plan", ["DR plan"]),
    ("Business Continuity Plan", ["BCP"]),
    ("Backup", ["data backup"]),
    ("Backup Strategy", ["backup planning"]),
    ("Recovery Point Objective", ["RPO"]),
    ("Recovery Time Objective", ["RTO"]),
    ("Business Impact Analysis", ["BIA"]),
    ("System Recovery", ["IT recovery"]),

    # ========================================================
    # SECURITY MONITORING
    # ========================================================

    ("Security Monitoring", ["cyber monitoring"]),
    ("Security Log", ["security logs"]),
    ("Event Log", ["system event log"]),
    ("Log Management", ["security log management"]),
    ("Security Alert", ["security alerts"]),
    ("Security Information and Event Management", ["SIEM"]),
    ("Security Operations Center", ["SOC"]),
    ("Security Analyst", ["cybersecurity analyst"]),
    ("Threat Intelligence", ["cyber threat intelligence"]),
    ("Security Dashboard", ["security monitoring dashboard"]),

    # ========================================================
    # GOVERNANCE, RISK AND COMPLIANCE
    # ========================================================

    ("Governance Risk and Compliance", ["GRC"]),
    ("Security Compliance", ["cyber compliance"]),
    ("Security Audit", ["cybersecurity audit"]),
    ("Security Assessment", ["security evaluation"]),
    ("Compliance Assessment", ["compliance review"]),
    ("Security Standard", ["information security standard"]),
    ("Security Framework", ["cybersecurity framework"]),
    ("NIST Cybersecurity Framework", ["NIST CSF"]),
    ("ISO 27001", ["ISO/IEC 27001"]),
    ("Security Policy Framework", ["security governance framework"]),
    ("Security Awareness Policy", ["security awareness policy"]),
    ("Acceptable Use Policy", ["AUP"]),
    ("Password Policy Security", ["password policy"]),

    # ========================================================
    # CLOUD SECURITY
    # ========================================================

    ("Cloud Security", ["cloud cybersecurity"]),
    ("Cloud Access Security", ["cloud access control"]),
    ("Cloud Identity Management", ["cloud IAM"]),
    ("Cloud Data Protection", ["cloud data security"]),
    ("Cloud Security Monitoring", ["cloud monitoring"]),
    ("Cloud Misconfiguration", ["cloud security configuration"]),
    ("Cloud Network Security", ["cloud network protection"]),
    ("Container Security", ["container cybersecurity"]),
    ("Virtual Machine Security", ["VM security"]),
    ("Serverless Security", ["serverless application security"]),

    # ========================================================
    # MOBILE AND ENDPOINT SECURITY
    # ========================================================

    ("Endpoint Security", ["endpoint protection"]),
    ("Endpoint Detection and Response", ["EDR"]),
    ("Extended Detection and Response", ["XDR"]),
    ("Mobile Security", ["mobile device security"]),
    ("Mobile Device Management", ["MDM"]),
    ("Application Control", ["application whitelisting"]),
    ("Device Encryption", ["endpoint encryption"]),
    ("Secure Boot", ["trusted boot"]),
    ("Operating System Security", ["OS security"]),
    ("Antivirus", ["anti-malware"]),
    ("Endpoint Protection Platform", ["EPP"]),

    # ========================================================
    # IoT SECURITY
    # ========================================================

    ("IoT Security", ["Internet of Things security"]),
    ("IoT Device Security", ["smart device security"]),
    ("IoT Authentication", ["IoT identity"]),
    ("IoT Encryption", ["IoT data encryption"]),
    ("IoT Network Security", ["IoT network protection"]),
    ("IoT Firmware Security", ["firmware security"]),
    ("IoT Access Control", ["IoT authorization"]),
    ("IoT Privacy", ["Internet of Things privacy"]),

    # ========================================================
    # SECURITY ETHICS
    # ========================================================

    ("Cybersecurity Ethics", ["cyber ethics"]),
    ("Digital Ethics", ["technology ethics"]),
    ("Responsible Disclosure", ["vulnerability disclosure"]),
    ("Security Research Ethics", ["ethical security research"]),
    ("Privacy Ethics", ["data privacy ethics"]),
    ("Responsible Technology Use", ["ethical technology use"]),
    ("Professional Cybersecurity Ethics", ["cybersecurity professional ethics"]),

    # ========================================================
    # SECURITY CAREERS
    # ========================================================

    ("Cybersecurity Analyst", ["security analyst"]),
    ("Security Engineer", ["cybersecurity engineer"]),
    ("Network Security Engineer", ["network security specialist"]),
    ("Security Architect", ["cybersecurity architect"]),
    ("Penetration Tester", ["ethical hacker"]),
    ("Security Consultant", ["cybersecurity consultant"]),
    ("Digital Forensics Analyst", ["forensics analyst"]),
    ("Incident Response Analyst", ["incident responder"]),
    ("Security Operations Analyst", ["SOC analyst"]),
    ("Security Auditor", ["cyber auditor"]),
]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """Generate the Cybersecurity knowledge family."""

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
    print("CYBERSECURITY GENERATOR")
    print("=" * 60)
    print(f"Concepts : {len(CONCEPTS)}")
    print(f"Records  : {len(records)}")
    print("=" * 60)