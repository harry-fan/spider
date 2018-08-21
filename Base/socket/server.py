import socket
import threading
import time

def deal_client(sock, addr):
    # 第四步：接收传来的数据，并发送给对方
    print("Accept new connect from %s:%s..." % addr)
    sock.send(b'Hello!, I am server!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print("----> %s!" % data.decode('utf-8'))
        sock.send(('Loop_Msg: %s!' %data.decode('utf-8')).encode('utf-8'))

    # 第五步：关闭socket
    sock.close()
    print('Connection from %s:%s close.' % addr)

if __name__ == '__main__':
    # 第一步：创建一个IPv4和Tcp协议的socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # 第二步：监听链接
    s.listen(5)
    print('Waiting for connect ... ')
    while True:
        # 第三步：接收新的连接
        sock, addr = s.accept()
        # 创建新的线程处理TCP连接
        t = threading.Thread(target=deal_client, args=(sock, addr))
        t.start()
