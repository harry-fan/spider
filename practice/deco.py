

import time

def deco(func):
    print('xxxxxxxxxxxxxx')
    def wrapper():
        print("++++++++++")
        starttime = time.time()
        func()
        endtime = time.time()
        print('mmmmmmmmmmmmmmmm')
        msecs = (endtime - starttime)*1000
        print('time us %s ms' % msecs)
    return wrapper

@deco
def func():
    print("=============")
    print('hello')
    time.sleep(1)
    print('world')

if __name__ == '__main__':
    f = func
    f()
