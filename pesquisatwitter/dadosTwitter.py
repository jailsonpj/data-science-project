from twython import Twython

CONSUMER_KEY="QR5fsBnBCqD3Rda6szBchJCdW"
CONSUMER_SECRET="13FYl5BN0QGd43X1qNhMPSZrjH2Virgo7uHKREv3aKPO3tmBKL"

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET)

#procura por tweets contendo a palavra python
for status in twitter.search(q='"python"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(user,":",text)
    print()
'''results = twitter.cursor(twitter.search,q='python')

for result in results:
    user = result["user"]["screen_name"]
    text = result["text"]
    print(user,":",text)
    print()'''
