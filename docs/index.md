# 🚗 Automotive Cybersecurity Laboratory

> **A hands-on automotive cybersecurity laboratory for studying CAN Bus communication, Linux SocketCAN, attack simulation, intrusion detection, and traffic analysis.**

---

## Project Overview

Modern vehicles rely on the **Controller Area Network (CAN)** to enable communication between Electronic Control Units (ECUs). While CAN is lightweight and reliable, it was originally designed without built-in security, making it vulnerable to attacks such as message spoofing, replay attacks, and bus flooding.

This project was developed to explore these concepts through a practical, hands-on laboratory environment. It combines a custom Python-based CAN simulator with a Linux SocketCAN implementation to demonstrate how CAN traffic can be generated, monitored, attacked, and analyzed.

---

## Key Features

| Feature | Status |
|---------|:------:|
| CAN Bus Simulation | ✅ |
| ECU Simulation | ✅ |
| CAN Traffic Generation | ✅ |
| CAN Message Logging | ✅ |
| Rule-Based Intrusion Detection System (IDS) | ✅ |
| Attack Simulation | ✅ |
| SocketCAN Integration | ✅ |
| Offline Traffic Analysis | ✅ |
| Automatic Report Generation | ✅ |

---

## Laboratory Architecture

![System Architecture](assets/diagrams/system_architecture.png)

📖 **Learn more:** [System Architecture](architecture.md)

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python, Bash |
| Networking | CAN Bus, SocketCAN |
| Linux Tools | can-utils (`cansend`, `candump`, `cangen`) |
| Libraries | python-can, Matplotlib |
| Documentation | GitHub Pages, Markdown |

---

## Automotive Cybersecurity Concepts Demonstrated

- CAN Bus Communication
- Electronic Control Unit (ECU) Simulation
- CAN Traffic Monitoring
- CAN Message Injection
- CAN Message Spoofing
- CAN Bus Flooding
- Rule-Based Intrusion Detection
- Traffic Logging
- Offline Forensic Analysis

---

## Project Structure

```text
automotive-security-lab/
├── src/                 # Python CAN simulator
├── socketcan/           # Linux SocketCAN laboratory
├── tools/               # Logger, IDS, analyzers
├── analysis/            # Generated charts and reports
├── docs/                # GitHub Pages documentation
└── config/              # Network configuration
```

---

## Documentation

| Page | Description |
|------|-------------|
| [Getting Started](getting-started.md) | Installation and setup |
| [System Architecture](architecture.md) | Laboratory architecture |
| [Threat Model](threat-model.md) | Security analysis |
| [SocketCAN Lab](socketcan.md) | Linux CAN laboratory |
| [Results](results.md) | Analysis and charts |

---

## Skills Demonstrated

This project showcases practical experience in:

- Automotive Networking
- Embedded Systems Concepts
- Linux Development
- CAN Bus Protocol
- SocketCAN
- Python Development
- Threat Modeling
- Intrusion Detection Systems
- Traffic Analysis
- Technical Documentation

---

## Future Enhancements

- Replay Attack Demonstration
- DBC File Support
- CAN FD Support
- ISO-TP Demonstration
- Secure ECU Authentication
- Unit Testing
- Continuous Integration (GitHub Actions)

---

## Author

**Boluwatife Ekundayo**

Electrical & Electronics Engineer focused on Embedded Systems and Automotive Cybersecurity.

- GitHub: https://github.com/Tife28
- LinkedIn: https://www.linkedin.com/in/boluwatife-ekundayo
