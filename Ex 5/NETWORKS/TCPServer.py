# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:00:26 2026

@author: admin
"""

from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime
import pprint
HOST = '127.0.0.1'
PORT = 2437
BUFSIZ = 1024
ADDR = (HOST, PORT)
class MyRequestHandler(SRH):
    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        print("{}".format(self.client_address))
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        data = str(data, 'utf-8')
        echo_data = "{} {}".format(ctime(), data)
        self.request.sendall(bytes(echo_data, 'utf-8'))
tcpServ = TCP(ADDR, MyRequestHandler)
tcpServ.allow_reuse_address = True
print("...waiting for connection")
tcpServ.serve_forever()
