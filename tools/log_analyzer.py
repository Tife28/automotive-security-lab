import json

def analyze_log(file_path):
    print("Analyzing CAN log...\n")

    with open(file_path, "r") as f:
        for line in f:
            msg = json.loads(line)

            if "rpm" in str(msg):
                if isinstance(msg.get("data", {}).get("rpm"), int):
                    if msg["data"]["rpm"] > 6500:
                        print("[ALERT] RPM anomaly detected:", msg)


if __name__ == "__main__":
    analyze_log("logs/sample_can_traffic.log")
