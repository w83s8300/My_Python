
from selenium.webdriver.chrome.options import Options

#自動化不跑表頭(瀏覽器不開啟)
options=Options()
options.add_argument("--no-sandbox")
options.add_argument("headless");
#options.add_argument("--proxy-server=http://aa.bb.cc:8008") #無痕模式

import time

# =============================================================================
# #web分享
# [開網頁]
# browser.get('https://www.google.com/')
# [option的方法,加一個逗號再放進參數]
# browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
# =============================================================================

from selenium import webdriver

browser=webdriver.Chrome(options=options) #options不跑表頭(瀏覽器不開啟)
#browser.set_window_size(400,900)   #瀏覽器顯示大小
browser.set_window_position(1000,0) #瀏覽器自動顯示於視窗哪個位置
browser.maximize_window()           #瀏覽器顯示最大
browser.implicitly_wait(20)         #強制20秒或資料收集完即換頁(很重要！)
#一律用get(沒有post)
browser.get('http://www.dic.mdu.edu.tw/front/Members/teachers/member.php?ID=bWR1X2RpYyZ0ZWFjaGVycw==')  
html=browser.page_source

# =============================================================================
# #欲開啟多個瀏覽器另設browser即可
# browser1=webdriver.Chrome(ChromeDriverManager().install())
# browser1.set_window_size(400,900)   #網頁顯示大小
# browser1.set_window_position(500,0) #自動顯示於視窗哪個位置
# #一律用get(沒有post)
# browser1.get('http://www.dic.mdu.edu.tw/front/Members/teachers/member.php?ID=bWR1X2RpYyZ0ZWFjaGVycw==')  
# html=browser1.page_source
# =============================================================================

from bs4 import BeautifulSoup  #抓資料
soup=BeautifulSoup(html,'lxml')
teacher=soup.select("h3.member-name>a")
for i in teacher:
    print(i.text)

time.sleep(5)   #休息五秒鐘
browser.close() #自動關閉瀏覽器