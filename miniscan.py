#!/usr/bin/env python3
"""

Mini TCP port scanner (educational)


Sequential (no threads), text output only
Applies: "secure" if port>1024
Only scan systems you own or have explicit permission to test

"""

import argparse
import socket
from typing import Iterable, List

Default_ports = [1025,80, 443, 22, 25, 3389, 1433, 1521, 3306, 5432, 5900,]
Default_timeout = 0.5

def is_port_secure(port: int) -> bool:
    return port > 1024

def validate_port(p: int) -> int:
    if not (1<= p <= 65535):
        raise argparse.ArgumentTypeError(f"Port {p} is out of range (1-65535).")
    return p

def parse_port_list(port_list: str) -> List[int]:
    parts = [x.strip() for x in port_list.split(",") if x.strip()]
    # Split on commas, remove empty parts

    # Convert to integers and validate
    ports = []
    for part in parts:
        try:
            port = int(part)
            if validate_port(port):
                ports.append(port)
        except ValueError:
            pass # Ignore invalid ports

    return ports

def is_open(host: str, port: int, timeout: float = Default_timeout) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True # Port is open
    except Exception:
        return False
        # Port is closed or filtered

def scan(host: str, ports: Iterable[int], timeout: float = Default_timeout):
    # Dedupe and sort for tidy output
    unique_ports = sorted({int(p) for p in ports})
    results = []
    for p in unique_ports:
        results.append(
            {
                "port": p,
                "open": is_open(host, p, timeout),
                "secure": is_port_secure(p)
            }
            ) 
    return results

def print_results(host: str, results: List[dict]) -> None:
    #Print each port result
    for r in results:
        port = r["port"]

        if r["open"]:
            status = "open"
        else:
            status = "closed"

        if r["secure"]:
            secure = "secure"
        else:
            secure = "not secure"

        print(f"{host}:{port} is {status} ({secure})")

    # Count statistics
        total_ports = len(results)
        open_ports = 0

        for r in results:
            if r["open"]:
                open_ports = open_ports + 1
            #open_ports += 1

        print(f"\nScanned {total_ports} ports")
        print(f"Found {open_ports} open ports")

def main():
    # Get input from user
    host = input("Enter hostname or IP to scan: ")
    ports_input = input("Enter ports to scan (comma-separated e.g., 80,443): ")

    # Parse the ports
    port_list = parse_port_list(ports_input)

    # Scan the ports
    print(f"Scanning {host}...")
    results = scan(host, port_list)

    # Print the results
    print_results(host, results)

#Run the program
if __name__ == "__main__":
    main()

    





         
    
    

     

      
      
      
  
  
  
