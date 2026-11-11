#!/usr/bin/env python3
"""Tiny file transfer. Receive: file_transfer.py recv OUT ; Send: file_transfer.py send HOST FILE"""
import socket, sys, os

PORT = 9002

if len(sys.argv) < 3 or sys.argv[1] not in ("recv", "send"):
    print("Usage:\n  Receive: python3 file_transfer.py recv <output_file>\n  Send:    python3 file_transfer.py send <host> <input_file>")
    sys.exit(1)

if sys.argv[1] == "recv":
    with socket.socket() as s:
        s.bind(("0.0.0.0", PORT)); s.listen(1)
        print(f"[*] Listening for incoming file transfer on port {PORT}...")
        conn, a = s.accept()
        out_filename = os.path.basename(sys.argv[2])
        with conn, open(out_filename, "wb") as f:
            while chunk := conn.recv(65536): f.write(chunk)
        print(f"[+] Successfully received file '{out_filename}' from {a}")
else:
    if len(sys.argv) < 4:
        print("Usage for send: python3 file_transfer.py send <host> <input_file>")
        sys.exit(1)
    target_host = sys.argv[2]
    source_file = sys.argv[3]
    if not os.path.exists(source_file):
        print(f"[-] Error: Source file '{source_file}' does not exist.")
        sys.exit(1)
    with socket.create_connection((target_host, PORT)) as s, open(source_file, "rb") as f:
        print(f"[*] Sending '{source_file}' to {target_host}:{PORT}...")
        while chunk := f.read(65536): s.sendall(chunk)
    print("[+] File transmission complete.")
