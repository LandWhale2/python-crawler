import configparser
import time
from selenium import webdriver

Config = configparser.ConfigParser()
Config.read('user_info.conf')

id = Config.get('dc', 'id')
pw = Config.get('dc', 'pw')
url = Config.get('dc', 'url')
gall = Config.get('dc', 'gall')
title = Config.get('dc', 'title')
content = Config.get('dc', 'content')


# 리눅스를 위한 가상 디스플레이 드라이버 로드 
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 800))  
#display.start()

# 크롬 환경 변수
options = webdriver.ChromeOptions()
# 화면으로 창을 등장시켜 동작시키지않고 , 렌더링으로 가상으로 동작 시켜줌
options.add_argument('headless')
# 화면 사이즈 조정
options.add_argument('window-size=1920x1080')
# gpu 가속 X
options.add_argument("disable-gpu")


#크롬 드라이버 로드
driver = webdriver.Chrome(executable_path='/Users/landwhale/Desktop/유틸/크롬/chromedriver', chrome_options=options)
driver.implicitly_wait(3)


# 디시인사이드 로그인 페이지 로드
driver.get(url)

# 아이디
driver.find_element_by_name('user_id').send_keys(id)
# 패스워드
driver.find_element_by_name('pw').send_keys(pw)
# 로그인
driver.find_element_by_id('login_ok').click()

# 글을 쓰고자 하는 갤러리로 이동
driver.get(gall)
time.sleep(3)

# 제목 입력을함
driver.find_element_by_name('subject').send_keys(title)


# HTML으로 쓰기 방식 변경
driver.find_element_by_id("tx_switchertoggle").click()
# 1초 기다림
time.sleep(1)

# 글쓰기 폼으로 진입
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))
print(driver.page_source)

#본문 입력
driver.find_element_by_tag_name("body").send_keys(content)

driver.switch_to_default_content()

#글쓰기 저장
time.sleep(3)
driver.find_element_by_xpath("//button[@class='btn_blue btn_svc write']").click()

#저장 딜레이
time.sleep(1)
#웹페이지 닫기
driver.close()

