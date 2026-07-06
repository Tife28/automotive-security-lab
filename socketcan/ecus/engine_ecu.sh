#!/bin/bash

echo "Engine ECU started..."

while true
do
    RPM=$((800 + RANDOM % 5201))     # 800–6000
    LOAD=$((10 + RANDOM % 81))       # 10–90%

    RPM_HEX=$(printf "%04X" $RPM)

    HIGH=${RPM_HEX:0:2}
    LOW=${RPM_HEX:2:2}

    LOAD_HEX=$(printf "%02X" $LOAD)

    cansend vcan0 101#${HIGH}${LOW}${LOAD_HEX}0000000000

    sleep 0.2
done