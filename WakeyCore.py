from bs4 import BeautifulSoup
import urllib.request
import datetime
import time
import re
import os
import subprocess


def PodcastParser(url):
    print("Starting Requests"); url = urllib.request.urlopen(url)
    print("Request Done"); content = url.read()
    print("Start Parsing"); soup = BeautifulSoup(content, "html.parser")
    #Find first mp3 link(newest)
    variable = soup.find('a', href=re.compile('http.*\.mp3'))['href']
    print("Done Parsing", variable)
    playerVLC(variable)
    return

def youtubePlayList(url):
    #Removes old playlist file-Supresses error if file does not exist
    with contextlib.suppress(FileNotFoundError):
        os.remove("c:\\logs\\goats.txt") 
    URL = url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all("tr", {"class": "pl-video"})
    time.sleep(2)
    for link in links:
        #print(link.get("data-title"))
        log = open("c:\\logs\\goats.txt", "a")
        print("https://www.youtube.com/watch?v=" + link.get("data-video-id"), file = log)
        test = "c:\\logs\\goats.txt"
        return


def playerVLC(Media):
    os.system("C:\\Users\\bmastrud\\Desktop\\vlc-2.2.3\\vlc -Incurse --play-and-exit 2> error.log " + Media)
    return

        

