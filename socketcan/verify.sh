#!/bin/bash

echo "Checking SocketCAN environment..."
echo

echo -n "cangen: "
which cangen

echo -n "candump: "
which candump

echo -n "cansend: "
which cansend

echo

echo "Checking vcan interface..."

ip link show vcan0