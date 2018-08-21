from lxml import etree
import requests
import re

# 这是一个典型的搜索小说爬虫，
# 结合着F12去查看网页代码，就可以很清楚这个全部步骤

user_agent = 'Mozilla/4.0 (aompatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}

r = requests.get('http://seputu.com/', headers=headers)

pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
# parse page
html = etree.HTML(r.text)
div_muls = html.xpath('.//*[@class="mulu"]')
for div_mulu in div_muls:
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) >0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]#.encode('utf-8')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1)
                real_title = match.group(2)
                print(date, real_title)
