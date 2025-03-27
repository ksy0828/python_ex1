##퀴즈
import feedparser
from openpyxl import Workbook

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)
titles = []
links = []
descriptions = []
authors = []
pubDates = []

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

wb = Workbook()
ws = wb.active 
ws.title = "RSS"

headers = ['타이틀', 'link', 'descriptions', 'authors', 'pubDates']
ws.append(headers)

#보안뉴스 정보를 RSS로 가져와서 엑셀파일로 생성!!!

for i in range(len(titles)):
    ws.append([titles[i], links[i], descriptions[i], authors[i], pubDates[i]])


wb.save("snews.xlsx")