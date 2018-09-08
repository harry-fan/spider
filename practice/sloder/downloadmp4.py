#!/usr/lib/python3

import requests
from bs4 import BeautifulSoup

archive_url = 'http://www.4pcc.com/play/19817-0-0.html'

def get_video_links():
    r = requests.get(archive_url)
    print("r = ", r)
    soup = BeautifulSoup(r.content, "html5lib")
    links = soup.findAll('a')
    print("links = ", links)
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]
    print video_links
    return video_links

def download_video_series(video_links):
    for link in video_links:
        file_name = link.splite('/')[-1]

        print("Downloading file:%s" %file_name)
        r = requests.get(link, stream=True)


        with open(file_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

print("download over")

if __name__ == "__main__":
    video_link = get_video_links()
    download_video_series(video_link)
