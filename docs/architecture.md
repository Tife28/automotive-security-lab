# System Architecture

## Overview

The Automotive Cybersecurity Lab simulates a simplified in-vehicle network environment. Multiple ECUs generate CAN messages, an attacker module injects malicious traffic, and a monitoring system observes and records network activity.

---

## Architecture Diagram

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

## Components

### ECU Simulator

Responsibilities:

* Generate normal CAN traffic
* Simulate vehicle signals
* Emulate ECU behavior

Examples:

* Engine RPM
* Vehicle Speed
* Door Lock Status

---

### Simulated CAN Bus

Responsibilities:

* Deliver messages between components
* Emulate CAN network behavior
* Provide a common communication channel

---

### Attacker Module

Responsibilities:

* Inject malicious CAN messages
* Simulate ECU spoofing
* Generate abnormal vehicle data

Implemented Attacks:

* RPM spoofing
* Speed spoofing

---

### Intrusion Detection System (IDS)

Responsibilities:

* Monitor CAN traffic
* Detect anomalous messages
* Generate security alerts

Current Detection Methods:

* RPM threshold monitoring
* Speed threshold monitoring
* Explicit attack flag detection

---

### Logger

Responsibilities:

* Record CAN traffic
* Support forensic analysis
* Provide historical records for investigation

---

## Data Flow

1. ECU simulator generates CAN messages.
2. Messages are transmitted onto the simulated CAN bus.
3. IDS receives a copy of each message and performs analysis.
4. Logger records all traffic.
5. Attacker injects malicious messages.
6. IDS detects anomalies and generates alerts.

---

## Security Monitoring Design

The IDS operates passively and does not interfere with normal CAN communications. It observes network traffic and raises alerts when messages violate predefined safety thresholds.

This approach mimics the behavior of monitoring systems commonly deployed in automotive cybersecurity environments.

---

## Design Decisions

### Why Python?

Python enables rapid prototyping and experimentation.

### Why a Simulated CAN Bus?

The simulation allows automotive security concepts to be explored without requiring specialized hardware.

### Why Threshold-Based Detection?

Threshold-based detection is easy to implement, validate, and explain while demonstrating fundamental IDS concepts.

---

## Future Improvements

* SocketCAN integration
* Physical CAN hardware support
* Replay attack detection
* CAN bus flooding detection
* Machine-learning anomaly detection
* Gateway ECU simulation
* Real-time dashboard visualization
