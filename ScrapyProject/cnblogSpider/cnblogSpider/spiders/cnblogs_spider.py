# coding:utf-8

import scrapy

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs" # 爬虫名
    allowed_domains = ["cnblogs.com"] # 域名
    start_urls = [
            "http://www.cnblogs.com/qiyeboy/default.html?page=1"
            ]
    def parse(self, response):
        # 实现解析
        pass

