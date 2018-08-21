
from bs4 import BeautifulSoup
import requests
import os

def write_file(name, txt):
    with open(name, 'a+') as f:
            f.write(txt)

if __name__ == '__main__':
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    url_ = "https://www.ybdu.com/xiaoshuo/19/19067/7006828.html"
    txt = requests.get(url_, headers=header)
    sp = BeautifulSoup(txt.text, "lxml")
    
    ttxt = sp.find('div', id='htmlContent')
    xxt_finally = ttxt.text.split(';')[0].strip()
    length = len(xxt_finally.split())
    num = 0
    while True:
        xx = xxt_finally.split()[num]
        if num < length - 1:
            write_file('page.txt', xx)
            num = num +1
        else:
            break
