import requests
import pymysql
import json
from bs4 import BeautifulSoup

url="https://www.cwb.gov.tw/Data/js/week/ChartData_Week_County_C.js?T=2021102916-3&_=1635496669467"
headers={
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
        }#自定義直(網頁的headers
Cookies={'over18':'1',}#自定義直(網頁的Cookies

page=requests.get(url,headers=headers,cookies=Cookies)#帶入自定義直
doc = page.text

page = requests.get(url,headers=headers,cookies=Cookies).text  #把網頁變成text