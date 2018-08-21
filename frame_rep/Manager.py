#coding:utf-8
from multiprocessing.managers import BaseManager

# 分布式管理器
def start_Manager(self, url_q, result_q):
    '''
    创建一个分布式管理器
    url_q: 管理进程将URL传递给爬虫节点的通道
    result_q: 爬虫节点将数据返回给数据提取进程的通道
    '''
    # 把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
    # 将Queue对象在网络中暴漏
    BaseManager.register('get_task_queue', callable=lambda:url_q)
    BaseManager.register('get_result_queue', callable=lambda:result_q)
    # 绑定端口号 8001 设置验证口令，baike 相当于对象初始化
    manager = BaseManager(address=('', 8001), authkey='baike')
    # 返回manager对象
    return manager
