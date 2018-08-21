# coding:utf-8
# 使用python2进行编译，python3没有下面的模块
try:
    import cPickle
except Exception,e:
    import Pickle

import hashlib

class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt') # 未爬取URL的集合
        self.old_urls = self.load_progress('old_urls.txt') # 已爬取URL的集合
    
    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        '''
        return self.new_url_size()!=0
    def get_new_url(self):
        '''
        获取一个未爬取的URL
        '''
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url
    def add_new_url(self, url):
        '''
        将新的URL添加到为爬去的URL集合中
        '''
        if url is None:
            return 
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        将新的URL添加到未爬取的URL集合中
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        获取未爬取的URL集合的大小
        '''
        return len(self.new_urls)
    def old_url_size(self):
        '''
        获取已经爬取URL集合的大小
        '''
        return len(self.old_urls)
    def save_progress(self, path, data):
        '''
        保存进度
        '''
        with open(path, 'wb') as f:
            cPickle.dump(data, f)

    def load_progress(self, path):
        '''
        从本地加载进度
        '''
        print('从文件加载进度: %s' % path)
        try:
            with open(path, 'rb') as f:
                tmp = cPickle.load(f)
                return tmp
        except Exception:
            print('无法从本地加载文件 %s' % path)
        return set()

# 分布式爬虫的url管理器。和之前不同的是：将爬取过的url进行MD5处理
# 处理后的信息长度为128位  python中生成是256位，取中间128位
# 添加save_progress和load_progress方法进行序列化操作

