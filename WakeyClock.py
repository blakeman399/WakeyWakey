import os
import time
import datetime
import subprocess

alarmTime = str(raw_input("What time would you like me to wake you? "))

youtubeURL = str(raw_input("YouTube URL? "))



while True:
    currentTime = time.strftime("%H:%M")
    if(currentTime == alarmTime ):
        subprocess.Popen("C:\\Users\\bmastrud\\Downloads\\mps\\VLC.exe --no-video " + youtubeURL, shell=False)
        time.sleep(60)
    else:
        print(currentTime)
        time.sleep(1)
        print(alarmTime)
