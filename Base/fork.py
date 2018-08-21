# fork 创建进程
# 两个返回值 等于0是子进程
# 大于0是 父进程


import os

print('current process %s start ...'% os.getpid())
pid = os.fork()
# print(pid) 返回值不同时进行,两个进程之间不同时刻
if pid < 0:
    print("error in fork")
elif pid == 0:
    print("I %s am child process  and my parent process is %s" % (os.getpid(), os.getppid()))
else:
    print("I %s created a child proces %s " % (os.getpid(), pid))

print("over======================")

