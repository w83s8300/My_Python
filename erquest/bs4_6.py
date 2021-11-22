import requests
import pymysql
import json
from bs4 import BeautifulSoup
import re


url="https://www.cwb.gov.tw/Data/js/week/ChartData_Week_County_C.js?T=2021110209-0&_=1635815086433"#<<<<<把你要爬的網址放在這
page=requests.get(url)#帶入自定義直
doc = page.text

pattan=r":\{'C':\{'H':\[(.*?)\],'L':\["
High=re.findall(pattan,doc)
pattan=r"'L':\[(.*?)\]\},'F'"
Low=re.findall(pattan,doc)
pattan=r'''\]\]\},
    '(.*?)':\{'C':'''
citySn=re.findall(pattan, doc)
citySn.insert(0,"10017")


https="https://www.cwb.gov.tw/V8/C/ajax/_header.html?v=20211027"
page = requests.get(https)#讀取網頁
page=page.text  #把網頁變成text
soup = BeautifulSoup(page,'lxml')#分析網頁
cityLists = soup.select('form#megacity>section.col-xs-12>label.select>select>option')[2:-1]#找標題位子  符號>是指AAA>BBB只AAA下一個一定要是BBB
cityLists1 = soup.select('#megacity label>select>option')[2:-1]#找標題位子
print((cityLists))
cityList=[]
for city in cityLists1:
    cityList.append([city['value'],city.text])
    
    

    

    
    
    
    