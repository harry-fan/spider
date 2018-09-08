#-*- coding:utf-8 -*-
import re
import json
from bs4 import BeautifulSoup
import urllib.request
import requests

if __name__ == '__main__':
    ip = 'http://www.iqiyi.com/v_19rrb2yq04.html?fc=8b62d5327a54411b#vfrm=19-9-0-1'
    get_url = 'http://www.sfsft.com/api.php?=%s' %ip

    get_movie_url = 'http://www.sfsf.com/api.php'

    head = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',
            'referer':'http://www.sfsft.com/index.php?url=%s' %ip}

    get_url_req = requests.get(url = get_url, headers = head)
    get_url_response = urllib.request.urlopen(get_url_req)
    get_url_html = get_url_response.read().decode('utf-8')
    print(get_url_html)
    bf = BeautifulSoup(get_url_html, 'lxml')

    a = str(bf.find_all('script'))
    pattern = re.compile("url: '(.+)',", re.IGNORECASE)

