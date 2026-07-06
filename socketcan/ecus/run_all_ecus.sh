#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

"$SCRIPT_DIR/engine_ecu.sh" &
ENGINE_PID=$!

"$SCRIPT_DIR/speed_ecu.sh" &
SPEED_PID=$!

"$SCRIPT_DIR/body_ecu.sh" &
BODY_PID=$!

echo
echo "ECUs running..."
echo

echo "Engine PID : $ENGINE_PID"
echo "Speed PID  : $SPEED_PID"
echo "Body PID   : $BODY_PID"

wait