from bs4 import BeautifulSoup as bs
from pytube import YouTube
import requests
import os
import re
url = "https://www.youtube.com/watch?v=w96a4FYUA-4&list=PLJYf0JdTApCqAbZImkQagXEuByh-b_7To"
r = requests.get(url)
page = r.text
soup=bs(page,'html.parser')

vids = soup.findAll(href=re.compile("watch"))
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
print(videolist)
count=0
for item in videolist:
 
    # increment counter:
    count+=1
 
    # initiate the class:
    try:
        yt = YouTube(item)
    except:
        print("error encountered")
        continue

    stream = yt.streams.first().download('./')

print(count)