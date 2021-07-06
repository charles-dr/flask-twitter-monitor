import tweepy
from pytwitter import Api
import os
import logging
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

logger.info(f"Processing tweet id ~")

CONSUMER_KEY = "2KjuEM5fJtLVlf0oxP4UhFwDu"
CONSUMER_SECRET = "ZEWHR1RvVXO5TqQBSz3Y1ZsBq24k51BSa7uDrwaDKbsVu9Z17j"
ACCESS_TOKEN = "1052098057922273280-ijrjpHRnSjYVsmoZWwrNmnyC2TADFD"
ACCESS_TOKEN_SECRET = "MgKlIwO0LiqBaAA3xgankdxUcyiWUOncYJ6C7MJpNX2T9"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABgWEAEAAAAA87yfet9KQjmZFmn2ieiiKK3W9ok%3DIK80SpDOwyxnkjeeTTziQTKYGCxzIgcFOhfCTEIvAlumk9VTCW"

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create API Object
# api = tweepy.API(auth)

def create_api(consumer_key, consumer_secret, access_token, access_token_secret):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth, wait_on_rate_limit=True)
  return api

def create_api_v12(consumer_key, consumer_secret, access_token, access_token_secret):
  client = tweepy.Client(bearer_token=BEARER_TOKEN,
    consumer_key = consumer_key
    , consumer_secret = consumer_secret
    , access_token = access_token
    , access_token_secret = access_token_secret)
  return client

def create_api_v2(bearer_token):
  api = Api(
    bearer_token = bearer_token
    # consumer_key = consumer_key,
    # consumer_secret = consumer_secret,
    # access_token = access_token,
    # access_token_secret = access_token_secret,
  )
  return api


# api = create_api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# user_timeline = api.user_timeline(screen_name='CMIContent')

# try:
#   api.update_status("Did you get a vaccine?")
# except Exception as e:
#   print(e)


# user = api.get_user('AdWeek')
# print('User Details:')
# print(user.name)
# print(user.location)
# print(user.status.text)
# print('[User] ID', user.id)
# statuses = api.lookup_users([user.id])
# print('[Statuses]', statuses[0].status)

## ----------- V1
api_v1 = create_api(
  consumer_key = CONSUMER_KEY,
  consumer_secret = CONSUMER_SECRET,
  access_token = ACCESS_TOKEN,
  access_token_secret = ACCESS_TOKEN_SECRET,
  )

# status = api_v1.get_status('1410639112613163009', tweet_mode = 'extended')
statuses = api_v1.statuses_lookup(id_=['1410639112613163009'], tweet_mode = 'extended')
status = statuses[0]
# print('[V1][Status]', status.retweeted_status.full_text)

# user_v1 = api_v1.get_user(screen_name = 'BusiHelper')
# print('[User] V1:', user_v1)


## ----------- V2
# api_v2 = create_api_v2(bearer_token = BEARER_TOKEN)
# user_v2 = api_v2.get_user(username = 'BusiHelper')

# print('[User] V2:', user_v2.__dict__['data'].id)

# timelines = api_v2.get_timelines(user_id = user_v2.__dict__['data'].id, start_time="2021-07-01T00:00:00Z", end_time="2021-07-05T00:00:00Z",
#   media_fields = ['url', 'public_metrics' ],
#   expansions=['author_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id'],
#   tweet_fields = ['author_id', 'entities', 'id', 'lang', 'public_metrics', 'text', 'referenced_tweets'],
#   user_fields = ['id', 'name', 'public_metrics', 'verified']
# )
# _twit = timelines.data[0].__dict__
# print('[Timeline] V2', timelines.data[0].__dict__)
# print('[Text] V2', timelines.data[0].__dict__['text'])
# print('[Entities]', timelines.data[0].__dict__['entities'].__dict__)
# print('[Public Metrics]', timelines.data[0].__dict__['public_metrics'].__dict__)
# print('[Reference Tweet]', _twit['referenced_tweets'][0].__dict__)



# api_v2 = create_api_v2(consumer_key = CONSUMER_KEY, 
#   consumer_secret = CONSUMER_SECRET, access_token = ACCESS_TOKEN, access_token_secret = ACCESS_TOKEN_SECRET)
# user1 = api_v2.get_user(username = 'BusiHelper')
# print('[API V2][User]', user1)
