import subprocess
import os
import time

print("Starting Automotive Cybersecurity Lab...\n")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SIM_PATH = os.path.join(BASE_DIR, "can_simulator/can_simulator.py")
ATTACKER_PATH = os.path.join(BASE_DIR, "can_simulator/attacker.py")

# Start simulator
sim = subprocess.Popen(["python3", SIM_PATH])

time.sleep(2)

# Start attacker
attacker = subprocess.Popen(["python3", ATTACKER_PATH])

print("System running: Simulator + Attacker active")

sim.wait()
attacker.wait()
