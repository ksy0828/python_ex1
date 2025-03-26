# https://www.malware-traffic-analysis.net/2023/index.html 를 크롤링 해서
# 1. 제목 주소를 가져오시오.
# 2. 링크 정보를 전체 URL 형식으로 출력하세요.
# 3. 결과 값을 txt 파일로 저장하세요.!!

import requests
import os, re
from bs4 import BeautifulSoup

header_info = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36'}
code = requests.get(f"https://www.malware-traffic-analysis.net/2023/index.html", headers=header_info)

soup = BeautifulSoup(code.text, "lxml")
# print(soup.prettify())


#제목 가져오기
titles = soup.select("#main_content > div.content > ul > li > a.main_menu")

    #파일 저장하기
with open(f'crawlQ.txt', 'w', encoding='utf-8') as file:
    for title, link in zip(titles, soup.find_all('a')):
        # print(title.text)
        
        href = link.get('href')
        if href:
            print(href)  # URL 출력
            file.write(f"제목 : {title.text} \n")
            file.write(f"링크 : https://www.malware-traffic-analysis.net/2023/{href} \n")
            # 아 뭔가 될 것 같은데 앞부분만 안나오면 될 것 같은데..


