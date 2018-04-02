import json

#Input files to compare tweets:
file_1 = "02_04_2018"+".json"
file_2 = "26"+".json"

#Watch the magic work:
id_toRemove = {}

f1 = open(file_1, 'r')
f2 = open(file_2, 'r')

def tweet_reader(f):
    id = []
    for line in f:
        if line != '\n':
            tweets= json.loads(line)
            if tweets.has_key('id'):
                id.append(tweets['id'])
    return id

id_toRemove = set(tweet_reader(f1)) - set(tweet_reader(f2))
print(id_toRemove)



