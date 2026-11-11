#!/usr/bin/env python3
"""Tiny file transfer. Receive: file_transfer.py recv OUT ; Send: file_transfer.py send HOST FILE"""
import socket, sys, os
PORT = 9002
if sys.argv[1] == "recv":
    with socket.socket() as s:
        s.bind(("0.0.0.0", PORT)); s.listen(1)
        conn, a = s.accept()
        with conn, open(os.path.basename(sys.argv[2]), "wb") as f:
            while chunk := conn.recv(65536): f.write(chunk)
        print("received from", a)
else:
    with socket.create_connection((sys.argv[2], PORT)) as s, open(sys.argv[3], "rb") as f:
        while chunk := f.read(65536): s.sendall(chunk)
