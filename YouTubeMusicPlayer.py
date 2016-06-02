
from WakeyCore import playerVLC, youtubeSearch

def YouyPlayer():
    search = input("What Song Would You Like? ")
    playerVLC(youtubeSearch(search))
YouyPlayer()