#coding:utf-8
import time
from src.dataSave import DataOutput

def store_Proc(self, store_q):
    output = DataOutput()
    while True:
        if not store_q.empty():
            data = store_q.get()
            if data == 'end':
                print('存储进程接受通知然后结束')
                output.out_put_html()
                return
            output.store_data(data)
        else:
            time.sleep(0.1)
