import requests
from bs4 import BeautifulSoup

url = "https://www.boannews.com/"

header_info = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36'}

r = requests.get(url, headers=header_info, verify=False)
soup = BeautifulSoup(r.text, 'lxml')
subjects = soup.select('#headline0 > ul > li > p')
for subject in subjects:
    print(subject.te)