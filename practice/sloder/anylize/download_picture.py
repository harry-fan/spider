#!/usr/lib/python3
import requests
from bs4 import BeautifulSoup
import os
import sys


reload(sys)
sys.setdefaultencoding('utf8')

headers = {'User-Agent': "Mozilla/5.0(windows Nt 6.1; WOW64) AppleWeibkit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url, headers=headers)

soup = BeautifulSoup(start_html.text, 'lxml')
li_list = soup.find('div', class_='all').find_all('a')
for li in li_list:
    title = li.get_text()
    href = li['href']
    html = requests.get(href, headers=headers)
    html_soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_soup.find('div', class_='pagenavi').find_all('span')
    max_sp = max_span.find_all('span')[-2].get_text()
    for page in range(1, int(max_sp)+1):
        page_url = href + '/' + str(page)
        img_html = requests.get(page_url, headers=headers)
        img_soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_soup.find('div', class_='main_image')
        if not img_url:
            continue
        img_url_bak = img_url.find('img')['src']
