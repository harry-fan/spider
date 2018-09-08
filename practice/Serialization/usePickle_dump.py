# pickle提供简单的持久化功能，可以将对象以文件的形式存放在磁盘

import pickle

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def show(self):
        print(self.name + "_" +str(self.age))

aa = Person("harry", 24)
aa.show()
f = open('./harry_info.txt', 'wb') # 此处必须是wb，pickle存储是二进制，没有b属性，就会报错
pickle.dump(aa, f)
f.close()
