#!/usr/bin/python3
#-*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102UBrowser/6.1.2107.204 Safari/537.36'}

url_list = []
def get_href(url):
    if url in url_list:
        return None
    else:
        url_list.append(url)
        return url

def down_pic(url):
    r = requests.get(url, headers)
    name = url[-10:-4]
    print(name)
    with open(name+'.jpg', 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

def get_url_list(url):
    get_url = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(get_url).read() 
    soup = BeautifulSoup(res, "html.parser")
    pict_list = soup.find('div', id='list_img').find_all('a', target='_blank')
    return pict_list

def get_new_url(content):
    html = content['href']
    new_url = get_href(html)
    if new_url == None:
        return None
    else:
        return new_url

def get_picture_url_info(url):
    girl_url = urllib.request.Request(url, headers=headers)
    ret_girl_url = urllib.request.urlopen(girl_url).read()
    soup = BeautifulSoup(ret_girl_url, "html.parser")
    picture = soup.find_all('div', class_='p-tmb')
    return picture

def get_addr(girl_url):
    tmp = girl_url.find('img')
    addr = tmp['src']
    www = "http://www.xiaohuar.com"
    return www+addr

def start():
    url = 'http://www.xiaohuar.com/list-1-\d+.html'
    lst = get_url_list(url)
    for line in lst:
        new_url = get_new_url(line)
        if new_url == None:
            continue
        info = get_picture_url_info(new_url)
        for girl in info:
            addr = get_addr(girl)
            print('addr:', addr)
            down_pic(addr)
        break

if __name__ == '__main__':
    start()
