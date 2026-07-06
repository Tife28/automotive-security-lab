#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

"$SCRIPT_DIR/rpm_spoof.sh" &
RPM_PID=$!

"$SCRIPT_DIR/speed_spoof.sh" &
SPEED_PID=$!

echo
echo "Attack modules running..."
echo

echo "RPM Attack PID   : $RPM_PID"
echo "Speed Attack PID : $SPEED_PID"

wait