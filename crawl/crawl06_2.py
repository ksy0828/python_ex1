# https://www.malware-traffic-analysis.net/2023/index.html 를 크롤링 해서
# 1. 제목 주소를 가져오시오.
# 2. 링크 정보를 전체 URL 형식으로 출력하세요.
# 3. 결과 값을 txt 파일로 저장하세요.!!

# 강사님 코드

import requests
from bs4 import BeautifulSoup

url = "https://www.malware-traffic-analysis.net/2023/index.html"
headers = {'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

tags = soup.select('#main_content > div.content > ul > li > a.main_menu')

print(tags)
# 결과 값 리스트
results = []

# 링크 정보 추출 및 출력
for tag in tags:
    link_text = tag.text
    link_href = f"https://www.malware-traffic-analysis.net/2023/{tag['href']}"
    results.append(f"제목 : {link_text}\n링크 : {link_href}\n")
    print(link_text)
    print(link_href)

# txt 파일로 저장
with open('malwares.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result)