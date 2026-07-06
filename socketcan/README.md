readme.md

# SocketCAN Environment

This directory contains scripts for creating and testing a Linux Virtual CAN (vCAN) environment.

## To clone this branch use the command below
git clone --branch socketcan-lab --single-branch https://github.com/Tife28/automotive-security-lab.git

## Requirements

- Linux
- can-utils
- iproute2

## Make executable:

chmod +x socketcan/cleanup_vcan.sh
chmod +x socketcan/setup_vcan.sh
chmod +x socketcan/verify.sh

## Setup

```bash
./setup_vcan.sh

## Verify

```bash
./verify.sh

## Remove Interface

```bash
./cleanup_vcan.sh