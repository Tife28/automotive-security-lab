# System Architecture

This lab simulates a simplified in-vehicle network environment.

## Components

- ECU Simulator: Generates vehicle signals (speed, RPM, door status)
- CAN Bus: Communication medium for all ECUs
- Attacker Module: Simulates CAN injection and spoofing attacks
- Defender Module: Detects anomalies in CAN traffic
- Logger: Records all CAN messages for analysis

## Flow

ECUs → CAN Bus → Logger/Analyzer → Security Modules
