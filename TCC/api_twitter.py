from api_base import API_Base
from credentials import TWITTER_CONSUMER_KEY,TWITTER_CONSUMER_SECRET,TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET
from requests_oauthlib import OAuth1

class API_Twitter(API_Base):

    def __init__(self):
        self.auth = OAuth1(TWITTER_CONSUMER_KEY,
                          TWITTER_CONSUMER_SECRET,
                          TWITTER_ACCESS_TOKEN,
                          TWITTER_ACCESS_TOKEN_SECRET)
        super().__init__('https://api.twitter.com/1.1', auth=self.auth)

    def get_users(self, screen_name):
        params = {'screen_name':screen_name}
        return super().make_request(self._url_base+'/users/show.json', params)

    def get_user_tweets(self, screen_name):
        params = {'screen_name':screen_name}
        return super().make_request(self._url_base+'/statuses/user_timeline.json', params)

screen_name = 'kevingo'
api = API_Twitter()
caio = api.get_users(screen_name)
tweets = api.get_user_tweets(screen_name)
print(tweets[1])
