"""
==============================================================
NETWORKING KNOWLEDGE GENERATOR
Version 3.0
==============================================================

Purpose:
    Curated Computer Networking concepts for the Intelligent
    Educational Assistant.

Architecture:
    Uses common.py to generate structured educational
    knowledge families while preserving the existing JSON
    record format.
"""

from __future__ import annotations

from .common import build_knowledge_family


CATEGORY = "Networking"


# ============================================================
# CURATED NETWORKING CONCEPTS
# ============================================================

CONCEPTS = [

    # --------------------------------------------------------
    # NETWORKING FOUNDATIONS
    # --------------------------------------------------------

    ("Computer Networking", ["computer networks", "networking"]),
    ("Computer Network", ["network"]),
    ("Network Communication", ["data communication"]),
    ("Data Communication", ["digital communication"]),
    ("Network Protocol", ["network protocols"]),
    ("Network Architecture", ["network architecture"]),
    ("Network Infrastructure", ["network infrastructure"]),
    ("Network Resource", ["network resources"]),
    ("Network Node", ["network node"]),
    ("Network Host", ["network host"]),
    ("Client", ["network client"]),
    ("Server", ["network server"]),
    ("Peer to Peer Network", ["P2P", "peer-to-peer"]),
    ("Client Server Network", ["client-server"]),
    ("Distributed Network", ["distributed networking"]),

    # --------------------------------------------------------
    # NETWORK TYPES
    # --------------------------------------------------------

    ("Local Area Network", ["LAN"]),
    ("Wide Area Network", ["WAN"]),
    ("Metropolitan Area Network", ["MAN"]),
    ("Personal Area Network", ["PAN"]),
    ("Wireless Local Area Network", ["WLAN"]),
    ("Campus Area Network", ["CAN"]),
    ("Storage Area Network", ["SAN"]),
    ("Virtual Private Network", ["VPN"]),
    ("Intranet", ["private organizational network"]),
    ("Extranet", ["business network"]),
    ("Internet", ["global computer network"]),
    ("Public Network", ["public networking"]),
    ("Private Network", ["private networking"]),

    # --------------------------------------------------------
    # NETWORK TOPOLOGIES
    # --------------------------------------------------------

    ("Network Topology", ["network layouts"]),
    ("Bus Topology", ["bus network"]),
    ("Star Topology", ["star network"]),
    ("Ring Topology", ["ring network"]),
    ("Mesh Topology", ["mesh network"]),
    ("Full Mesh Topology", ["full mesh"]),
    ("Partial Mesh Topology", ["partial mesh"]),
    ("Tree Topology", ["hierarchical topology"]),
    ("Hybrid Topology", ["hybrid network topology"]),

    # --------------------------------------------------------
    # NETWORK DEVICES
    # --------------------------------------------------------

    ("Router", ["network router"]),
    ("Switch", ["network switch"]),
    ("Hub", ["network hub"]),
    ("Bridge", ["network bridge"]),
    ("Gateway", ["network gateway"]),
    ("Repeater", ["network repeater"]),
    ("Modem", ["network modem"]),
    ("Wireless Access Point", ["AP", "access point"]),
    ("Network Interface Card", ["NIC"]),
    ("Network Firewall", ["network firewall"]),
    ("Proxy Server", ["proxy"]),
    ("Load Balancer", ["network load balancer"]),
    ("Network Controller", ["network controller"]),
    ("Wireless Router", ["WiFi router"]),

    # --------------------------------------------------------
    # NETWORK MEDIA
    # --------------------------------------------------------

    ("Transmission Medium", ["network transmission media"]),
    ("Guided Transmission Media", ["wired media"]),
    ("Unguided Transmission Media", ["wireless media"]),
    ("Twisted Pair Cable", ["twisted pair"]),
    ("Unshielded Twisted Pair", ["UTP"]),
    ("Shielded Twisted Pair", ["STP"]),
    ("Coaxial Cable", ["coax cable"]),
    ("Fiber Optic Cable", ["optical fiber"]),
    ("Single Mode Fiber", ["single-mode fiber"]),
    ("Multimode Fiber", ["multimode fiber"]),
    ("Radio Wave", ["radio transmission"]),
    ("Microwave Transmission", ["microwave communication"]),
    ("Infrared Transmission", ["infrared communication"]),
    ("Satellite Communication", ["satellite networking"]),

    # --------------------------------------------------------
    # OSI MODEL
    # --------------------------------------------------------

    ("OSI Model", ["Open Systems Interconnection"]),
    ("Physical Layer", ["OSI layer 1"]),
    ("Data Link Layer", ["OSI layer 2"]),
    ("Network Layer", ["OSI layer 3"]),
    ("Transport Layer", ["OSI layer 4"]),
    ("Session Layer", ["OSI layer 5"]),
    ("Presentation Layer", ["OSI layer 6"]),
    ("Application Layer", ["OSI layer 7"]),
    ("Encapsulation", ["network encapsulation"]),
    ("Decapsulation", ["network decapsulation"]),
    ("Protocol Data Unit", ["PDU"]),
    ("Frame", ["data frame"]),
    ("Packet", ["network packet"]),
    ("Segment", ["TCP segment"]),
    ("Datagram", ["network datagram"]),

    # --------------------------------------------------------
    # TCP/IP MODEL
    # --------------------------------------------------------

    ("TCP IP Model", ["TCP/IP model"]),
    ("Network Access Layer", ["link layer"]),
    ("Internet Layer", ["internet layer"]),
    ("Transport Layer TCP IP", ["transport layer TCP"]),
    ("Application Layer TCP IP", ["TCP/IP application layer"]),
    ("TCP IP Protocol Suite", ["internet protocol suite"]),

    # --------------------------------------------------------
    # IP ADDRESSING
    # --------------------------------------------------------

    ("IP Address", ["Internet Protocol address"]),
    ("IPv4", ["IPv4 address"]),
    ("IPv6", ["IPv6 address"]),
    ("Public IP Address", ["public IP"]),
    ("Private IP Address", ["private IP"]),
    ("Static IP Address", ["static IP"]),
    ("Dynamic IP Address", ["dynamic IP"]),
    ("Loopback Address", ["localhost", "loopback"]),
    ("APIPA", ["automatic private IP addressing"]),
    ("Network Address", ["network portion"]),
    ("Broadcast Address", ["broadcast IP"]),
    ("Multicast Address", ["multicast IP"]),
    ("Unicast Address", ["unicast IP"]),
    ("Subnet Mask", ["subnet"]),
    ("CIDR", ["Classless Inter-Domain Routing"]),
    ("CIDR Notation", ["slash notation"]),
    ("Default Gateway", ["gateway address"]),
    ("Network Prefix", ["IP prefix"]),
    ("Host Portion", ["host part of IP address"]),

    # --------------------------------------------------------
    # SUBNETTING
    # --------------------------------------------------------

    ("Subnetting", ["IP subnetting"]),
    ("Subnet", ["network subnet"]),
    ("Supernetting", ["route aggregation"]),
    ("Variable Length Subnet Mask", ["VLSM"]),
    ("Classless Addressing", ["classless IP addressing"]),
    ("Classful Addressing", ["classful networking"]),
    ("Network Class A", ["Class A"]),
    ("Network Class B", ["Class B"]),
    ("Network Class C", ["Class C"]),
    ("Network Class D", ["Class D"]),
    ("Network Class E", ["Class E"]),
    ("Subnet Calculator", ["subnet calculation"]),
    ("Subnet Mask Calculation", ["subnetting calculation"]),

    # --------------------------------------------------------
    # MAC AND ETHERNET
    # --------------------------------------------------------

    ("MAC Address", ["Media Access Control address"]),
    ("Ethernet", ["Ethernet networking"]),
    ("Ethernet Frame", ["Ethernet frame"]),
    ("MAC Table", ["switch MAC table"]),
    ("ARP", ["Address Resolution Protocol"]),
    ("ARP Table", ["ARP cache"]),
    ("Gratuitous ARP", ["GARP"]),
    ("Ethernet Switch", ["Layer 2 switch"]),

    # --------------------------------------------------------
    # TRANSPORT PROTOCOLS
    # --------------------------------------------------------

    ("Transmission Control Protocol", ["TCP"]),
    ("User Datagram Protocol", ["UDP"]),
    ("TCP Connection", ["TCP session"]),
    ("TCP Three Way Handshake", ["three-way handshake"]),
    ("TCP Flow Control", ["TCP flow control"]),
    ("TCP Congestion Control", ["congestion control"]),
    ("TCP Reliability", ["reliable transport"]),
    ("UDP Communication", ["UDP networking"]),
    ("Port Number", ["network port"]),
    ("Socket", ["network socket"]),
    ("Socket Programming", ["network socket programming"]),

    # --------------------------------------------------------
    # APPLICATION PROTOCOLS
    # --------------------------------------------------------

    ("HTTP", ["Hypertext Transfer Protocol"]),
    ("HTTPS", ["secure HTTP"]),
    ("FTP", ["File Transfer Protocol"]),
    ("SFTP", ["SSH File Transfer Protocol"]),
    ("SMTP", ["Simple Mail Transfer Protocol"]),
    ("POP3", ["Post Office Protocol"]),
    ("IMAP", ["Internet Message Access Protocol"]),
    ("DNS", ["Domain Name System"]),
    ("DHCP", ["Dynamic Host Configuration Protocol"]),
    ("SSH", ["Secure Shell"]),
    ("Telnet", ["remote terminal protocol"]),
    ("SNMP", ["Simple Network Management Protocol"]),
    ("NTP", ["Network Time Protocol"]),
    ("ICMP", ["Internet Control Message Protocol"]),
    ("RDP", ["Remote Desktop Protocol"]),
    ("LDAP", ["Lightweight Directory Access Protocol"]),
    ("TFTP", ["Trivial File Transfer Protocol"]),

    # --------------------------------------------------------
    # DNS
    # --------------------------------------------------------

    ("Domain Name System", ["DNS"]),
    ("DNS Server", ["domain name server"]),
    ("DNS Resolution", ["name resolution"]),
    ("DNS Record", ["domain record"]),
    ("A Record", ["DNS A record"]),
    ("AAAA Record", ["DNS AAAA record"]),
    ("CNAME Record", ["canonical name record"]),
    ("MX Record", ["mail exchange record"]),
    ("NS Record", ["name server record"]),
    ("TXT Record", ["DNS TXT"]),
    ("PTR Record", ["reverse DNS"]),
    ("DNS Cache", ["DNS caching"]),
    ("Recursive DNS Query", ["recursive resolution"]),
    ("Authoritative DNS Server", ["authoritative name server"]),

    # --------------------------------------------------------
    # DHCP
    # --------------------------------------------------------

    ("Dynamic Host Configuration Protocol", ["DHCP"]),
    ("DHCP Server", ["DHCP service"]),
    ("DHCP Client", ["DHCP client"]),
    ("DHCP Lease", ["IP lease"]),
    ("DHCP Discover", ["DHCPDISCOVER"]),
    ("DHCP Offer", ["DHCPOFFER"]),
    ("DHCP Request", ["DHCPREQUEST"]),
    ("DHCP Acknowledgement", ["DHCPACK"]),

    # --------------------------------------------------------
    # ROUTING
    # --------------------------------------------------------

    ("Routing", ["network routing"]),
    ("Router Table", ["routing table"]),
    ("Routing Protocol", ["routing protocols"]),
    ("Static Routing", ["static route"]),
    ("Dynamic Routing", ["dynamic routing"]),
    ("Default Route", ["default routing"]),
    ("Next Hop", ["next-hop routing"]),
    ("Routing Metric", ["route metric"]),
    ("Administrative Distance", ["AD routing"]),
    ("Distance Vector Routing", ["distance vector"]),
    ("Link State Routing", ["link state"]),
    ("Path Vector Routing", ["path vector"]),
    ("RIP", ["Routing Information Protocol"]),
    ("OSPF", ["Open Shortest Path First"]),
    ("EIGRP", ["Enhanced Interior Gateway Routing Protocol"]),
    ("BGP", ["Border Gateway Protocol"]),
    ("IS IS", ["Intermediate System to Intermediate System"]),

    # --------------------------------------------------------
    # SWITCHING
    # --------------------------------------------------------

    ("Network Switching", ["switching"]),
    ("Circuit Switching", ["circuit switching"]),
    ("Packet Switching", ["packet switching"]),
    ("Message Switching", ["message switching"]),
    ("Layer 2 Switching", ["data link switching"]),
    ("Layer 3 Switching", ["multilayer switching"]),
    ("VLAN", ["Virtual LAN"]),
    ("VLAN Tagging", ["802.1Q"]),
    ("Trunk Port", ["VLAN trunk"]),
    ("Access Port", ["switch access port"]),
    ("Inter VLAN Routing", ["inter-VLAN routing"]),
    ("Spanning Tree Protocol", ["STP"]),
    ("Rapid Spanning Tree Protocol", ["RSTP"]),
    ("Port Security", ["switch port security"]),

    # --------------------------------------------------------
    # WIRELESS NETWORKING
    # --------------------------------------------------------

    ("Wireless Networking", ["wireless network"]),
    ("WiFi", ["Wi-Fi"]),
    ("WiFi Standards", ["IEEE 802.11"]),
    ("Wireless Network Security", ["WiFi security"]),
    ("SSID", ["wireless network name"]),
    ("BSSID", ["basic service set identifier"]),
    ("Wireless Channel", ["WiFi channel"]),
    ("Wireless Interference", ["radio interference"]),
    ("Bluetooth", ["Bluetooth networking"]),
    ("NFC", ["Near Field Communication"]),
    ("ZigBee", ["Zigbee wireless"]),
    ("WiMAX", ["wireless broadband"]),

    # --------------------------------------------------------
    # NETWORK PERFORMANCE
    # --------------------------------------------------------

    ("Bandwidth", ["network bandwidth"]),
    ("Latency", ["network delay"]),
    ("Throughput", ["network throughput"]),
    ("Jitter", ["network jitter"]),
    ("Packet Loss", ["packet loss"]),
    ("Round Trip Time", ["RTT"]),
    ("Goodput", ["network goodput"]),
    ("Network Availability", ["network uptime"]),
    ("Network Reliability", ["network reliability"]),
    ("Quality of Service", ["QoS"]),
    ("Traffic Shaping", ["network traffic shaping"]),
    ("Congestion", ["network congestion"]),

    # --------------------------------------------------------
    # NETWORK SECURITY
    # --------------------------------------------------------

    ("Network Security", ["network protection"]),
    ("Network Firewall", ["firewall"]),
    ("Packet Filtering", ["packet filter"]),
    ("Stateful Firewall", ["stateful inspection"]),
    ("Stateless Firewall", ["stateless filtering"]),
    ("Proxy Firewall", ["proxy firewall"]),
    ("Network Access Control", ["NAC"]),
    ("Intrusion Detection System", ["IDS"]),
    ("Intrusion Prevention System", ["IPS"]),
    ("Network Segmentation", ["network segmentation"]),
    ("Network Address Translation", ["NAT"]),
    ("Port Address Translation", ["PAT"]),
    ("Demilitarized Zone", ["DMZ"]),
    ("Secure Network Design", ["network security architecture"]),

    # --------------------------------------------------------
    # NETWORK MANAGEMENT
    # --------------------------------------------------------

    ("Network Management", ["network administration"]),
    ("Network Monitoring", ["network monitoring"]),
    ("Network Troubleshooting", ["network troubleshooting"]),
    ("Network Configuration", ["network configuration"]),
    ("Network Documentation", ["network documentation"]),
    ("Network Diagram", ["network topology diagram"]),
    ("IP Address Management", ["IPAM"]),
    ("Network Performance Monitoring", ["NPM"]),
    ("Simple Network Management Protocol", ["SNMP"]),
    ("Syslog", ["network logging"]),
    ("Ping", ["ICMP ping"]),
    ("Traceroute", ["tracert", "trace route"]),
    ("Netstat", ["network statistics"]),
    ("Nslookup", ["DNS lookup command"]),
    ("Ipconfig", ["ipconfig command"]),
    ("Ifconfig", ["ifconfig command"]),

    # --------------------------------------------------------
    # NETWORK VIRTUALIZATION
    # --------------------------------------------------------

    ("Network Virtualization", ["virtual networking"]),
    ("Virtual Network", ["virtual network"]),
    ("Software Defined Networking", ["SDN"]),
    ("Network Function Virtualization", ["NFV"]),
    ("Virtual Switch", ["vSwitch"]),
    ("Virtual Router", ["virtual routing"]),
    ("Overlay Network", ["network overlay"]),
    ("VXLAN", ["Virtual Extensible LAN"]),

    # --------------------------------------------------------
    # MODERN NETWORKING
    # --------------------------------------------------------

    ("Cloud Networking", ["cloud network"]),
    ("Edge Networking", ["edge network"]),
    ("Content Delivery Network", ["CDN"]),
    ("Network as a Service", ["NaaS"]),
    ("Zero Trust Network", ["zero trust networking"]),
    ("Network Automation", ["automated networking"]),
    ("Network Orchestration", ["network orchestration"]),
    ("IPv6 Transition", ["IPv6 migration"]),
    ("Dual Stack", ["IPv4 IPv6 dual stack"]),
]


def generate() -> list[dict]:
    """Generate the Networking knowledge family."""

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
    print("NETWORKING GENERATOR")
    print("=" * 60)
    print(f"Concepts : {len(CONCEPTS)}")
    print(f"Records  : {len(records)}")
    print("=" * 60)