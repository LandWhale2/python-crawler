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
webtoon_list = list()
webtoon_area = soup.find("table", {"class" : "viewList"}).find_all("td", {"class" : "title"})
for webtoon_index in webtoon_area:
    info_soup = webtoon_index.find("a")
    _url = info_soup["href"]
    _text = info_soup.text.split(".")
    _title = ""
    _num = _text[0]
    if len(_text) > 1:
        _title = _text[1]
    webtoon_list.append((_num, _title, _url, ))
print(webtoon_list)
