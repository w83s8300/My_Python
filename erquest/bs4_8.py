from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("headless")

import time

from selenium import webdriver
"""
browser=webdriver.Chrome(options=options)
# browser.set_window_size(400,900)
browser.set_window_position(1100,0)
browser.maximize_window()
browser.implicitly_wait(20)
browser.get("http://www.dic.mdu.edu.tw/front/Members/teachers/member.php?ID=bWR1X2RpYyZ0ZWFjaGVycw==")

html=browser.page_source

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
teacher=soup.select("h3.member-name > a")
pttData = []
for i in teacher:
    print(i.text)
    pttData.append(i.text)

browser.close()
"""
browser=webdriver.Chrome(options=options)
browser.set_window_size(400,900)
browser.implicitly_wait(20)
url="https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone%2013&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType"
browser.get(url)

html=browser.page_source
browser.implicitly_wait(20) 
#browser.find_element_by_name("identifier").send_keys("w83s83")
#browser.find_elements_by_link_text("111學年度碩士班招生考試入學簡章").click()

time.sleep(5)   #休息五秒鐘
browser.close()

