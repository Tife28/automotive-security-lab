import time
import json
import os
from can_bus import CAN_BUS

LOG_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "logs/sample_can_traffic.log"
)

print("[LOGGER] Started logging CAN traffic...\n")

while True:
    if not CAN_BUS.empty():
        msg = CAN_BUS.get()

        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(msg) + "\n")

    time.sleep(0.1)
