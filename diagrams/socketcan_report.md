# SocketCAN Analysis Report

## Capture Summary

| Metric | Value |
|---------|------:|
| Total CAN Frames | 651 |
| Engine ECU Frames | 303 |
| Speed ECU Frames | 308 |
| Body ECU Frames | 40 |

## Intrusion Detection Results

| Detection | Count |
|-----------|------:|
| RPM Anomalies | 125 |
| Speed Anomalies | 125 |

## Generated Artifacts

- socketcan_rpm_chart.png
- socketcan_speed_chart.png
- socketcan_ecu_distribution.png

## Notes

This analysis was generated from captured SocketCAN traffic on the virtual CAN interface (`vcan0`).

The analyzer decoded CAN frames according to the project CAN message specification and applied rule-based intrusion detection using the following thresholds:

- RPM > 6500
- Speed > 180 km/h
