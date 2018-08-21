# 扒取灵车小说

from bs4 import BeautifulSoup
import requests
import os

base_url = "http://www.jingyu.com"
url_1 = "/chaplist/MdbYExW7L3G3Ow.html?exsrc=360soonebox"

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

url = base_url + url_1
base_page = requests.get(url, headers=header)
soup = BeautifulSoup(base_page.text, "lxml")

file_table = {}

def gen_dir_name(page):
    dir_name = page.find('h4', class_='volume')
    if dir_name and len(dir_name.text) >=4 :
        name = dir_name.text.split()[1].strip()
        return name
    else:
        return False

def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)

def gen_chapter(page):
    chapter_list = page.find_all("li", class_=' col-4')
    for lst in chapter_list:
        url_ = lst.find('a')['href']
        file_name = lst.text.split()[1].strip()
        global file_table
        file_table[file_name] = url_

def get_new_soup(urll):
    url_new = base_url + urll
    txt_page = requests.get(url_new, headers=header)
    txt_soup = BeautifulSoup(txt_page.text, "lxml")
    return txt_soup

def get_txt(soup):
    #article = soup.find('div', class_='content-wrap').find_all('p')
    article = soup.find_all('p')
    # 动态渲染页面，延时加载, 目前不会，暂时不往后处理了

if __name__ == '__main__':
    volume = soup.find("ul", class_="volume-list").find_all('li') # 获取卷章节 根据名字创建目录
    for page in volume:
        name = gen_dir_name(page)
        if not name:
            continue
        gen_chapter(page)
    
    for i in file_table:
        urll = file_table[i]
        urll = "/chapter/7aCkFBGyLHCDOj.html" # 正式扒取时候，取消这句
        soup = get_new_soup(urll)
        get_txt(soup)
        break
