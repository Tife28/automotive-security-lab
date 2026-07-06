# SocketCAN Laboratory

This branch extends the Automotive Cybersecurity Lab by replacing the Python-only CAN bus simulation with a Linux SocketCAN environment. It demonstrates realistic CAN traffic generation, CAN traffic capture, attack simulation, and intrusion detection using industry-standard Linux tools.

---

# Prerequisites

- Ubuntu or another Linux distribution with SocketCAN support
- Python 3.10+
- Git
- can-utils
- python-can

---

# Clone the Repository

```bash
git clone --branch socketcan-lab --single-branch https://github.com/Tife28/automotive-security-lab.git

cd automotive-security-lab
```

---

# Install Dependencies

Install CAN utilities.

```bash
sudo apt update

sudo apt install can-utils
```

Install the Python dependency.

```bash
pip install python-can
```

---

# Start the laboratory.

```bash
chmod +x start_lab.sh stop_lab.sh

./start_lab.sh
```

The script automatically:

- Creates the `vcan0` interface
- Starts the CAN traffic monitor
- Starts the simulated ECUs
- Starts the SocketCAN IDS

View the live outputs in separate terminals:

```bash
tail -f runtime_logs/candump.log
```

```bash
tail -f runtime_logs/ecu.log
```

```bash
tail -f runtime_logs/ids.log
```

Launch attack scenarios:

```bash
./socketcan/attacks/run_attacks.sh
```

Stop the laboratory:

```bash
./stop_lab.sh
```
---

# Project Workflow

```text
Engine ECU ─┐
            │
Speed ECU ──┼──────────────► SocketCAN (vcan0)
            │                      │
Body ECU ───┘                      │
                                   ├────────► candump
                                   │
Attack Modules ───────────────────►│
                                   │
                                   └────────► Python IDS
                                               │
                                               ▼
                                           Security Alerts
```

---

# Technologies

- Linux SocketCAN
- CAN-utils (`cansend`, `candump`, `cangen`)
- Python
- python-can
- Virtual CAN (`vcan`)
- Controller Area Network (CAN)
- Automotive Intrusion Detection
