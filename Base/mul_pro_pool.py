# 批量创建进程 p.join在之前有写作用
# 进程池 Pool


from multiprocessing import Pool
import os, time, random

def run_task(name):
    print('Task %s pid=%s id running ...' %(name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)

print('current process %s.' % os.getpid())
p = Pool(processes=3)
for i in range(5):
    p.apply_async(run_task, args=(i,))
print('Waiting for all subprocess done ...')
p.close()
p.join()
print('All subprocess done.')



# 首先创建容量为3的进程池， 向进程池添加5个任务，从结果可以看出
# 一开始只运行了3个，最多会运行3个进程，一个任务结束了，新的任务
# 才回添加进来, 结果如下：
# current process 7372.
# Waiting for all subprocess done ...
# Task 0 pid=7374 id running ...
# Task 1 pid=7375 id running ...
# Task 2 pid=7373 id running ...
# Task 2 end.
# Task 3 pid=7373 id running ...
# Task 1 end.
# Task 4 pid=7375 id running ...
# Task 3 end.
# Task 0 end.
# Task 4 end.
# All subprocess done.
