import requests
from bs4 import BeautifulSoup
 

def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


url = "https://www.naver.com/"
html = get_html(url)
soup = BeautifulSoup(html,'lxml') # BeautifulSoup 객체생성
keywords = soup.find_all('a').find('span') # 데이터에서 태그와 클래스를 찾는 함수
print(keywords)
