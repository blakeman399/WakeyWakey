from bs4 import BeautifulSoup
import urllib.request
import datetime
import time
import re
import os
import subprocess


def Parser(url):
    print("Starting Requests"); url = urllib.request.urlopen(url)
    print("Request Done"); content = url.read()
    print("Start Parsing"); soup = BeautifulSoup(content, "html.parser")
    #Find first mp3 link(newest)
    variable = soup.find('a', href=re.compile('http.*\.mp3'))['href']
    print("Done Parsing", variable)
    playerVLC(variable)
    return


def playerVLC(variable):
    os.system("C:\\Users\\bmastrud\\Desktop\\vlc-2.2.3\\vlc -Incurse --play-and-exit 2> error.log " + variable)
    return
