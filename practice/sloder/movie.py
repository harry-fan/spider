#!/usr/lib/python2

import requests
print("start")

url = 'http://vd3.bdstatic.com/mda-ifhjfwfs07970fip/mda-ifhjfwfs07970fip.mp4'
r = requests.get(url, stream=True)

with open('bigMall.mp4', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024*1024):
        if chunk:
            mp4.write(chunk)

print("dowload over")
