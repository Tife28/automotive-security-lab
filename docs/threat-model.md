# Threat Model

This document identifies the primary security threats addressed by the Automotive Cybersecurity Laboratory. The analysis is based on a simplified Controller Area Network (CAN) architecture and demonstrates common attack techniques against in-vehicle communication systems.

---

# Objectives

The purpose of this threat model is to:

- Identify critical assets within the simulated vehicle network.
- Analyze potential attack vectors.
- Demonstrate representative automotive cyber attacks.
- Evaluate basic detection mechanisms.
- Propose future security improvements.

---

# Laboratory Scope

The threat model applies to the simulated in-vehicle network implemented in this project.

Included components:

- Engine ECU
- Speed ECU
- Body ECU
- Virtual CAN Bus (SocketCAN)
- CAN Logger
- Intrusion Detection System (IDS)

Out of scope:

- Secure Boot
- ECU firmware security
- Automotive Ethernet
- Telematics
- Over-the-Air (OTA) updates
- Hardware security modules (HSMs)

---

# Protected Assets

| Asset | Description | Importance |
|--------|-------------|------------|
| CAN Bus | Communication backbone between ECUs | High |
| Engine ECU | Engine RPM and load information | High |
| Speed ECU | Vehicle speed information | High |
| Body ECU | Door lock status | Medium |
| CAN Logs | Captured network traffic | Medium |
| IDS | Detects malicious CAN traffic | High |

---

# Threat Actors

The following attacker profiles are considered.

| Threat Actor | Capability |
|--------------|------------|
| Malicious Insider | Physical access to the CAN network |
| Vehicle Owner | Access to diagnostic interfaces |
| Researcher | Security testing in a laboratory |
| Adversary | CAN message injection and spoofing |

---

# Attack Surface

Potential entry points include:

- OBD-II diagnostic connector
- Compromised ECU
- Rogue CAN node
- Diagnostic tools
- Linux SocketCAN interface (`vcan0`) during laboratory testing

---

# Attack Scenarios

## Scenario 1 — Engine RPM Spoofing

### Description

An attacker injects CAN frames containing unrealistic engine RPM values.

### Goal

Cause other ECUs to process incorrect engine information.

### Impact

- Incorrect dashboard readings
- Invalid engine telemetry
- Potential safety implications in a real vehicle

### Detection

The IDS raises an alert when:

```text
RPM > 6500
```

---

## Scenario 2 — Vehicle Speed Spoofing

### Description

The attacker injects false vehicle speed messages.

### Goal

Override legitimate speed information.

### Impact

- Incorrect speed display
- False telemetry
- Safety risks in dependent systems

### Detection

The IDS raises an alert when:

```text
Vehicle Speed > 180 km/h
```

---

## Scenario 3 — CAN Bus Flooding

### Description

A high volume of CAN frames is transmitted using `cangen`, consuming bus bandwidth.

### Goal

Reduce availability of legitimate CAN communication.

### Impact

- Increased network load
- Delayed legitimate messages
- Reduced network reliability

### Detection

Currently identified through abnormal traffic volume during offline analysis.

Future work will include automated rate-based detection.

---

## Scenario 4 — CAN Message Injection

### Description

An attacker transmits arbitrary CAN frames using tools such as `cansend`.

### Goal

Impersonate a legitimate ECU.

### Impact

- Spoofed vehicle signals
- Incorrect ECU behavior
- False sensor data

### Detection

Detected through rule-based anomaly analysis and log inspection.

---

# Threat Summary

| Threat | Likelihood | Impact | Current Detection |
|----------|-----------|--------|-------------------|
| RPM Spoofing | Medium | High | Rule-Based IDS |
| Speed Spoofing | Medium | High | Rule-Based IDS |
| Message Injection | Medium | High | Partial |
| CAN Flooding | Low | High | Offline Analysis |

---

# Current Security Controls

The laboratory currently implements:

- CAN traffic logging
- Rule-based intrusion detection
- Threshold-based anomaly detection
- Offline traffic analysis
- Attack simulation
- Structured reporting

---

# Limitations

This project intentionally simplifies several aspects of production vehicle security.

The laboratory does **not** currently implement:

- CAN authentication
- Message integrity protection
- ECU authentication
- Secure gateways
- Cryptographic key management
- Secure diagnostics
- CAN FD security mechanisms

These limitations are intentional to keep the project focused on demonstrating core CAN security concepts.

---

# Future Improvements

Planned enhancements include:

- Replay attack detection
- CAN message authentication
- Statistical anomaly detection
- Machine learning-based IDS
- DBC-aware CAN decoding
- CAN FD support
- UDS diagnostic message monitoring
- ISO-TP communication analysis

---

# Conclusion

This threat model demonstrates how common attacks against a CAN network can be reproduced within a controlled laboratory environment. The project combines attack simulation, traffic logging, intrusion detection, and offline analysis to illustrate practical automotive cybersecurity concepts while providing a platform for future experimentation and research.
