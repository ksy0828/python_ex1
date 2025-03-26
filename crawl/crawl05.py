import requests
from bs4 import BeautifulSoup

keyword = input("키워드 입력 >> ")#검색키워드

for pnum in range(1, 5): #5페이지까지 가져오고 싶을때

    header_info = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36'}
    code = requests.get(f"https://kin.naver.com/search/list.naver?query={keyword}&page={pnum}", headers=header_info)
    # https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC
    soup = BeautifulSoup(code.text, "lxml")
    # print(soup.prettify())

    """
    #제목 가져오기
    titles = soup.select("#s_content > div.section > ul > li > dl > dt > a")
    # print(titles)
    for title in titles:
        print(title.text)

    #날짜 정보 가져오기 
    days = soup.select("#s_content > div.section > ul > li > dl > dd.txt_inline")
    for day in days:
        print(day.text)
    """
    titles = soup.select("#s_content > div.section > ul > li > dl > dt > a")
    dates = soup.select("#s_content > div.section > ul > li > dl > dd.txt_inline")


    for title, date in zip(titles, dates):
        print(f"질문 : {title.text}")
        print(f"날짜 : {date.text}")
        print()




