# Task 1: Network Security & Port Scanning Assessment

## Overview
This module demonstrates hands-on network reconnaissance using custom Python socket programming to identify open ports and active services on a target system.

## Project Structure
- `scripts/scanner.py`: Multi-threaded Python TCP port scanner.
- `screenshots/`: Terminal execution evidence showing detected listening ports.
- `pcaps/`: Directory reserved for network packet captures.

## Usage
To scan a target IP address:
```bash
python3 scripts/scanner.py <target_ip>
