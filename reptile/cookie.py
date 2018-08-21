#!/usr/bin/python2.7
#coding:utf-8

import cookielib
import urllib2

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
res = opener.open('http://www.zhihu.com')
for item in cookie:
    print(item.name +':'+ item.value)
