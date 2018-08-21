#!/usr/bin/python2.7
#coding:utf-8

import urllib
import urllib2

url = 'http://www.xxx.com/login'

user_agent = 'Mozilla/4.0 (compatile; MSIE 5.5; Windows NT)'
referer = 'http://www.xxx.com/'
postdata = {'username':'harry', 'password':'harry123'}

headers = {'User-Agent':user_agent, 'Referer':referer}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
html = response.read()

# 也可以这样写

req.add_header('User-Agent', user_agent)
req.add_header('Referer', referer)
req.add_data(data)
response = urllib2.urlopen(req)
html = response.read()
