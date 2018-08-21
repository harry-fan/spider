# 创建线程

import random
import time, threading

def thread_run(urls):
    print("current %s is running ..." % threading.current_thread().name)
    for url in urls:
        print("%s ---->>>> %s" %(threading.current_thread().name, url))
        time.sleep(random.random())
    print("%s ended." % threading.current_thread().name)

print("%s is running ..." % threading.current_thread().name)
t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1','url_2','url_3'],))
t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4','url_5','url_6'],))
# 别忘记参数args的list后面的逗号,否则报错

t1.start()
t2.start()

t1.join()
t2.join()
print("%s ended." % threading.current_thread().name)

# MainThread is running ...
# current Thread_1 is running ...
# Thread_1 ---->>>> url_1
# current Thread_2 is running ...
# Thread_2 ---->>>> url_4
# Thread_1 ---->>>> url_2
# Thread_2 ---->>>> url_5
# Thread_1 ---->>>> url_3
# Thread_2 ---->>>> url_6
# Thread_1 ended.
# Thread_2 ended.
# MainThread ended.
