#!/usr/bin/env python3
import socket, sys, threading

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
port = int(sys.argv[2]) if len(sys.argv) > 2 else 9000

def reader(s):
    while data := s.recv(1024):
        print(data.decode(errors="replace"), end="")
    print("\n[disconnected]")

with socket.create_connection((host, port)) as s:
    threading.Thread(target=reader, args=(s,), daemon=True).start()
    try:
        for line in sys.stdin:
            s.sendall(line.encode())
    except KeyboardInterrupt:
        pass
