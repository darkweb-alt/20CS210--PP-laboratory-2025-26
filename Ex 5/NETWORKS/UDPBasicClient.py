from socket import *
from time import ctime
host='127.0.0.1'
port=12345
address=(host,port)
bufsize=1024
z=socket(AF_INET,SOCK_DGRAM)
while True:
    data="hello"
    data=data.encode()
    if not data:
        break
    z.sendto(data,address)
    data,address=z.recvfrom(bufsize)
    if not data:
        break
    print(data)
    break
z.close()
