# MiniScan

A simple TCP port scanner built in Python as a learning project.

## Description

MiniScan is a basic port scanner that checks if TCP ports are open on a target host. It demonstrates fundamental Python concepts including functions, error handling, and network programming.

## Features

- Scan single ports or multiple ports (comma-separated)
- Validates port numbers (1-65535)  
- Identifies secure vs system ports
- Clean output showing open/closed status
- Built using only Python standard library (no external dependencies)

## Usage

```bash
python miniscan.py

When prompted:
1. Enter the target host (e.g., `google.com` or `192.168.1.1`)
2. Enter ports to scan (e.g., `80` or `22,80,443`)

## Example Output
```
Enter the host: google.com
Enter the ports: 80,443,22

Scanning google.com...
Port 80: OPEN
Port 443: OPEN
Port 22: CLOSED
```


## Author

Built as a learning project to understand Python fundamentals and basic networking concepts.
