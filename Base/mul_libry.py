# multiprocessing库的简单测试使用

from multiprocessing import Pool, Process, Value, Array, Manager

import time
import os


# 线程池Pool
def f(x):
    time.sleep(0.5)
    print(x)
    return x*x

# print(map(f,[1,2,3]))
# p = Pool(11)
# print(p.map(f,[1,2,3]))

#进程的内存共享
#def ff(n,a):
#    n.value = 888
#    print("current process is: ", os.getpid())
#    for i in range(10):
#        a[i] = -a[i]
#
#if __name__ == '__main__':
#    num = Value('d',0.0)
#    arr = Array('i', range(10))
#
#    print(num.value)
#    print(arr[:])
#    print("current process is: ", os.getpid())
#    # 不同的进程id，使用到的内存地址是一样的
#
#    p = Process(target=ff, args=(num, arr)) #
#    p.start()
#    p.join()
#    print(num.value)
#    print(arr[:])

# 进程的内存共享Manager
def fff(d, l):
    d['a'] = 888
    l[1] = 99999
    l.reverse()

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=fff, args=(d, l))
    p.start()
    p.join()
    print(d)
    print(l[:])
