#!/usr/bin/env python3
"""Minimal multi-client TCP chat server."""
import socket, threading

HOST, PORT = "0.0.0.0", 9000
clients, lock = [], threading.Lock()

def broadcast(msg, sender):
    with lock:
        for c in clients[:]:
            if c is not sender:
                try: c.sendall(msg)
                except OSError: clients.remove(c)

def handle(conn, addr):
    with lock: clients.append(conn)
    print(f"[+] {addr}")
    try:
        while data := conn.recv(1024):
            broadcast(f"{addr[0]}: ".encode() + data, conn)
    finally:
        with lock:
            if conn in clients: clients.remove(conn)
        conn.close(); print(f"[-] {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT)); s.listen()
        print(f"Chat server on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
