import time
import json

# Simple baseline thresholds (real-world inspired)
MAX_RPM = 6500
MAX_SPEED = 180


def analyze_message(msg):
    data = msg["data"]

    alerts = []

    # RPM anomaly detection
    if "rpm" in data:
        if data["rpm"] > MAX_RPM:
            alerts.append(f"RPM anomaly detected: {data['rpm']}")

    # Speed anomaly detection
    if "speed_kmh" in data:
        if data["speed_kmh"] > MAX_SPEED:
            alerts.append(f"Speed anomaly detected: {data['speed_kmh']} km/h")

    return alerts


def main():
    print("\n[IDS] Intrusion Detection System Started...\n")

    while True:
        # In real systems this would read CAN bus
        # Here we simulate input via manual paste/log file concept

        raw_input_msg = input("Enter CAN message (JSON): ")

        try:
            msg = json.loads(raw_input_msg)
            alerts = analyze_message(msg)

            if alerts:
                print("\n[!!! ALERT !!!]")
                for alert in alerts:
                    print(alert)
            else:
                print("[OK] Message normal")

        except Exception as e:
            print("Invalid message format")

        print("-" * 50)


if __name__ == "__main__":
    main()
