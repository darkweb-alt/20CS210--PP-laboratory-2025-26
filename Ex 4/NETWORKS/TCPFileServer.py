# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:04:12 2026

@author: admin
"""

import socket                   # Import socket module
port = 12345                   # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = '0.0.0.0'   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', data)

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',l)
       l = f.read(1024)
    f.close()
    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()
