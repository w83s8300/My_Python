import requests
import pymysql
import pandas as pd
from bs4 import BeautifulSoup
db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區


#https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E
https="https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E"
page = requests.get(https)#讀取網頁

page=page.text  #把網頁變成text

#soup = BeautifulSoup(page,'html.parser')
soup = BeautifulSoup(page,'lxml')#分析網頁

newTitles=[]
newhref=[]
x = soup.select('div.story-list__text h2 a')#找標題位子
for i in x:
    newTitles.append(i.getText())#取的標題
    newhref.append(i["href"])#取的網址

y = soup.select('time.story-list__time   ')#找時間位子
newTime=[]
#print(x)
for i in y:
    newTime.append(i.getText())#取的時間

newsDatas=[]
for i in range(len(newTitles)):#變成表格
    newsDatas.append({"title":newTitles[i],"link":newhref[i],"date":newTime[i]})


# articleUrl=newsDatas[4]['link']#讀取新的網址
# articlePage=requests.get(articleUrl)讀取新的網頁
# articleSoup = BeautifulSoup(articlePage.text,'lxml')#分析網頁
# x=articleSoup.select('section.article-content__editor > p')#找內文的位子由後往前看

# articleText=""
# for i in x:
#     textP=i.text#讀取內文
#     textP=textP.replace('\n','')
#     articleText+=textP

# articleText=""
# for i in x:
#     if len(i.text)>1:
#         articleText+=i.text


for index,newsData in enumerate(newsDatas):
    #爬取每一則新聞(newsData)連結(articleUrl)內的文章內容(articleText)
    articleUrl=newsData['link']
    articlePage=requests.get(articleUrl)
    articleSoup = BeautifulSoup(articlePage.text,'lxml')
    x=articleSoup.select('section.article-content__editor > p')
    articleText=""
    for i in x:
        if len(i.text)>1:
            articleText+=i.text
    newsDatas[index]['content'] = articleText    
    
    
    #===================================        
    #重複性的檢查，如果標題title已存在資料庫裡，則該則新聞視為重複，不加入資料庫
    sql="select * from news where title='{}'".format(newsData['title'])
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchone()
    if data == None:
        sql="insert into news (title,link,date,content) values ('{}','{}','{}','{}')".\
            format(newsData['title'],newsData['link'],newsData['date'],articleText)
        cursor.execute(sql)
        db.commit()
        print('新增 "{}" 新聞'.format(newsData['title'][:5]))
    else:
        print('該則新聞已存在資料庫裡')
db.close()


