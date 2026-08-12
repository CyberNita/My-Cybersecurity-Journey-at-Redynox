import socket
import concurrent.futures
import sys
from datetime import datetime

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((ip, port))
            if result == 0:
                return port, True
    except Exception:
        pass
    return port, False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    print(f"[*] Starting scan on target: {target_ip}")
    print(f"[*] Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in range(1, 8081)]
        for future in concurrent.futures.as_completed(futures):
            port, is_open = future.result()
            if is_open:
                print(f"[+] Port {port:<5} is OPEN")

if __name__ == "__main__":
    main()
