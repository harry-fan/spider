# coding:utf-8
# 导入自定义的模块，需要在对应目录下加__init__.py文件

from src.UrlManager import UrlManager 
import time


def url_manager_proc(self, url_q, conn_q, root_url):
    url_manager = UrlManager()
    url_manager.add_new_url(root_url)
    while True:
        while(url_manager.has_new_url()):
            # 从URL管理器获取新的URL
            new_url = url_manager.get_new_url()
            # 将新的URL发给工作节点
            url_q.put(new_url)
            print('old_url=',url_manager.old_url_size())
            # 加判断条件，爬取2000个链接后关闭
            if(url_manager.old_url_size()>2000):
                url_q.put('end')
                print('控制节点发起结束通知')
                url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                return
        # 将resutl_solve_proc获取到的url添加到URL管理器
        try:
            if not conn_q.empty():
                urls = conn_q.get()
                url_manager.add_new_urls(urls)
        except BaseException:
            time.sleep(0.1) # 延时休息
