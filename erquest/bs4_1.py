import requests
import pymysql
import pandas as pd
db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區
from bs4 import BeautifulSoup
#https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E
https="https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E"
page = requests.get(https)#讀取網頁

page=page.text  

#soup = BeautifulSoup(page,'html.parser')
soup = BeautifulSoup(page,'lxml')#分析網頁

newTitles=[]
newhref=[]
x = soup.select('div.story-list__text h2 a')
for i in x:
    newTitles.append(i.getText())
    newhref.append(i["href"])

y = soup.select('time.story-list__time   ')
newTime=[]
#print(x)
for i in y:
    newTime.append(i.getText())

newsDatas=[]
for i in range(len(newTitles)):
    newsDatas.append({"title":newTitles[i],"link":newhref[i],"date":newTime[i]})

for newsData in newsDatas :
    sql = ''' select * 
    from news
    where title="{}"'''.format(newsData['title'])
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchone()

    if data == None:
        sql='''insert 
            into news(title,link,date)
            values ("{}","{}","{}")'''.format(newsData['title'],newsData['link'],newsData['date'])
        cursor.execute(sql)
        db.commit()
    else:
        print("重複")

db.close()   

    





