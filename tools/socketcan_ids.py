import can

MAX_RPM = 6500
MAX_SPEED = 180

print("=" * 60)
print(" SocketCAN Intrusion Detection System")
print("=" * 60)
print("Listening on vcan0...\n")

bus = can.interface.Bus(
    channel="vcan0",
    interface="socketcan"
)

while True:

    msg = bus.recv()

    can_id = msg.arbitration_id
    data = list(msg.data)

    # -------------------------
    # Engine ECU
    # -------------------------

    if can_id == 0x101:

        if len(data) >= 3:

            rpm = (data[0] << 8) | data[1]
            load = data[2]

            print(
                f"[ENGINE] RPM={rpm}  LOAD={load}%"
            )

            if rpm > MAX_RPM:

                print(
                    f"\n[ALERT] RPM Spoofing Detected!"
                )

                print(
                    f"RPM = {rpm}\n"
                )

    # -------------------------
    # Speed ECU
    # -------------------------

    elif can_id == 0x102:

        if len(data) >= 1:

            speed = data[0]

            print(
                f"[SPEED] {speed} km/h"
            )

            if speed > MAX_SPEED:

                print(
                    f"\n[ALERT] Speed Spoofing Detected!"
                )

                print(
                    f"Speed = {speed} km/h\n"
                )

    # -------------------------
    # Body ECU
    # -------------------------

    elif can_id == 0x103:

        if len(data) >= 1:

            state = "LOCKED"

            if data[0] == 0:
                state = "UNLOCKED"

            print(
                f"[BODY] Door {state}"
            )

    else:

        print(
            f"[UNKNOWN] ID=0x{can_id:X}"
        )