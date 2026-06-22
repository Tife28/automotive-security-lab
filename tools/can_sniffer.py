import can

print("Listening on vcan0...\n")

bus = can.interface.Bus(
    channel="vcan0",
    interface="socketcan"
)

while True:
    msg = bus.recv()

    print(
        f"ID=0x{msg.arbitration_id:X} "
        f"DATA={msg.data.hex()}"
    )
