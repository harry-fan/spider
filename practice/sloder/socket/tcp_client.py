from socket import  *

HOST = '127.0.0.1'
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    print('data = ', data)
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFFSIZE).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()
