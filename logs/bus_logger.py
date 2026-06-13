from can_bus import subscribe
import os
import json
import time

LOG_FILE = "logs/sample_can_traffic.log"

def log(msg):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_dir, LOG_FILE)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    print("Writing to:", full_path)
    with open(full_path, "a") as f:
        f.write(json.dumps(msg) + "\n")

    print("[LOGGED]", msg)

def main():
    print("[LOGGER] Started...\n")

    subscribe(log)

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
