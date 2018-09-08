#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102UBrowser/6.1.2107.204 Safari/537.36'}
url = 'https://movie.douban.com/review/best/'
r = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(r).read()

soup = BeautifulSoup(res, "html.parser")
lists = soup.find_all('div', class_='main review-item')
I = 0
for line in lists:
    title = line.find('a', class_='subject-img').find('img')['title']#.encode('utf-8')
    name = line.find('a', class_='name').get_text()#.encode()
    content = line.find('div', class_='short-content').text#.encode()
    str_for_write = """
    name: %s
    title: %s
    content: %s
    """ %(name, title, content)
    #with open('spider.txt', 'wb') as f:
        #f.write(str_for_write)
        #f.close()
    print(str_for_write)
    I = I + 1
    print('第%d个已经扒取完成' %(I))
    #break
