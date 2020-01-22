import requests
from bs4 import BeautifulSoup


def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html





url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = get_html(url)

soup = BeautifulSoup(html, 'lxml')
tags = soup.findAll('div', attrs={'class': 'tit3'})

print(tags)