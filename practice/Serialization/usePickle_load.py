# coding:utf-8
import pickle

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def show(self):
        print(self.name + "_" +str(self.age))

f = open('./harry_info.txt', 'rb')
bb = pickle.load(f) # load时候需要把类定义包含进来，如果找不到类定义，加载就会失败
f.close()
bb.show()
