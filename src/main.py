import subprocess
import time

print("Starting Automotive Cybersecurity Lab...\n")

# Start simulator
sim = subprocess.Popen(["python", "src/can_simulator/can_simulator.py"])

time.sleep(2)

# Start attacker
attacker = subprocess.Popen(["python", "src/can_simulator/attacker.py"])

print("System running: Simulator + Attacker active")

sim.wait()
attacker.wait()
