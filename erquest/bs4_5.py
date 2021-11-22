import requests
import pymysql
import json
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/Gossiping/index.html"
headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
        }#自定義直(網頁的headers
Cookies={'over18':'1',}#自定義直(網頁的Cookies

page=requests.get(url,headers=headers,cookies=Cookies)#帶入自定義直
doc = page.text

page = requests.get(url,headers=headers,cookies=Cookies).text  #把網頁變成text
soup = BeautifulSoup(page,'lxml')
title = soup.select('div.title>a')

author = soup.select('div.meta>div.author')
pttData = []

for i in range(len(title)):
        print(title[i].text,author[i].text)
        
for i in range(len(title)):
    pttData.append({"title":title[i].text,"author":author[i].text})
    print(pttData)


