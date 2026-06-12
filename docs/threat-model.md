# Threat Model

## Assets
- CAN bus communication
- ECU messages
- Vehicle control signals

## Threats
- CAN message injection
- Replay attacks
- Spoofing ECU identity
- Denial of Service (bus flooding)

## Attack Scenarios

### 1. Speed spoofing
Attacker sends fake speed data to override real ECU values.

### 2. Door unlock injection
Unauthorized CAN message unlocks vehicle doors.

### 3. Bus flooding
Attacker overwhelms CAN network causing disruption.

## Mitigations (future work)
- Message authentication
- IDS anomaly detection
- Secure ECU firmware
