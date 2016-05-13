from testingfunctions import Parser
import datetime
import time



def NPRPlayer():
    currentTime = time.strftime("%H:%M")
    if(currentTime == '10:35'):
        Parser("http://www.npr.org/podcasts/500005/hourly-news-summary")
    else:
        print("Waiting")
        time.sleep(10)
        NPRPlayer()

NPRPlayer()
