# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:11:10 2026

@author: admin
"""

from socket import *
from time import ctime
host=''
port=12345
address=(host,port)
bufsize=1024
u=socket(AF_INET,SOCK_DGRAM)
u.bind(address)
while True:
    print("waiting formessage")
    data,addr=u.recvfrom(bufsize)
    u.sendto(ctime().encode(),addr)
    print("received from and send to",addr)
u.close()
