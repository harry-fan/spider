#!/usr/bin/python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
url = 'https://movie.douban.com/review/best/'
r = requests.get(url, headers=header)

soup = BeautifulSoup(r.text, "html.parser")
lists = soup.find_all('div', class_='main review-item').find_all('a')['title']

