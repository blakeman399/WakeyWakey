from bs4 import BeautifulSoup
import urllib.request
import re
import os
import time
import datetime
import subprocess

url = urllib.request.urlopen("http://www.npr.org/podcasts/500005/hourly-news-summary")
content = url.read()
soup = BeautifulSoup(content)

#Find first mp3 link(newest)
variable=soup.find('a', href=re.compile('http.*\.mp3'))['href']

print(variable)
os.system("C:\\Users\\Blake\\Desktop\\VLC\\VLC.exe " + variable)

#Use this if you want to find all MP3 links
#for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
    #print ("URL:", a['href'])


