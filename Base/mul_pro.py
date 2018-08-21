# 使用 Process 创建进程
# 不局限于应用系统，linux和unix均可以使用


import os
from multiprocessing import Process

def run_proc(name):
    print('child process %s %s Runing ...' %(name, os.getpid()))

print("Parent process %s" % os.getpid())
for i in range(3):
    p = Process(target=run_proc, args=(str(i)))
    print('process will start ...')
    p.start()
p.join() 
print("Process end.")

# p.join() 函数解释：等待进程结束
# 如果不加 join 那么不会等待进程结束，直接执行接下来的进程 
