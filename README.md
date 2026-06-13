# Automotive Cybersecurity Lab

## Overview

The Automotive Cybersecurity Lab is a Python-based simulation of an in-vehicle Controller Area Network (CAN) environment designed to explore vehicle network security concepts. The project demonstrates how Electronic Control Units (ECUs) communicate over a CAN bus, how attackers can inject malicious messages, and how basic intrusion detection techniques can be used to identify abnormal behavior.

This project was built as a hands-on learning environment for studying automotive cybersecurity, CAN communication, attack simulation, and defensive monitoring.

---

## Learning Objectives

* Understand CAN bus communication
* Simulate ECU behavior and vehicle signals
* Explore common automotive attack scenarios
* Implement basic intrusion detection techniques
* Analyze and log CAN traffic
* Apply threat modeling concepts to vehicle networks

---

## Features

### Implemented

* ECU simulation

  * Engine ECU
  * Speed ECU
  * Body ECU

* CAN message generation

* Attack simulation

  * RPM spoofing
  * Speed spoofing

* Rule-based Intrusion Detection System (IDS)

* Traffic logging and analysis

### Planned

* Replay attack simulation
* CAN bus flooding attacks
* SocketCAN integration
* Wireshark traffic analysis
* Machine-learning anomaly detection
* Real CAN hardware integration

---

## System Architecture

```text
+-------------+
| Engine ECU  |
+-------------+

+-------------+
| Speed ECU   |
+-------------+

+-------------+
| Body ECU    |
+-------------+
        |
        v
+----------------+
| Simulated CAN  |
|      Bus       |
+----------------+
        |
        +----------------+
        |                |
        v                v
+----------------+  +----------------+
| IDS Module     |  | Logger Module  |
+----------------+  +----------------+
        ^
        |
+----------------+
| Attacker       |
+----------------+
```

---

## Attack Scenarios

### RPM Spoofing

The attacker injects CAN messages containing unrealistic engine RPM values in an attempt to override legitimate ECU data.

Detection Method:
The IDS raises an alert when RPM exceeds a predefined threshold.

### Speed Spoofing

The attacker injects false vehicle speed values to simulate overspeed conditions.

Detection Method:
The IDS raises an alert when vehicle speed exceeds expected operating limits.

---

## IDS Methodology

The IDS uses threshold-based anomaly detection.

Detection Rules:

* RPM > 6500 RPM → Alert
* Speed > 180 km/h → Alert
* Explicit attack messages → Alert

---

## Example Output

```text
{
  "timestamp": 1781345741.1235647,
  "can_id": "0x102",
  "data": {
    "speed_kmh": 212
  },
  "ATTACK": true
}
[ALERT] ATTACK MESSAGE DETECTED: {'timestamp': 1781345741.1235647, 'can_id': '0x102', 'data': {'speed_kmh': 212}, 'ATTACK': True}
[ALERT] Speed anomaly detected: {'timestamp': 1781345741.1235647, 'can_id': '0x102', 'data': {'speed_kmh': 212}, 'ATTACK': True}
[LOGGED] {'timestamp': 1781345741.1235647, 'can_id': '0x102', 'data': {'speed_kmh': 212}, 'ATTACK': True}
------------------------------------------------------------
[IDS RECEIVED] {'debug': 'simulator alive'}
[LOGGED] {'debug': 'simulator alive'}
{
  "timestamp": 1781345741.1284976,
  "can_id": "0x101",
  "data": {
    "rpm": 3871,
    "load": 33
  }
}
[IDS RECEIVED] {'timestamp': 1781345741.1284976, 'can_id': '0x101', 'data': {'rpm': 3871, 'load': 33}}
[LOGGED] {'timestamp': 1781345741.1284976, 'can_id': '0x101', 'data': {'rpm': 3871, 'load': 33}}
```

---

## Project Structure

```text
automotive-security-lab/
│
├── analysis/
│   ├── ecu_distribution.png
│   ├── rpm_chart.png
│   └── speed_chart.png
│ 
├── config/
│   └── vehicle_network.json
│   
├── diagrams/
│   ├── can_simulator.png
│   ├── ids_alerts.png
│   └── logs.png
│   
├── docs/
│   ├── threat_model.md
│   └── architecture.md
│
├── logs/
│   ├── sample_can_traffic.log
│   └── bus_logger.py
│
├── src/
│   └── can_simulator/
│       ├── attacker.py
│       ├── can_bus.py
│       ├── can_simulator.py
│       ├── ids.py
│       └── main.py
│   
├── tools/
│   ├── can_sniffer.py
│   └── log_analyzer.py
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Lessons Learned

* CAN networks do not provide native message authentication.
* Any device with CAN bus access can inject messages.
* Message spoofing can manipulate perceived vehicle state.
* Intrusion detection systems improve visibility into malicious activity.
* Logging and monitoring are essential for incident investigation.

---

## Limitations

* Uses a simulated CAN bus rather than physical CAN hardware.
* IDS relies on static threshold rules.
* ECU behavior is simplified for educational purposes.
* Does not implement cryptographic message authentication.

---

## Technologies Used

* Python
* Linux
* CAN Concepts
* JSON
* SocketCAN (planned)
* Wireshark (planned)

---

## Author

Electrical & Electronics Engineer transitioning into Automotive Cybersecurity with a focus on vehicle network security, embedded systems, and intrusion detection.
