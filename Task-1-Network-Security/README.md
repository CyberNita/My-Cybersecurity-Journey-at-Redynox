# Task 01: Network Security & Packet Analysis

## Overview
This module explores basic network auditing by combining active host probing with passive packet inspection. It features a custom Python TCP port scanner and a Scapy-based packet sniffer run on Kali Linux.

## Directory Layout
- `scripts/scanner.py`: Multi-threaded Python TCP port scanner using the standard `socket` library.
- `scripts/sniffer.py`: Passive packet sniffer using `scapy` to capture raw network traffic.
- `pcaps/capture.pcap`: Saved packet capture file containing captured scan traffic.

## Execution Steps

### 1. Active Port Scanning
Run the scanner against a local target or loopback address:
```bash
python3 scripts/scanner.py 127.0.0.1
