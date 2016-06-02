from bs4 import BeautifulSoup
import urllib.request
from gtts import gTTS
import time
import re
import os
import contextlib
import requests

# Windows Path
filePath = "C:\\logs\\"
vlcPlayer = "C:\\Users\\bmastrud\Desktop\\vlc-2.2.3\\"


# NPR Hourly Podcast Parser
def PodcastParser(url):
    print("Starting Requests")
    url = urllib.request.urlopen(url)
    print("Request Done")
    content = url.read()
    print("Start Parsing")
    soup = BeautifulSoup(content, "html.parser")
    # Find first mp3 link(newest)
    variable = soup.find('a', href=re.compile('http.*\.mp3'))['href']
    print("Done Parsing", variable)
    playerVLC(variable)


# YouTubeParser - Creates txt file with playlists urls
def youtubePlayList(url):
    # Removes old playlist file-Supresses error if file does not exist
    with contextlib.suppress(FileNotFoundError):
        os.remove(filePath + "playList.txt")

    url = urllib.request.urlopen(url)
    content = url.read()
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all("tr", {"class": "pl-video"})
    time.sleep(2)
    for link in links:
        # print(link.get("data-title"))
        log = open(filePath + "playList.txt", "a")
        print("https://www.youtube.com/watch?v=" + link.get("data-video-id"), file=log)


# RSSParser - Finds Headlines
def RssFeed(RssURL):
    with contextlib.suppress(FileNotFoundError):
        os.remove(filePath + "rss.txt")
    url = urllib.request.urlopen(RssURL)
    content = url.read()
    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all('item')
    for item in items:
        title = item.find('title').text
        log = open(filePath + "rss.txt", "a")
        print(title, file=log)


# Google TTS
def GTTS(txt):
    tts = gTTS(text=txt, lang='en')
    tts.save(filePath + "hello.mp3")


# VLCFunction
def playerVLC(Media):
    print("Starting VLC")
    os.system(vlcPlayer + "vlc " + Media)

def youtubeSearch(Query):
    youtube = "https://www.youtube.com/results?search_query="
    youtubePlay = "https://www.youtube.com"
    inputVar = Query
    results = youtube + inputVar.replace(" ", "+")
    r = requests.get(results)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        test = youtubePlay + soup.find('a', href=re.compile('/watch'))['href']
        return test
