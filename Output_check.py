import os, os.path
import datetime

now = datetime.datetime.now()

files =[]
for file in os.listdir('.'):
    if file.endswith(".json"):
        files.append(file)
print files
print len(files)