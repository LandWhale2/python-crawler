# import bs4
# import requests




# def get_html(url):
#    _html = ""
#    resp = requests.get(url)
#    if resp.status_code == 200:
#       _html = resp.text
#    return _html


# url = "https://news.naver.com/"
# html = get_html(url)

# soup = bs4.BeautifulSoup(html, "lxml")
# inner = soup.findAll("div", {"class":"newsnow_tx_inner"})
# print(inner)

import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(html, "html.parser")
news = soup.find("div", {"class":"section section_wide"}).find_all("a", {"class" : "nclicks(rig.ranklif)"})
results = []
for news_index in news:
    # info = news_index.find("a")
    print(news_index.text)
    # print(_url)