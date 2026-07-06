# SocketCAN Analysis Report

## Capture Summary

| Metric | Value |
|---------|------:|
| Total CAN Frames | 249 |
| Engine ECU Frames | 118 |
| Speed ECU Frames | 116 |
| Body ECU Frames | 15 |

## Intrusion Detection Results

| Detection | Count |
|-----------|------:|
| RPM Anomalies | 44 |
| Speed Anomalies | 45 |

## Generated Artifacts

- socketcan_rpm_chart.png
- socketcan_speed_chart.png
- socketcan_ecu_distribution.png

## Notes

This analysis was generated from captured SocketCAN traffic on the virtual CAN interface (`vcan0`).

The analyzer decoded CAN frames according to the project CAN message specification and applied rule-based intrusion detection using the following thresholds:

- RPM > 6500
- Speed > 180 km/h
