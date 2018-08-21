#!/usr/bin/python2.7
# coding:utf-8

# 把task任务进程分布到多台机器上，实现大规模的分布式爬虫

import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 任务数量
task_num = 10

# 定义收发队列
task_queue = Queue.Queue(task_num)
result_queue = Queue.Queue(task_num)

def get_result():
    return result_queue
def get_task():
    return task_queue

# 创建类似的Queuemanager
class Queuemanager(BaseManager):
    pass

def win_run():
    # windows下绑定调用接口不能使用lambda，只能先定义函数再绑定
    Queuemanager.register('get_task_queue', callable=get_task)
    Queuemanager.register('get_result_queue', callable=get_result)

    manager = Queuemanager(address=('127.0.0.1', 8001), authkey='qiye')
    # 启动
    manager.start()
    try:
        # 通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 添加任务
        for url in ["ImageUrl_"+str(i) for i in range(10)]:
            print('put task %s ...' %url)
            task.put(url)
        print('try get result ... ')
        for i in range(10):
            print("result is %s ." %result.get(timeout=10))
    except:
        print('manager error')
    finally:
        # 一定关闭，否则报管道未关闭的错误
        manager.shutdown()

if __name__ == '__main__':
    # windows 下多进程可能会有问题，添加如下可以缓解
    freeze_support()
    win_run()
