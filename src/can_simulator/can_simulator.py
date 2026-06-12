import time
import random
import json
from logs.logger import log_message
log_message(msg)

# Simulated CAN message IDs (like real automotive ECUs)
ENGINE_ECU_ID = 0x101
SPEED_ECU_ID = 0x102
BODY_ECU_ID = 0x103


def generate_engine_data():
    return {
        "rpm": random.randint(800, 6000),
        "load": random.randint(10, 90)
    }


def generate_speed_data():
    return {
        "speed_kmh": random.randint(0, 180)
    }


def generate_body_data():
    return {
        "door_lock": random.choice(["LOCKED", "UNLOCKED"])
    }


def format_can_message(can_id, data):
    return {
        "timestamp": time.time(),
        "can_id": hex(can_id),
        "data": data
    }


def main():
    print("Starting CAN Bus Simulation...\n")

    while True:
        engine_msg = format_can_message(ENGINE_ECU_ID, generate_engine_data())
        speed_msg = format_can_message(SPEED_ECU_ID, generate_speed_data())
        body_msg = format_can_message(BODY_ECU_ID, generate_body_data())

        messages = [engine_msg, speed_msg, body_msg]

        for msg in messages:
            print(json.dumps(msg, indent=2))

        print("-" * 50)
        time.sleep(2)


if __name__ == "__main__":
    main()
