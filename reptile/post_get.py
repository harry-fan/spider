#!/usr/bin/python2.7
# coding:utf-8

# GET类型
import urllib2
# 请求
request = urllib2.Request('http://www.zhihu.com')
# 相应
response = urllib2.urlopen(request)
html = response.read()


# POST类型
import urllib
import urllib2

url = 'http://www.zhihu.com'
postdata = {'username':'harry', 'password':'harry123'}
data = urllib.urlencode(postdata) # 转换格式
req = urllib2.Request(url, data)  # 请求，传入参数
response = urllib2.urlopen(req)
html = response.read()
