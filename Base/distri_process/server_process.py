#!/usr/bin/python2.7
#coding:utf-8

import random,time,Queue
from multiprocessing.managers import BaseManager

# 第一步：建立task_queue和result_queue，存放任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()

class Queuemanager(BaseManager):
    pass

# 第二步：把创建的两个队列注册在网络上，利用register方法
# callable 参数关联了Queue 对象
# 将Queue 暴漏在网络中
Queuemanager.register('get_task_queue', callable=lambda:task_queue)
Queuemanager.register('get_result_queue', callable=lambda:result_queue)

# 第三步：绑定端口号8001 设置验证口令'qiye' 对象初始化
manager = Queuemanager(address=('', 8001), authkey='qiye')

# 第四步：启动管理监听通道
manager.start()

# 第五步：通过管道实例的方法获得通过网络访问的Queue 对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 第六步： 添加任务
for url in ["ImageUrl_"+str(i) for i in range(10)]:
    print('put task %s ...' % url)
    task.put(url)

while True:
    print('waiting over')
    time.sleep(15)
    print('run over')
    break
#获取返回结果
print('try to get result ...')
for i in range(10):
    print("result is %s ." % result.get(timeout=10))

#关闭管理
manager.shutdown()
