import json

id_jad=[]
id_colin=[]

#f = open('28_2018_jad_data.json', 'r')
f = open('26.json', 'r')
for line in f:
    tweets= json.loads(line)
    if tweets.has_key('id'):
        id_jad.append(tweets['id'])

f = open('02_04_2018.json', 'r')
for line in f:
    if line != '\n':
        tweets = json.loads(line)
        if tweets.has_key('id'):
            id_colin.append(tweets['id'])

print set(id_colin) - set(id_jad)