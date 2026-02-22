# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:14:58 2026

@author: admin
"""

import socket
import os

SERVER_IP = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = "sample.txt"

# Send file name
sock.sendto(filename.encode(), (SERVER_IP, PORT))

# Send file data
with open(filename, "rb") as f:
    while True:
        data = f.read(BUFFER_SIZE)
        if not data:
            break
        sock.sendto(data, (SERVER_IP, PORT))

# Send EOF marker
sock.sendto(b"EOF", (SERVER_IP, PORT))

print("File sent successfully")
sock.close()
