# 使用urlretrieve函数将远程数据下载到本地

import urllib
from lxml import etree
import requests

def Schedule(blocknum, blocksize, totalsize):
    '''
    blocknum: 已经下载的数据块
    blocksize: 数据块的大小
    totalsize: 远程文件大小
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前进度: %d' % per)

user_agent = 'Mozilla/4.0 (aompatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}

r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
# 使用lxml解析网页
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src') #找寻所有的img
i = 0

for img_url in img_urls:
    urllib.request.urlretrieve(img_url, 'img'+str(i)+'.jpg', Schedule)
    i = i + 1
