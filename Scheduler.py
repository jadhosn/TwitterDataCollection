import schedule
import tweepy
import datetime
import os.path

filename = "999"
consumer_key = 'MgJmKnzEgbiIMej45dRiTLMo0'
consumer_secret = 'Ekm7vr8q9upcHjvL8KqvkQl6HnPzAjS1wS4kBAaUn6IzbUZ0MW'
access_token= '969345855105847297-ImVGCbferhWyaoPiGTqGWoQYLXUlSAf'
access_token_secret= 'Pwrwj0apYpK5wxY75CXMVXBfEPdeOsqnG0TkV7iyMqT00'
args = ["bike lane", "bike lanes", "bikelane", "bikelanes", "bicycle lane", "bicycle lanes", "bicyclelane", "bicyclelanes", "cycle lane", "cycle lanes", "cyclelane", "cyclelanes", "bike path", "bike paths", "bikepath", "bikepaths", "bicycle path", "bicycle paths", "bicyclepath", "bicyclepaths", "cycle path", "cycle paths", "cyclepath", "cyclepaths", "bike trail", "bike trails", "biketrail", "biketrails", "bicycle trail", "bicycle trails", "bicycletrail", "bicycletrails", "cycle trail", "cycle trails", "cycletrail", "cycletrails", "bike boulevard", "bike boulevards", "bikeboulevard", "bikeboulevards", "bicycle boulevard", "bicycle boulevards", "bicycleboulevard", "bicycleboulevards", "cycle track", "cycle tracks", "cycletrack", "cycletracks", "bicycle track", "bicycle tracks", "bicycletrack", "bicycletracks", "bike track", "bike tracks", "biketrack", "biketracks", "bike sharrow", "bike sharrows", "bicycle sharrow", "bicycle sharrows", "bike route", "bike routes", "bikeroute", "bikeroutes", "bicyclist", "bicyclists", "cyclist", "cyclists", "biker", "bikers"]


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            with open(filename, 'a') as f:
                f.write(data)
            f.close()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status_code):
        if status_code == 420:
            return False

def job():
    print "in the loop"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=args, async=True)

'''
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
'''
schedule.every(1).minute.do(job)

while 1:
    now = datetime.datetime.now()
    name = now.strftime('%d') + "_" + now.strftime('%m') + "_" + now.strftime('%Y')
    filename = name + ".json"
    if os.path.isfile(filename):
        name += "_min" + now.strftime('%M') + "_sec" + now.strftime('%S')
        filename = name + ".json"
    print(filename)
    schedule.run_pending()















