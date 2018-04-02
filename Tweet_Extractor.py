import json

f = open('28_2018_jad_data.json', 'r')
for line in f:
    tweets= json.loads(line)
    if tweets.has_key('extended_tweet'):
        print "TEXT"
        print tweets['text']
        print '\r'
        print "EXTENDED"
        print tweets['extended_tweet']['full_text']
        print '\n'
    else:
        print "ONLY SHORT TEXT"
        print tweets['text']
        print '\n'
