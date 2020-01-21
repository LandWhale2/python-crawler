from bs4 import BeautifulSoup
import requests


def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
html = get_html(url)
soup = BeautifulSoup(html, 'lxml')
l = soup.find_all("a")
print(len(l))


