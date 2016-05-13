import requests
from bs4 import BeautifulSoup
import os
import sys
import time
import contextlib

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
