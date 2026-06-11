#!/usr/bin/env python3
"""Send a UDP stop signal to the running GR00T motion controller."""

import socket
import sys

HOST = "127.0.0.1"
PORT = 9876

def send_stop(message: str = "STOP", host: str = HOST, port: int = PORT) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(message.encode(), (host, port))
    print(f"Sent '{message}' to {host}:{port}")

if __name__ == "__main__":
    msg  = sys.argv[1] if len(sys.argv) > 1 else "STOP"
    host = sys.argv[2] if len(sys.argv) > 2 else HOST
    port = int(sys.argv[3]) if len(sys.argv) > 3 else PORT
    send_stop(msg, host, port)
