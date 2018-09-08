

import time

def deco(func):
    print('xxxxxxxxxxxxxx')
    def wrapper(a, b): # 参数放这里
        print("++++++++++")
        starttime = time.time()
        func(a, b)
        endtime = time.time()
        print('mmmmmmmmmmmmmmmm')
        msecs = (endtime - starttime)*1000
        print('time us %s ms' % msecs)
    return wrapper

@deco
def func(a, b):
    print("=============")
    print('hello')
    time.sleep(1)
    print('world')
    print('result : %s' %(a+b))

if __name__ == '__main__':
    f = func
    f(3,4)
