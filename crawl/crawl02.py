#250326 웹 크롤링
import requests
from bs4 import BeautifulSoup

url = "https://www.boannews.com/" #http's'를 하면 인증서가 없다는 등등 오류 발생

header_info = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36'}
#헤더 정보가 없으면 봇으로 판단해 못 가져오는 사이트가 있음 (네이버는 필수)
#사이트마다 요청하는 헤더정보가 다를 수 있고 변경될 수 있음

# r.text : HTML 정보
r = requests.get(url, headers=header_info, verify=False) #verify 검증을 하지 않음 (http's')
soup = BeautifulSoup(r.text, 'lxml')
# print(soup.prettify())
links = soup.find_all('a')
for link in links:
    print(link.get('href')) #link 정보만 뽑아오기