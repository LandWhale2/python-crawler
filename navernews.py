import pandas as pd
import bs4
import urllib.request

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(html, "html.parser")
news = soup.find("div", {"class":"section section_wide"}).find_all("a", {"class" : "nclicks(rig.ranklif)"})
results = list()
index = 0
for news_index in news:
    index += 1
    _url = url+news_index["href"]
    results.append((_url, news_index.text))
    


data = pd.DataFrame(results)
data.columns = ['url', 'title']
print(data.head())
data.to_csv('NaverNews_kr', encoding='cp949')