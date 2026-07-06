#!/bin/bash

echo "Stopping Automotive Security Lab..."

for file in pids/*.pid
do
    [ -f "$file" ] || continue

    PID=$(cat "$file")

    kill "$PID" 2>/dev/null
done

rm -rf pids

./socketcan/cleanup_vcan.sh

echo
echo "Lab stopped."