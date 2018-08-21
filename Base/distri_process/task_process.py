#!/usr/bin/python2.7
# coding:utf-8

import time
from multiprocessing.managers import BaseManager

# 创建Queuemanager
class Queuemanager(BaseManager):
    pass

# 第一步：使用Queuemanager注册获取queue的方法名称
Queuemanager.register('get_task_queue')
Queuemanager.register('get_result_queue')

# 第二步：链接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s ... ' % server_addr)

# 端口验证口令必须和服务进程一致
m = Queuemanager(address=(server_addr, 8001), authkey='qiye')

# 从网络连接
m.connect()
# 第三步：获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

# 第四步：从task队列获取任务，把结果写入result队列
while(not task.empty()):
    image_url = task.get(True, timeout=5)
    print('run task download %s ...' % image_url)
    time.sleep(1)
    result.put('%s ---->>> SUCESS' % image_url)

print('worker exit.')
