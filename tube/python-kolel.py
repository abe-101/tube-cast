import feedparser
import json
import os
import json
from datetime import datetime, timedelta, timezone
from dateutil.tz import tzutc
from dateutil import parser

pod = feedparser.parse('https://anchor.fm/s/955ecec4/podcast/rss')

titles = set()
for entry in pod.entries:
    titles.add(entry['title'])


with open("/home/thinkpad/repos/Kolel-L-horah-Maaseh-Podcast/kolel_nice_updated.json") as file:
    data = json.load(file)


new = []
for entry in data:
    if not entry['title'] in titles:
        new.append(entry)


for i in range(10):
    print(new[i]['id']+',', end=''
