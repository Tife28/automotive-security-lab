#!/bin/bash

echo "====================================="
echo " Setting up Virtual CAN Interface"
echo "====================================="

# Load the vcan kernel module
sudo modprobe vcan

# Remove old interface if it exists
sudo ip link delete vcan0 2>/dev/null

# Create a new virtual CAN interface
sudo ip link add dev vcan0 type vcan

# Bring it up
sudo ip link set up vcan0

echo
echo "Virtual CAN interface created."
echo

ip -details link show vcan0