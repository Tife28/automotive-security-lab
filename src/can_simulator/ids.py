from can_bus import subscribe
import time

MAX_RPM = 6500
MAX_SPEED = 180


def process(msg):
    print("[IDS RECEIVED]", msg)

    data = msg.get("data", {})

    # 🚨 Explicit attack detection
    if msg.get("ATTACK") == True:
        print("[ALERT] ATTACK MESSAGE DETECTED:", msg)

    # 🚨 RPM anomaly
    if "rpm" in data and data["rpm"] > MAX_RPM:
        print("[ALERT] RPM anomaly detected:", msg)

    # 🚨 Speed anomaly
    if "speed_kmh" in data and data["speed_kmh"] > MAX_SPEED:
        print("[ALERT] Speed anomaly detected:", msg)


def main():
    print("[IDS] Live monitoring started...\n")

    subscribe(process)
    
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
