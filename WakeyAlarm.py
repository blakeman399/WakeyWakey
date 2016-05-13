from WakeyCore import youtubePlayList, playerVLC
import datetime
import time

AlarmTime = input("What time shall I wake you sir? ")
PlayList = input("Playlist? ")
playList = "C:\\logs\\goats.txt"

def AlarmClock(AlarmTime):
    currentTime = time.strftime("%H:%M")
    if(currentTime == AlarmTime):
        youtubePlayList(PlayList)
        playerVLC(playList)
    else:
        print("Waiting")
        time.sleep(10)
        AlarmClock(AlarmTime)

AlarmClock(AlarmTime)
