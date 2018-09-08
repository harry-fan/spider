from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFFSIZE = 1024
ADDR=(HOST, PORT)
#print(ADDR)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
print(tcpSerSock)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connecting")
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connect from ', addr)
    while True:
        data = tcpCliSock.recv(BUFFSIZE).decode()
        if not data:
            break
        tcpCliSock.send(('[%s] %s' %(ctime(), data)).encode())
    tcpCliSock.close()
    print(tcpCliSock)
tcpSerSock.close()

