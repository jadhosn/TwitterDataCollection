import tweepy
import datetime


consumer_key = 'JUAFioA4gWgxzxKcT9gdnkHLV'
consumer_secret = 't9hHzC5Q1lqqJzpmPEdSsOjZivT2Judh4EHw1OcZyCUJx4qEzL'
access_token= '128497598-PMg6jKPgh7U7RtI2MlM7Evh4COuL77sFtSBnC7AC'
access_token_secret= 'dGOXwaQpipwieSJpesxtMZUnq3HQidvbeT8EXXGFyWODu'
args = ["bike lane", "bike lanes", "bikelane", "bikelanes", "bicycle lane", "bicycle lanes", "bicyclelane", "bicyclelanes", "cycle lane", "cycle lanes", "cyclelane", "cyclelanes", "bike path", "bike paths", "bikepath", "bikepaths", "bicycle path", "bicycle paths", "bicyclepath", "bicyclepaths", "cycle path", "cycle paths", "cyclepath", "cyclepaths", "bike trail", "bike trails", "biketrail", "biketrails", "bicycle trail", "bicycle trails", "bicycletrail", "bicycletrails", "cycle trail", "cycle trails", "cycletrail", "cycletrails", "bike boulevard", "bike boulevards", "bikeboulevard", "bikeboulevards", "bicycle boulevard", "bicycle boulevards", "bicycleboulevard", "bicycleboulevards", "cycle track", "cycle tracks", "cycletrack", "cycletracks", "bicycle track", "bicycle tracks", "bicycletrack", "bicycletracks", "bike track", "bike tracks", "biketrack", "biketracks", "bike sharrow", "bike sharrows", "bicycle sharrow", "bicycle sharrows", "bike route", "bike routes", "bikeroute", "bikeroutes", "bicyclist", "bicyclists", "cyclist", "cyclists", "biker", "bikers"]


class MyStreamListener(tweepy.StreamListener):
    def get_filename(self):
        now = datetime.datetime.now()
        #filename = now.strftime('%M')+"_"+now.strftime('%d') + "_" + now.strftime('%m') + "_" + now.strftime('%Y')
        filename = now.strftime('%d') + "_" + now.strftime('%m') + "_" + now.strftime('%Y')
        return filename+'.json'

    def on_data(self, data):
        try:
            savefile=open(self.get_filename(),'a')
            savefile.write(data)
            savefile.close()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status_code):
        if status_code == 420:
            return False

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=args, async=True)

