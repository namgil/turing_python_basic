from socket import *
from threading import Thread
import os, sys




BUF_SIZE = 1024

while True:
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8080))
    data = input(">>")
    clientSock.sendall(data.encode())
    if(data == "bye"):
        clientSock.close()
        break
    res = clientSock.recv(1024)
    print(res.decode())

#함수화 시키기

