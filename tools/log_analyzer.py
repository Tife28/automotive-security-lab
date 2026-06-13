import json
import os
import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "logs/sample_can_traffic.log"
OUTPUT_DIR = "analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)

records = []

# Read JSON lines log file
with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            print(f"Skipping malformed line: {line}")

print(f"Loaded {len(records)} CAN messages")

# -------------------------
# RPM DATA
# -------------------------

rpm_rows = []

for msg in records:
    if msg.get("can_id") == "0x101":
        data = msg.get("data", {})

        if "rpm" in data:
            rpm_rows.append({
                "timestamp": msg["timestamp"],
                "rpm": data["rpm"]
            })

rpm_df = pd.DataFrame(rpm_rows)

if not rpm_df.empty:
    rpm_df["elapsed_time"] = (
        rpm_df["timestamp"] - rpm_df["timestamp"].min()
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        rpm_df["elapsed_time"],
        rpm_df["rpm"],
        marker="o"
    )
    plt.title("Engine RPM Over Time")
    plt.xlabel("Elapsed Time (seconds)")
    plt.ylabel("RPM")
    plt.grid(True)
    plt.tight_layout()

    rpm_chart = os.path.join(OUTPUT_DIR, "rpm_chart.png")
    plt.savefig(rpm_chart)
    plt.close()

    print(f"Saved {rpm_chart}")

# -------------------------
# SPEED DATA
# -------------------------

speed_rows = []

for msg in records:
    if msg.get("can_id") == "0x102":
        data = msg.get("data", {})

        if "speed_kmh" in data:
            speed_rows.append({
                "timestamp": msg["timestamp"],
                "speed_kmh": data["speed_kmh"]
            })

speed_df = pd.DataFrame(speed_rows)

if not speed_df.empty:
    speed_df["elapsed_time"] = (
        speed_df["timestamp"] - speed_df["timestamp"].min()
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        speed_df["elapsed_time"],
        speed_df["speed_kmh"],
        marker="o"
    )
    plt.title("Vehicle Speed Over Time")
    plt.xlabel("Elapsed Time (seconds)")
    plt.ylabel("Speed (km/h)")
    plt.grid(True)
    plt.tight_layout()

    speed_chart = os.path.join(OUTPUT_DIR, "speed_chart.png")
    plt.savefig(speed_chart)
    plt.close()

    print(f"Saved {speed_chart}")

# -------------------------
# ECU MESSAGE DISTRIBUTION
# -------------------------

ecu_mapping = {
    "0x101": "Engine ECU",
    "0x102": "Speed ECU",
    "0x103": "Body ECU"
}

ecu_counts = {}

for msg in records:
    can_id = msg.get("can_id")

    ecu_name = ecu_mapping.get(can_id, can_id)

    ecu_counts[ecu_name] = ecu_counts.get(ecu_name, 0) + 1

distribution_df = pd.DataFrame(
    list(ecu_counts.items()),
    columns=["ECU", "Messages"]
)

if not distribution_df.empty:
    plt.figure(figsize=(8, 5))
    plt.bar(
        distribution_df["ECU"],
        distribution_df["Messages"]
    )

    plt.title("CAN Messages by ECU")
    plt.xlabel("ECU")
    plt.ylabel("Message Count")
    plt.tight_layout()

    distribution_chart = os.path.join(
        OUTPUT_DIR,
        "ecu_distribution.png"
    )

    plt.savefig(distribution_chart)
    plt.close()

    print(f"Saved {distribution_chart}")

# -------------------------
# SUMMARY STATISTICS
# -------------------------

print("\n===== SUMMARY =====")

print(f"Total Messages: {len(records)}")

for ecu, count in ecu_counts.items():
    print(f"{ecu}: {count}")

if not rpm_df.empty:
    print(
        f"RPM Range: "
        f"{rpm_df['rpm'].min()} - "
        f"{rpm_df['rpm'].max()}"
    )

if not speed_df.empty:
    print(
        f"Speed Range: "
        f"{speed_df['speed_kmh'].min()} - "
        f"{speed_df['speed_kmh'].max()} km/h"
    )

print("\nAnalysis complete.")
