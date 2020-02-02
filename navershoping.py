import bs4
import urllib.request

url = "https://swindow.naver.com/designer/list/category"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.select('div >div > ul > li')
print(items)