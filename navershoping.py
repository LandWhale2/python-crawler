import bs4
import urllib.request

url = "https://shopping.naver.com/living/homeliving/home"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.find("div", {"class":"_17oierHrKR"}).find_all("div", {"class":"txmFxWP6wn"})
print(items)