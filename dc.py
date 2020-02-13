import bs4
import requests
import pandas as pd
import datetime



DCUrl ='https://gall.dcinside.com/'

Page_id = 'leemalnyeon'
Page_index = '1'


def get_html(pageid, pageindex):
   url = 'https://gall.dcinside.com/mgallery/board/lists/'
   payload = {'id': pageid, 'page' : pageindex}
   headers = {
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
   }
   r = requests.get(url, params=payload, headers = headers)
   
   if r.status_code == 200:
      _html = r.text
   return _html



def get_dc_list(items):
   for item in items:
      #내용
      content = item.find('a')
      if content != None:
         content_text = content.text
      else:
         content_text = "X"
      #댓글
      comment = item.find('span', {"class": "reply_num"})
      if comment != None:
         comment_text = comment.text
      else:
         comment_text = '[0]'
   
      nickname = item.find('span', {"class": "ip"})
      if nickname != None:
         nickname_text = nickname.text
      else:
         nickname = item.find('span', {"class": "nickname in"})
         if nickname != None:
            nickname_text = nickname.text
         else:
            nickname_text = "X"


      url = item.find('a')
      if url != None:
         url = DCUrl +url["href"]
      else:
         url = "X"

      results.append((content_text, comment_text, nickname_text, url))
   
   return results





results = list()
html = get_html(Page_id, Page_index)
soup = bs4.BeautifulSoup(html, "lxml")
items = soup.find_all('tr')

get_dc_list(items)



data = pd.DataFrame(results)
data.columns = ['content', 'comments', 'nickname', 'url']
now = datetime.datetime.now()
data.to_csv(f'DC-{Page_id}-{now}.csv', encoding='utf-8-sig')