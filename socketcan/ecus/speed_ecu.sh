#!/bin/bash

echo "Speed ECU started..."

while true
do
    SPEED=$((RANDOM % 181))

    SPEED_HEX=$(printf "%02X" $SPEED)

    cansend vcan0 102#${SPEED_HEX}00000000000000

    sleep 0.2
done