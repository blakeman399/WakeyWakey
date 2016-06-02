from bs4 import BeautifulSoup
import urllib.request
from gtts import gTTS
import time
import re
import os
import contextlib
#import requests
from googleapiclient.discovery import build

# Windows Path
filePath = "C:\\logs\\"
vlcPlayer = "C:\\Users\\blake\Desktop\\vlc-2.2.3\\"


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


# YouTube Player
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=options,
        part="id",
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result["id"]["videoId"])

            youtubePlay = "https://www.youtube.com/watch?v="

    playerVLC(youtubePlay + videos[0])


# Legacy youtube search player
'''def youtubeSearch(Query):
    youtube = "https://www.youtube.com/results?search_query="
    youtubePlay = "https://www.youtube.com"
    inputVar = Query
    results = youtube + inputVar.replace(" ", "+")
    r = requests.get(results)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        test = youtubePlay + soup.find('a', href=re.compile('/watch'))['href']
        print(test)
        return test'''
