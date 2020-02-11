import bs4
import requests


def get_html():
   url = 'https://gall.dcinside.com/mgallery/board/lists/'
   payload = {'id': 'leemalnyeon', 'page' : '1'}
   headers = {
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
   }
   r = requests.get(url, params=payload, headers = headers)
   
   if r.status_code == 200:
      _html = r.text
   return _html




html = get_html()
soup = bs4.BeautifulSoup(html, "lxml")
items = soup.find_all('tr')
for item in items:
   content = item.find('a')
   if content != None:
      print(content.text)
   
# print(soup)
# print(items)
# items = soup.find('tr', {"class" : "ub-content us-post"})
# print(items)