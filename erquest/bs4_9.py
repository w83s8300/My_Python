from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--no-sandbox") #bypass OS security model
#options.add_argument("headless")
import time
from selenium import webdriver
from bs4 import BeautifulSoup


browser=webdriver.Chrome(options=options)
browser.set_window_size(400,900)
browser.implicitly_wait(20)
product=[]#建空的表之後要放資料
pageidx=3
for page in range(pageidx):
    url="https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone%2013&searchType=1&curPage={}&_isFuzzy=0&showType=chessboardType".format(page)#讀取網頁
    browser.get(url)#讀取網頁
    html=browser.page_source
    soup = BeautifulSoup(html,'lxml')#分析網頁
    pName=soup.select("div.listArea>ul h3")#找把位子
    pPrice=soup.select("div.listArea>ul span.price b")#找價錢位子
    for i in range(len(pPrice)):
        product.append((pName[i].text,int(pPrice[i].text.replace(',',''))))#標題和價錢變list .replace(',','')是把價錢28,889變28889 int是把文字變數字
    
time.sleep(2) 
browser.close()



# 課本 7-9 和7-13
