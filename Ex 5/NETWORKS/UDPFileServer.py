# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:14:28 2026

@author: admin
"""

import socket

SERVER_IP = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print("UDP Server waiting for file...")

# Receive file name
filename, client_addr = sock.recvfrom(BUFFER_SIZE)
filename = filename.decode()

print("Receiving file:", filename)

with open("received_" + filename, "wb") as f:
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        if data == b"EOF":
            break
        f.write(data)

print("File received successfully")
sock.close()
