import json
import time

def log_message(message, filename="logs/sample_can_traffic.log"):
    with open(filename, "a") as f:
        f.write(json.dumps(message) + "\n")
