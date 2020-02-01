import bs4
import urllib.request

url = "https://shopping.naver.com/living/homeliving/category?menu=10000921"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.find("a", {"class":"_8tp7k5rNMY"})
print(items)