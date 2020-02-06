import bs4
import urllib.request

url = "https://swindow.naver.com/designer/list/category"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.find_all('li', {"class": "item  _NEW_ITEM_LAYOUT"})
items = soup
print(items)

#크롤링 시 숨겨진 url 도 있다