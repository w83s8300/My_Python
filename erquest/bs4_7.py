import requests
from bs4 import BeautifulSoup
import pandas as pd

https="https://histock.tw/stock/2330"
page = requests.get(https)#讀取網頁
page=page.text  #把網頁變成text
soup = BeautifulSoup(page,'lxml')#分析網頁

"""
Data = soup.select('table#block20_ctl00_gBuy tr th')
Datacol=[]
for i in Data:
    Datacol.append(i.text)
Data = soup.select('div.LBlock_8  table#block20_ctl00_gBuy  tr td')
index=0
Dataname=[]
tmp=[]
for i in Data:
    if (index%6)==0:
        Dataname.append(tmp)
        tmp=[index//6+1]
        pass
    else:
        tmp.append(i.text)
        
    index+=1      
Dataname.append(tmp)
Dataname=Dataname[1:]
"""
#使用pandas來整理網頁全表格資料
data=soup.select("table.tb-stock.tbChip")
BPScore=pd.read_html(str(data))
"""
for i in range(10):
    BPScore.iloc[i,0]=i+1
    """
