from bs4 import BeautifulSoup

#soup = BeautifulSoup(open('index.html'), "lxml")
soup = BeautifulSoup(open('index.html'))

#print(soup.prettify())

print(soup.title.text.strip()) # 获取文本 The Dormouse's story 

print(soup.title.name) # title
soup.title.name = "myTitle"
print(soup.title) # None
print(soup.myTitle) # html文件中的title

print(soup.p['class'])
print(soup.p.get('class')) # 这两行都是['title']

print(soup.p.attrs) # {'class': ['title']}
print(soup.p.string) # The Dormouse's story


print(soup.name) # [document]
print(soup.attrs) # {}

print(soup.a.string) # Elsie

for string in soup.strings:
    print(repr(string))

soup.stripped_strings # 去除输出字符串中包含的空格和空行 

print(soup.find_all('a')) # a的所有集合

print(soup.select("title"))
print(soup.select("html head title"))

print(soup.select("a# link1"))

print(soup.select('a[href]'))
