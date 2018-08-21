#!/usr/bin/python2.7
#coding:utf-8

import requests

# 文件名不要用requests作为名字，import出错
# requests库是目前最好用的爬虫库之一，.get就可以获取连接
r = requests.get('http://www.baidu.com',)
print(r.content)

postdata = {'key':'value'}
r = requests.get('http://xxx', data=postdata)
print(r.content)
