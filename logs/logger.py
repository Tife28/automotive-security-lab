import json
import os

def log_message(message, filename="logs/sample_can_traffic.log"):
    # Ensure correct path relative to project root
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    full_path = os.path.join(base_dir, filename)

    # Ensure logs folder exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "a") as f:
        f.write(json.dumps(message) + "\n")
