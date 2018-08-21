import ctypes
import datetime
import random
import os
import time

from multiprocessing import Queue
from multiprocessing.pool import Pool

from multiprocessing import Value

# 该段程序作用是测试，
# 容量为9个进程的进程池同时运行30个进程所需要的时间
# 三个容量为3个进程的进程池同时运行30个进程所需要的时间
# 结果： 容量为9个进程的进程池占优，耗费时间更短一些。

class entry(object):
    def __init__(self, s: str, queue: Queue):
        self.s = s
        # self.queue = queue
        # self.counter = c_uint

    def cutString(self):
        index = random.randint(0, len(self.s) - 4)
        time.sleep(1)
        i = random.randint(0, 2)
        print("randint(0, 2) = {}".format(i), index)
        return self.s[index:index + 2]

    def exec(self):
        # self.counter.value += 1
        substring = self.cutString()
        # 往队列里放数据
        # self.queue.put(substring)
        return substring

    # 回调函数
    def display(self, s):
        global index # 此时的index不是class对象中的index，而是全局变量index初始值是1
        index += 1
        print("callback ----> {}:{}".format(index-1, s))


if __name__ == '__main__':
    param = "0123456789abcdefghijklmnopqrstuvwxyz"
    val = Value(ctypes.c_uint32, 1)
    # print('val type======================> ', type(val))
    # exit()
    index = 1
    queue = Queue()

    # 测试9个进程的进程池执行 doMatch() 函数30次需要的时间
    pool1 = Pool(9)
    start = datetime.datetime.now()
    for i in range(30):
        e = entry(param, queue)
        pool1.apply_async(e.exec, callback=e.display) #e.exec的返回值会传递给callback的函数作为参数

    pool1.close()
    pool1.join()
    finish = datetime.datetime.now()
    # tmp = []
    # while not queue.empty():
    #     tmp.append(queue.get())
    # print("9个进程的进程池执行结果:\n{}".format(tmp))
    print("9个进程的进程池执行花费的时间为：\t{}".format(finish - start))
    # 最多进程池中同时有9个进程在跑, 测试总共跑30个进程

    # 测试3组3个进程的进程池执行 doMatch() 函数30次需要的时间
    pool2 = Pool(3)
    pool3 = Pool(3)
    pool4 = Pool(3)
    pools = [pool2, pool3, pool4]
    index = 1

    start = datetime.datetime.now()
    for j in range(len(pools)):
        for i in range(10):
            e = entry(param, queue)
            pools[j].apply_async(e.exec, callback=e.display)

        pools[j].close()
    for j in range(len(pools)):
        pools[j].join()
    finish = datetime.datetime.now()
    print("3组3个进程的进程池执行花费的时间为：\t{}".format(finish - start))
    # tmp = []
    # while not queue.empty():
    #     tmp.append(queue.get())
    # print("3组3个进程的进程池执行结果：\n{}".format(tmp))
