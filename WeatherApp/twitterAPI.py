import twitter

api = twitter.Api(consumer_key='consumer_key',
    consumer_secret = 'consumer_secret',
    access_token_key = 'access_token_key',
    access_token_secret = 'access_token_secret')

#print(api.VerifyCredentials())
#statuses = api.GetUserTimeline(screen_name='CantBeatDaBEAST')
#print([s.text for s in statuses])

#status = api.PostUpdate('Tweeting from Python!')
#print(status.text)
def get_api(self):
    return api
