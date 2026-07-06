#!/bin/bash

echo "Removing virtual CAN interface..."

sudo ip link delete vcan0

echo "Done."