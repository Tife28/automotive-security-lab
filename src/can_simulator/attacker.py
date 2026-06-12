import time
import random
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from can_bus import send

TARGET_CAN_IDS = ["0x101", "0x102"]  # Engine + Speed ECUs


def spoof_rpm():
    return {
        "rpm": random.randint(7000, 9000),  # unrealistic high RPM
        "load": random.randint(95, 100)
    }


def spoof_speed():
    return {
        "speed_kmh": random.randint(180, 260)  # fake overspeed
    }


def format_attack(can_id, data):
    return {
        "timestamp": time.time(),
        "can_id": can_id,
        "data": data,
        "ATTACK": True
    }


def main():
    print("\n[!] ATTACKER MODULE STARTED - Injecting CAN messages...\n")

    while True:
        attack_rpm = format_attack("0x101", spoof_rpm())
        attack_speed = format_attack("0x102", spoof_speed())

        print(json.dumps(attack_rpm, indent=2))
        print(json.dumps(attack_speed, indent=2))
        send(attack_rpm)
        send(attack_speed)

        print("-" * 60)
        time.sleep(2)


if __name__ == "__main__":
    main()
