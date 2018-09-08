#!/usr/lib/python3
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import os
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

if(os.name == 'nt'):
    print(u'你正在使用win平台')
else:
    print(u'你使用linux平台')

def write_down(html, name):
    with open(name, 'wb') as f:
        for chunk in html.iter_content(1024):
            if chunk:
                html.write(chunk)

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

all_url = 'http://www.mzitu.com'
start_html = requests.get(all_url, headers=header)
path = './mzitu/'

soup = BeautifulSoup(start_html.text, "html.parser")
page = soup.find_all('a', class_='page-numbers')
max_page = page[-2].text

same_url = 'http://www.mzitu.com/page'
for n in range(1, int(max_page)+1):
    url = same_url + str(n)
    start_html = requests.get(url, headers=header)
    soup = BeautifulSoup(start_html.text, "html.parser")
    all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
    for a in all_a:
        title = a.get_text()
        if(title != ''):
            print('start:' + title)

            if(os.path.exists(path+title.strip().replace('?', ''))):
                flag = 1
            else:
                os.makedirs(path+title.strip().replace('?', ''))
                flag = 0
            os.chdir(path + title.strip().replace('?', ''))
            href = a['href']
            html = requests.get(href, headers = header)
            mess = BeautifulSoup(html.text, 'html.parser')
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text
            if(flag == 1 and len(os.listdir(path + title.strip().replace('?',' ')))>= int(pic_max)):
                print('aready exist')
                continue
            for num in range(1, int(pic_max)+1):
                pic = href + '/' + str(num)
                html = requests.get(pic, headers=header)
                mess = BeautifulSoup(html.text, 'html.parser')
                pic_url = mess.find('img', alt=title)
                html = requests.get(pic_url['src'], headers=header)
                print(pic_url['src'])
                file_name = pic_url['src'].split(r'/')[-1]
                #f = open(file_name, 'wb')
                #f.write(html.content)
                #f.close()
                write_down(html, file_name)
            print('finish')
    print('第',n,'页完成')



