# Threat Model

## System Description

The Automotive Cybersecurity Lab simulates multiple Electronic Control Units (ECUs) communicating over a Controller Area Network (CAN). The environment is used to study common automotive cyber threats and evaluate basic intrusion detection techniques.

---

## Assets

The following assets require protection:

* CAN bus communications
* ECU integrity
* Vehicle speed information
* Engine RPM information
* Door lock status
* Availability of vehicle communications
* Accuracy of sensor data

---

## Threat Actors

Potential attackers include:

* Individuals with physical access to the vehicle
* Malicious maintenance personnel
* Rogue aftermarket devices
* Compromised ECUs
* Attackers with access through diagnostic interfaces

---

## Trust Boundaries

### External Device → CAN Bus

Examples:

* OBD-II tools
* Aftermarket telematics devices
* Diagnostic equipment

Traffic crossing this boundary should not automatically be trusted.

---

## Attack Scenarios

### 1. Speed Spoofing

Entry Point:
Compromised ECU or OBD-II connection.

Attack Method:
Inject false speed values onto the CAN bus.

Impact:
Driver receives inaccurate speed information and downstream systems may make incorrect decisions.

Detection:
IDS triggers when speed exceeds configured thresholds.

---

### 2. RPM Spoofing

Entry Point:
Compromised ECU.

Attack Method:
Inject fraudulent engine RPM values.

Impact:
False engine state information may be presented to vehicle systems.

Detection:
IDS triggers when RPM exceeds expected operating limits.

---

### 3. Replay Attack

Entry Point:
Captured CAN traffic.

Attack Method:
Previously recorded CAN messages are retransmitted onto the network.

Impact:
Vehicle systems may accept outdated or fraudulent information.

Detection:
Future enhancement.

---

### 4. Bus Flooding

Entry Point:
Malicious device connected to the CAN bus.

Attack Method:
Transmit excessive CAN traffic to consume bus bandwidth.

Impact:
Legitimate ECU communications may be delayed or disrupted.

Detection:
Future enhancement.

---

## Risk Assessment

| Threat         | Likelihood | Impact |
| -------------- | ---------- | ------ |
| Speed Spoofing | Medium     | High   |
| RPM Spoofing   | Medium     | Medium |
| Replay Attack  | Medium     | Medium |
| Bus Flooding   | High       | High   |

---

## Mitigations

Potential defensive measures include:

* Intrusion Detection Systems
* Message authentication mechanisms
* Secure ECU firmware
* Gateway ECU filtering
* Network segmentation
* Traffic monitoring and logging

---

## Assumptions

This threat model assumes that an attacker has already gained access to the CAN network through a compromised ECU, diagnostic interface, or connected device.
