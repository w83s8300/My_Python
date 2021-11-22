import requests
from bs4 import BeautifulSoup
#https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E
https="https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E"
page = requests.get(https)#讀取網頁

page=page.text  

#soup = BeautifulSoup(page,'html.parser')
soup = BeautifulSoup(page,'lxml')#分析網頁

x=soup.find_all('a')#找所有的a標籤
print(x[:5])
for i in range(5):
    print(x[i].getText())