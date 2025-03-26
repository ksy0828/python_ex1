import feedparser
import pandas as pd

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)

titles = []
links = []
descriptions = []
authors = []
pubDates = []

for entry in feed.entries: #피드에서 엔트리 정보 가져와서 []공간에 저장하기
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

print(titles)