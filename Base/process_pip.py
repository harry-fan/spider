# 管道通信
# duplex参数默认为True，此时为全双工，均可发送接收消息
# 如果为False， conn1负责接收，conn2负责发送
# 没有消息进入阻塞状态， 管道关闭recv方法抛出EOFError

import multiprocessing
import random
import time, os

def proc_send(pipe, urls):
    for url in urls:
        print("process %s send: %s" % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print("Process %s recv: %s" %(os.getpid(), pipe.recv()))
        time.sleep(random.random())

pipe = multiprocessing.Pipe()
p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(5)]))
p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))

p1.start()
p2.start()

p1.join()
p2.join()
p2.terminate() # 不能强行终止
