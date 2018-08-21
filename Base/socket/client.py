# coding:utf-8

import socket
# 连接目标的IP和Port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

# 接收消息
print('---> ' + s.recv(1024).decode('utf-8'))
# 发送消息
s.send(b'Hello, I am client!')
print('---> ' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
# 关闭socket
s.close()
