#!/bin/bash

set -e

echo "========================================="
echo " Automotive Cybersecurity SocketCAN Lab"
echo "========================================="
echo

mkdir -p runtime_logs
mkdir -p pids

# Check dependencies
command -v cansend >/dev/null || {
    echo "ERROR: can-utils is not installed."
    exit 1
}

python3 -c "import can" >/dev/null 2>&1 || {
    echo "ERROR: python-can is not installed."
    echo "Run: pip install python-can"
    exit 1
}

echo "[1/4] Setting up vCAN..."
./socketcan/setup_vcan.sh

echo
echo "[2/4] Starting SocketCAN logger..."

python3 tools/socketcan_logger.py > runtime_logs/logger.log 2>&1 &
echo $! > pids/logger.pid

echo
echo "[3/4] Starting simulated ECUs..."

./socketcan/ecus/run_all_ecus.sh > runtime_logs/ecu.log 2>&1 &
echo $! > pids/ecu.pid

echo
echo "[4/4] Starting IDS..."

python3 tools/socketcan_ids.py > runtime_logs/ids.log 2>&1 &
echo $! > pids/ids.pid

echo
echo "========================================="
echo "Lab Started Successfully"
echo "========================================="
echo
echo "Live outputs:"
echo
echo "tail -f runtime_logs/logger.log"
echo "tail -f runtime_logs/ecu.log"
echo "tail -f runtime_logs/ids.log"
echo
echo "To launch attacks:"
echo
echo "./socketcan/attacks/run_attacks.sh"
echo
echo "To stop everything:"
echo
echo "./stop_lab.sh"
