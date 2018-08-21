# coding:utf-8

from dataSave import DataOutput 
from htmlDowloader import HtmlDownloader
from htmlParser import HtmlParser
from urlManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self, root_url):
        self.manager.add_new_url(root_url)

        while(self.manager.has_new_urls() and self.manager.old_url_size() < 100):
            #try:
            # 获取新的url
            new_url = self.manager.get_new_url()
            # 下载器下载网页
            html = self.downloader.download(new_url)
            # 解析器抽取网页数据
            new_urls, data = self.parser.parser(new_url, html)
            # 添加UR管理器
            self.manager.add_new_urls(new_urls)
            # 数据存储文件
            self.output.store_data(data)
            print("已经抓取 %s 个链接" % self.manager.old_url_size())
            #except Exception, e:
            #    print("crawl failded", e)
        self.output.out_put_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.html")
