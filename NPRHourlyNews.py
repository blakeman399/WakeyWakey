  GNU nano 2.2.6                                                 File: NPRHourlyNews.py

from bs4 import BeautifulSoup
import urllib.request
import re
import os
import time
import datetime
import subprocess

print("Starting Requests")
url = urllib.request.urlopen("http://www.npr.org/podcasts/500005/hourly-news-summary")
content = url.read()
print("Request Done")

print("Start Parsing")
soup = BeautifulSoup(content, "html5lib")

#Find first mp3 link(newest)
variable = soup.find('a', href=re.compile('http.*\.mp3'))['href']

print("Done Parsing")

os.system("cvlc --play-and-exit 2> error.log " + variable)

#Use this if you want to find all MP3 links
#for a in soup.findAll('a',href=re.compile('http.*\.mp3')):
    #print ("URL:", a['href'])

    #C:\\Users\\bmastrud\\Downloads\\mps\\VLC.exe -Incurse --no-video https://www.youtube.com/watch?v=arj7oStGLkU

'''alarmTime = input("What time would you like me to wake you? ")

Youtube URl Option
youtubeURL = input("YouTube URL? ")


#Alarm Clock Method
while True:
    currentTime = time.strftime("%H:%M")
    if(currentTime == alarmTime ):
        subprocess.Popen("C:\\Users\\bmastrud\\Downloads\\mps\\VLC.exe --no-video " + youtubeURL, shell=False)
        time.sleep(60)
    else:
        print(currentTime)
        time.sleep(1) '''

