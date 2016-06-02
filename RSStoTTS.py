from WakeyCore import GTTS, playerVLC, RssFeed
import time

youList = input("RSS URL? ")
playList = "C:\\logs\\hello.mp3"
RssFeed(youList)
text = open("C:\\logs\\rss.txt")
rss = text.read()
GTTS(rss)
print(rss)
time.sleep(2)
playerVLC(playList)