import bs4
import urllib.request

url = "https://search.shopping.naver.com/search/all.nhn?query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%87%BC%ED%95%91&frm=NVSCPRO"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.find('li', {"class": "_model_list _itemSection"})
item = items.find_all('a')
print(items)

