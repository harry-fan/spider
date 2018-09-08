import re
import requests

response = requests.get('http://www.xiaohuar.com/v/')

urls = re.findall(r'class="items".*?href="(.*?)"',response.text,re.S)
#print(urls)
#exit(0)
url = urls[5]
result = requests.get(url)
mp4_url = re.findall(r'id="media".*?src="(.*?)"',result.text, re.S)[0]

video = requests.get(mp4_url)
with open('meizi.mp4', 'wb') as f:
    f.write(video.content)
