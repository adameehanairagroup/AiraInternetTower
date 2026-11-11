#!/usr/bin/env python3
"""UDP echo server (run with 'server') or client (run with 'client HOST')."""
import socket, sys

PORT = 9001
if len(sys.argv) > 1 and sys.argv[1] == "client":
    host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(2)
        s.sendto(b"hello", (host, PORT))
        print(s.recvfrom(1024))
else:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", PORT)); print(f"UDP echo on {PORT}")
        while True:
            data, addr = s.recvfrom(1024); s.sendto(data, addr)
