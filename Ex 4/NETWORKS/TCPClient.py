# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 08:59:31 2026

@author: admin
"""

from socket import *
HOST = '127.0.0.1'
PORT = 2437
BUFSIZ = 1024
ADDR = (HOST, PORT)
while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, "utf-8"))
    #tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(str(data).strip())
    tcpCliSock.close()
    
    