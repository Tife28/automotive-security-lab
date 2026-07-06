import json
import os
import matplotlib.pyplot as plt

LOG_FILE = "logs/socketcan_traffic.jsonl"

rpm = []
speed = []

engine = 0
speed_ecu = 0
body = 0

rpm_alerts = 0
speed_alerts = 0

with open(LOG_FILE) as f:

    for line in f:

        msg = json.loads(line)

        can_id = msg["can_id"]
        data = msg["data"]

        if can_id == "0x101":

            engine += 1

            value = (data[0] << 8) | data[1]

            rpm.append(value)

            if value > 6500:
                rpm_alerts += 1

        elif can_id == "0x102":

            speed_ecu += 1

            value = data[0]

            speed.append(value)

            if value > 180:
                speed_alerts += 1

        elif can_id == "0x103":

            body += 1

os.makedirs("analysis", exist_ok=True)

# RPM Chart

plt.figure(figsize=(10,4))
plt.plot(rpm)
plt.title("Engine RPM")
plt.xlabel("Frame")
plt.ylabel("RPM")
plt.grid(True)
plt.savefig("analysis/socketcan_rpm_chart.png")
plt.close()

# Speed Chart

plt.figure(figsize=(10,4))
plt.plot(speed)
plt.title("Vehicle Speed")
plt.xlabel("Frame")
plt.ylabel("km/h")
plt.grid(True)
plt.savefig("analysis/socketcan_speed_chart.png")
plt.close()

# ECU Distribution

plt.figure(figsize=(6,5))

plt.bar(
    ["Engine","Speed","Body"],
    [engine,speed_ecu,body]
)

plt.title("ECU Distribution")

plt.savefig(
    "analysis/socketcan_ecu_distribution.png"
)

plt.close()

print("="*50)

print("SocketCAN Analysis Complete\n")

print(f"Engine Frames : {engine}")
print(f"Speed Frames  : {speed_ecu}")
print(f"Body Frames   : {body}")

print()

print(f"RPM Alerts    : {rpm_alerts}")
print(f"Speed Alerts  : {speed_alerts}")

print()

print("Charts saved in analysis/")
