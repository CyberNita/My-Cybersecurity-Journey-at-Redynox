This report provides a high-level summary suitable for a portfolio or assignment submission.

```markdown
# Executive Summary Report: Task 01 - Network Security

**Author:** Anita Nwokem  
**Environment:** Kali Linux  
**Tools Used:** Python 3 (`socket`, `scapy`), Wireshark  

---

## 1. Objective
The goal of this task was to develop custom scripts for network auditing and analyze the resulting traffic using industry-standard tools.

## 2. Methodology
1. **Script Development:** Developed `scanner.py` to test TCP port availability and `sniffer.py` to capture active network packets.
2. **Traffic Capture:** Executed scans over loopback (`127.0.0.1`) while capturing packet streams into raw `.pcap` files.
3. **Packet Analysis:** Inspected TCP flags (`SYN`, `RST`) and protocol layers using Wireshark display filters and packet details panes.

## 3. Results
- Identified open vs. closed ports based on returned TCP responses.
- Successfully captured live traffic streams and verified header fields across Layer 2 (Ethernet), Layer 3 (IP), and Layer 4 (TCP).

## 4. Key Recommendations
- **Network Segmentation:** Isolate critical hosts to restrict unmonitored local traffic analysis.
- **Service Hardening:** Close unused ports and replace cleartext communication with encrypted protocols.
