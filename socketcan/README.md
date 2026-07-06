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

# Step 1 — Create the Virtual CAN Interface

Run:

```bash
chmod +x socketcan/*.sh

./socketcan/setup_vcan.sh
```

Verify that the interface exists.

```bash
./socketcan/verify.sh
```

You should see a `vcan0` interface listed.

---

# Step 2 — Open Four Terminal Windows

The lab is designed to mimic multiple ECUs communicating over a CAN network. Open **four terminals** inside the project directory.

---

## Terminal 1 — CAN Traffic Monitor

Start a live CAN capture.

```bash
candump vcan0
```

This displays every CAN frame transmitted on the virtual CAN bus.

---

## Terminal 2 — Start the Simulated ECUs

Launch the Engine, Speed and Body ECUs.

```bash
chmod +x socketcan/ecus/*.sh

./socketcan/ecus/run_all_ecus.sh
```

This continuously generates normal vehicle CAN traffic.

---

## Terminal 3 — Start the SocketCAN IDS

Launch the intrusion detection system.

```bash
python tools/socketcan_ids.py
```

The IDS listens on `vcan0`, decodes CAN frames and checks for anomalies.

---

## Terminal 4 — Launch Attack Scenarios

Run the attack scripts.

```bash
chmod +x socketcan/attacks/*.sh

./socketcan/attacks/run_attacks.sh
```

This injects malicious CAN frames onto the virtual CAN bus.

---

# Expected Behaviour

**Terminal 1** should display a continuous stream of CAN frames.

**Terminal 2** should report that all simulated ECUs are running.

**Terminal 3** should display decoded ECU messages similar to:

```text
[ENGINE] RPM=2450 LOAD=54%

[SPEED] 78 km/h

[BODY] Door LOCKED
```

When attack traffic is injected, the IDS should produce alerts such as:

```text
[ALERT] RPM Spoofing Detected

RPM = 9000
```

and

```text
[ALERT] Speed Spoofing Detected

Speed = 240 km/h
```

---

# Optional — Bus Flooding Demonstration

To simulate a denial-of-service style CAN bus flooding attack, open an additional terminal and run:

```bash
./socketcan/attacks/bus_flood.sh
```

This uses `cangen` to generate high volumes of random CAN frames.

---

# Stop the Lab

Terminate the running scripts using **Ctrl + C**.

Remove the virtual CAN interface.

```bash
./socketcan/cleanup_vcan.sh
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
