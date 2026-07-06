#!/bin/bash

echo "Body ECU started..."

while true
do
    LOCK=$((RANDOM % 2))

    LOCK_HEX=$(printf "%02X" $LOCK)

    cansend vcan0 103#${LOCK_HEX}00000000000000

    sleep 1
done