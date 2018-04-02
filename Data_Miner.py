import tweepy
import datetime

now = datetime.datetime.now()
n = now.date
y = now.year

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
          #  with open(now.strftime('%d')+'_'+now.strftime('%m')+'_'+str(y)+'_query2.json', 'a') as f:
          with open(now.strftime('%d') + '_' + str(y) + '_colin_data.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    '''
        def on_status(self, status):
        print(status.text)
    '''
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

consumer_key = 'MgJmKnzEgbiIMej45dRiTLMo0'
consumer_secret = 'Ekm7vr8q9upcHjvL8KqvkQl6HnPzAjS1wS4kBAaUn6IzbUZ0MW'
access_token= '969345855105847297-ImVGCbferhWyaoPiGTqGWoQYLXUlSAf'
access_token_secret= 'Pwrwj0apYpK5wxY75CXMVXBfEPdeOsqnG0TkV7iyMqT00'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
'''
"bike lane", "bike lanes", "bikelane", "bikelanes", "bicycle lane", "bicycle lanes", "bicyclelane", "bicyclelanes", "cycle lane", "cycle lanes", "cyclelane", "cyclelanes", "bike path", "bike paths", "bikepath", "bikepaths", "bicycle path", "bicycle paths", "bicyclepath", "bicyclepaths", "cycle path", "cycle paths", "cyclepath", "cyclepaths", "bike trail", "bike trails", "biketrail", "biketrails", "bicycle trail", "bicycle trails", "bicycletrail", "bicycletrails", "cycle trail", "cycle trails", "cycletrail", "cycletrails", "bike boulevard", "bike boulevards", "bikeboulevard", "bikeboulevards", "bicycle boulevard", "bicycle boulevards", "bicycleboulevard", "bicycleboulevards", "cycle track", "cycle tracks", "cycletrack", "cycletracks", "bicycle track", "bicycle tracks", "bicycletrack", "bicycletracks", "bike track", "bike tracks", "biketrack", "biketracks", "bike sharrow", "bike sharrows", "bicycle sharrow", "bicycle sharrows", "bike route", "bike routes", "bikeroute", "bikeroutes", "bicyclist", "bicyclists", "cyclist", "cyclists", "biker", "bikers"
'''


args = ["bike lane", "bike lanes", "bikelane", "bikelanes", "bicycle lane", "bicycle lanes", "bicyclelane", "bicyclelanes", "cycle lane", "cycle lanes", "cyclelane", "cyclelanes", "bike path", "bike paths", "bikepath", "bikepaths", "bicycle path", "bicycle paths", "bicyclepath", "bicyclepaths", "cycle path", "cycle paths", "cyclepath", "cyclepaths", "bike trail", "bike trails", "biketrail", "biketrails", "bicycle trail", "bicycle trails", "bicycletrail", "bicycletrails", "cycle trail", "cycle trails", "cycletrail", "cycletrails", "bike boulevard", "bike boulevards", "bikeboulevard", "bikeboulevards", "bicycle boulevard", "bicycle boulevards", "bicycleboulevard", "bicycleboulevards", "cycle track", "cycle tracks", "cycletrack", "cycletracks", "bicycle track", "bicycle tracks", "bicycletrack", "bicycletracks", "bike track", "bike tracks", "biketrack", "biketracks", "bike sharrow", "bike sharrows", "bicycle sharrow", "bicycle sharrows", "bike route", "bike routes", "bikeroute", "bikeroutes", "bicyclist", "bicyclists", "cyclist", "cyclists", "biker", "bikers"]
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=args, async=True)


'''
public_tweets = api.search('bike bikes')
for tweet in public_tweets:
    print(tweet.text)
'''






