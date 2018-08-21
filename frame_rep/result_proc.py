# coding:utf-8
import time


def result_solve_proc(self, result_q, conn_q, store_q):
    while(True):
        try:
            if not result_q.empty():
                content = result_q.get(True)
                if content['new_urls']== 'end':
                    print('结果分析进程接受通知然后结束')
                    store_q.put('end')
                    return
                conn_q.put(content['new_urls']) # url为set类型
                store_q.put(content['data']) # 解析出来的数据为dict类型
            else:
                time.sleep(0.1)
        except BaseException:
            time.sleep(0.1)
