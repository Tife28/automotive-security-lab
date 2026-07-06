import can
import json
import os
import time

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "socketcan_traffic.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)

print("=" * 60)
print("SocketCAN Logger")
print("=" * 60)
print(f"Writing to: {LOG_FILE}\n")

bus = can.interface.Bus(
    channel="vcan0",
    interface="socketcan"
)

while True:
    msg = bus.recv()

    record = {
        "timestamp": time.time(),
        "can_id": hex(msg.arbitration_id),
        "data": list(msg.data)
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

    print(record)
