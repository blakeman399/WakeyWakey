import time
import datetime
import subprocess


while True:
    currentTime = time.strftime("%H:%M")
    if(currentTime == '09:17'):
        print("hello")
        #Play Youtube URL in audio mode with VLC
        subprocess.Popen("VLC --no-video https://youtu.be/lsJLLEwUYZM?list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG", shell=False)
        time.sleep(60)
    else:
        print(currentTime)
        time.sleep(1)
