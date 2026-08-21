from scapy.all import sniff, wrpcap, IP, TCP, UDP
import sys
import os

packets = []

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "OTHER"
        
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
            
        print(f"[+] [{protocol}] {src_ip} ---> {dst_ip}")
        packets.append(packet)

def main():
    print("[*] Starting Packet Sniffer... Capturing 20 packets.")
    print("[*] Press Ctrl+C to stop early.\n")
    
    try:
        # Sniff 20 packets on active interface
        sniff(iface="lo", prn=packet_callback, count=20, timeout=30)
    except KeyboardInterrupt:
        print("\n[*] Stopping capture...")

    output_dir = "../pcaps"
    os.makedirs(output_dir, exist_ok=True)
    pcap_path = os.path.join(output_dir, "capture.pcap")

    if packets:
        wrpcap(pcap_path, packets)
        print(f"\n[+] Successfully saved {len(packets)} packets to {pcap_path}")
    else:
        print("\n[-] No packets captured.")

if __name__ == "__main__":
    main()
