# Getting Started

This guide explains how to recreate the Automotive Cybersecurity Laboratory from scratch on a Linux system.

---

# Prerequisites

The laboratory has been developed and tested on **Ubuntu 24.04 LTS**, but should work on most modern Linux distributions with SocketCAN support.

## Required Software

| Software | Purpose |
|----------|---------|
| Python 3.10+ | ECU simulation and analysis |
| Git | Clone the repository |
| SocketCAN | Linux CAN networking |
| can-utils | CAN traffic generation and monitoring |
| pip | Install Python dependencies |

---

# Clone the Repository

Clone the SocketCAN laboratory branch:

```bash
git clone --branch socketcan-lab --single-branch https://github.com/Tife28/automotive-security-lab.git

cd automotive-security-lab
```

---

# Install System Dependencies

Ubuntu/Debian:

```bash
sudo apt update

sudo apt install can-utils python3-pip
```

---

# Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
automotive-security-lab/
│
├── src/
├── socketcan/
├── tools/
├── docs/
├── analysis/
└── logs/
```

---

# Start the Laboratory

The startup script automatically:

- Loads the Virtual CAN kernel module
- Creates the `vcan0` interface
- Starts the CAN logger
- Starts the Intrusion Detection System
- Starts the ECU simulator

Run:

```bash
chmod +x start_lab.sh stop_lab.sh socketcan/*.sh socketcan/attacks/*.sh socketcan/ecus/*.sh

sudo ./start_lab.sh
```

Expected output:

```text
Creating virtual CAN interface...
Starting CAN logger...
Starting IDS...
Starting ECU simulator...

Laboratory started successfully.
```

---

# Open a Second Terminal

Verify that the CAN interface is active:

```bash
ip link show vcan0
```

Expected:

```text
vcan0: <NOARP,UP,LOWER_UP>
```

---

# Open a Third Terminal

Monitor live CAN traffic:

```bash
candump vcan0
```

Example output:

```text
vcan0  101   [2]  12 34
vcan0  102   [2]  00 65
vcan0  103   [1]  01
```

---

# Open a Fourth Terminal

Run the attack demonstration:

```bash
./socketcan/attacks/run_attacks.sh
```

The attack script injects malicious CAN frames onto the virtual CAN network.

---

# Open a Fifth Terminal

Monitor IDS alerts:

```bash
tail -f runtime_logs/ids.log
```

Example:

```text
[ALERT] RPM anomaly detected
CAN ID: 0x101
RPM: 8950

[ALERT] Speed anomaly detected
CAN ID: 0x102
Speed: 240 km/h
```

---

# Analyze the Captured Traffic

After stopping the laboratory, generate analysis charts and reports:

```bash
python3 tools/socketcan_log_analyzer.py
```

Generated output:

```text
analysis/

socketcan_rpm_chart.png

socketcan_speed_chart.png

socketcan_ecu_distribution.png

socketcan_attack_summary.png

socketcan_report.md
```

---

# Stop the Laboratory

To terminate all running processes and clean up the virtual CAN interface:

```bash
./stop_lab.sh
```

---

# Troubleshooting

## `vcan0` does not exist

Load the Virtual CAN kernel module:

```bash
sudo modprobe vcan
```

---

## `candump` reports "No such device"

Create the virtual interface:

```bash
sudo ip link add dev vcan0 type vcan

sudo ip link set up vcan0
```

---

## Permission denied when running scripts

Make the scripts executable:

```bash
chmod +x start_lab.sh

chmod +x stop_lab.sh
```

---

## CAN traffic is not visible

Verify:

- `vcan0` is up
- The ECU simulator is running
- `candump` is listening on `vcan0`

---

# Next Steps

Once the laboratory is running successfully, continue with:

- [SocketCAN Laboratory](socketcan.md)
- [System Architecture](architecture.md)
- [Threat Model](threat_model.md)
- [Analysis Results](results.md)
