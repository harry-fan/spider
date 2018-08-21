# 线程同步，保证数据的正确性

import threading

mylock = threading.RLock()
num = 0

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print("%s locked, number: %d" %(threading.current_thread().name, num))
            if num>=4:
                mylock.release()
                print("%s release, number: %d" %(threading.current_thread().name, num))
                break
            num += 1
            print("%s released, number: %d" %(threading.current_thread().name, num))
            mylock.release()

thread1 = myThread('Thread_1')
thread2 = myThread('Thread_2')
thread1.start()
thread2.start()

