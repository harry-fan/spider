#!/usr/bin/python2.7
# coding:utf-8

# 执行方式可以： ./g_event_yield.py 2.7版本解释器已经内嵌

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

# 没有utf-8出现中文会报错

def run_task(url):
    print('Vist -- > %s' % url)
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print("%d bytes received from %s." %(len(data), url))
    except Exception, e:
        print(e)

urls = ['https://github.com/', 'https://www.python.org/','https://cnblogs.com/']
greenlets = [gevent.spawn(run_task, url) for url in urls]
gevent.joinall(greenlets)

# 结果
# Vist -- > https://github.com/
# Vist -- > https://www.python.org/
# Vist -- > https://cnblogs.com/
# 45741 bytes received from https://cnblogs.com/.
# 81991 bytes received from https://github.com/.
# 48822 bytes received from https://www.python.org/.
