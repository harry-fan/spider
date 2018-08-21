# coding:utf-8
import time,Queue
from multiprocessing.managers import BaseManager
from Manager import start_Manager
from multiprocessing import Process
from url_proc import url_manager_proc
from result_proc import result_solve_proc
from store_proc import store_Proc

class NodeManager(BaseManager):
    def start_manager(self, url_q, result_q):
        start_Manager(self, url_q, result_q)

    def url_proc(self, url_q, conn_q, root_url):
        url_manager_proc(self, url_q, conn_q, root_url)

    def result_proc(self,result_q, conn_q, store_q):
        result_solve_proc(self, result_q, conn_q, store_q)

    def store_proc(self, store_q):
        store_Proc(self, store_q)

if __name__ == '__main__':
    # 初始化4个队列
    url_q = Queue.Queue()
    result_q = Queue.Queue()
    store_q = Queue.Queue()
    conn_q = Queue.Queue()
    #创建分布式管理器
    node = NodeManager()
    manager = node.start_manager(url_q, result_q)
    # 创建URl管理进程、数据提取进程、
    url_proc = Process(target=node.url_proc, args=(result_q, conn_q, 'http://baike.baidu.com/view/284853.html',))
    result_proc = Process(target=node.result_proc, args=(result_q, conn_q, store_q,))
    store_proc = Process(target=node.store_proc, args=(store_q,))
    url_proc.start()
    result_proc.start()
    store_proc.start()
