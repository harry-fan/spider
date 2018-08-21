# 通过类继承方式创建线程

import random
import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print("current %s is running ..." % threading.current_thread().name)
        for url in self.urls:
            print("%s ---->>>> %s" % (threading.current_thread().name, url))
            time.sleep(random.random())
        print("%s is ended." % threading.current_thread().name)

print("%s is running ..." % threading.current_thread().name)
t1 = myThread(name="Thread_1", urls=['url_1', 'url_2', 'url_3']) 
t2 = myThread(name="Thread_2", urls=['url_4', 'url_5', 'url_6']) 

t1.start()
t2.start()

t1.join()
t2.join()
print("%s ended." % threading.current_thread().name)

# Result
# MainThread is running ...
# current Thread_1 is running ...
# Thread_1 ---->>>> url_1
# current Thread_2 is running ...
# Thread_2 ---->>>> url_4
# Thread_2 ---->>>> url_5
# Thread_2 ---->>>> url_6
# Thread_2 is ended.
# Thread_1 ---->>>> url_2
# Thread_1 ---->>>> url_3
# Thread_1 is ended.
# MainThread ended.
