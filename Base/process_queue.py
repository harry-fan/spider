# Queue 多进程之间的通信
# Pipe 两个进程间的通信

# 下面的例子：两个子进程往Queue中写数据，一个
# 子进程从Queue中读取数据

from multiprocessing import Process, Queue
import os, time, random

def proc_write(q, urls):
    print("Process %s is writing ..." % os.getpid())
    for url in urls:
        q.put(url)
        print('put %s to queue ...' % url)
        time.sleep(random.random())

def proc_read(q):
    print('Process %s is reading ...' % os.getpid())
    while True:
        url = q.get(True)
        print('get %s from queue.' % url)

q = Queue()
proc_write1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
proc_write2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
proc_reader = Process(target=proc_read, args=(q,))

# 启动子进程 proc_writer 写入
proc_write1.start()
proc_write2.start()
# 启动子进程 proc_reader 读取
proc_reader.start()

# 等待 proc_writer 结束：
proc_write1.join()
proc_write2.join()

# proc_reader 进程是死循环，无法等待结束，只能强行终止
proc_reader.terminate()


# Result:
# Process 7470 is writing ...
# Process 7472 is reading ...
# Process 7471 is writing ...
# put url_4 to queue ...
# get url_4 from queue.
# put url_1 to queue ...
# get url_1 from queue.
# put url_5 to queue ...
# get url_5 from queue.
# put url_2 to queue ...
# get url_2 from queue.
# put url_3 to queue ...
# get url_3 from queue.
# put url_6 to queue ...
# get url_6 from queue.
