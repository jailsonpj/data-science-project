from twython import Twython, TwythonError
import pandas as pd

CONSUMER_KEY="QR5fsBnBCqD3Rda6szBchJCdW"
CONSUMER_SECRET="13FYl5BN0QGd43X1qNhMPSZrjH2Virgo7uHKREv3aKPO3tmBKL"
ACCESS_TOKEN = "231448840-l12SVUES8llIvk136fktswGHUvCOl6UbYCW5CLz7"
ACCESS_SECRET = "vJpuj4jvzKA7DhyQmucxfWRntyF4jDMvDhEmM0EfiTntG"
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)


#procura por tweets contendo a palavra python
'''for status in twitter.search(q='"python"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(user,":",text)
    print()'''

#pesquisa timeline de um usurio
try:
    user_timeline = twitter.get_user_timeline(screen_name='julianyraiol')
except TwythonError as e:
    print(e)
print(user_timeline)
