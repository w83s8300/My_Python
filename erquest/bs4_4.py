"""
import requests
import pymysql
import json
from bs4 import BeautifulSoup
import tkinter as tk
db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區
numbers = 2#頁數
key= "新冠肺炎"#名字
for page in range(numbers):
    print(page)
    #https://udn.com/search/word/2/%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E
    https="https://udn.com/api/more?page={}&id=search:{}&channelId=2&type=searchword&last_page=4432".format(page+1, key)
    print(https)
    page = requests.get(https).text  #把網頁變成text
    newsDatas =json.loads(page)#把page的json變字典
    newsDatas = newsDatas['lists']#讀取newsDatas裏的['lists']
    
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
         #重複性的檢查，如果標題title已存在資料庫裡，則該則新聞視為重複，不加入資料庫
        sql="select * from news where title='{}'".format(newsData['title'])
        cursor.execute(sql)
        db.commit()
        data=cursor.fetchone()
        if data == None:
            #爬取每一則新聞(newsData)連結(articleUrl)內的文章內容(articleText)
            articleUrl=newsData['titleLink']
            articlePage=requests.get(articleUrl)
            articleSoup = BeautifulSoup(articlePage.text,'lxml')
            x=articleSoup.select('section.article-content__editor > p')
            articleText=""
            for i in x:
                if len(i.text)>1:
                    articleText+=i.text
            newsDatas[index]['content'] = articleText          
          #===================================   
            sql="insert into news (title,link,date,content) values ('{}','{}','{}','{}')".\
                format(newsData['title'],newsData['titleLink'],newsData['time']['date'],articleText)
            cursor.execute(sql)
            db.commit()
            print('新增 "{}" 新聞'.format(newsData['title'][:5]))
        else:
            print('該則新聞已存在資料庫裡')
    
db.close()
"""
import requests
import pymysql
from bs4 import BeautifulSoup
import json
import tkinter as tk

def udnSearch():
    global keyword
    print(keyword.get())
    numbers=10 #一新聞篇數
    if (numbers%20) !=0:
        pages=(numbers//20)+1 #全部頁數
    else:
        pages=(numbers//20)
        
    for page in range(pages):
        print(page)
        url="https://udn.com/api/more?page={}&id=search:{}&channelId=2&type=searchword&last_page=4432".format(page,keyword.get())
        page=requests.get(url).text
        newsDatas=json.loads(page)['lists']
        
        #放入資料庫
        db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫
        cursor = db.cursor()#cursor是前置緩衝區
        
        for index,newsData in enumerate(newsDatas):
                #重複性的檢查，如果標題title已存在資料庫裡，則該則新聞視為重複，不加入資料庫
            sql="select * from news where title='{}'".format(newsData['title'])
            cursor.execute(sql)
            db.commit()
            data=cursor.fetchone()
            if data == None:
                #爬取每一則新聞(newsData)連結(articleUrl)內的文章內容(articleText)
                articleUrl=newsData['titleLink']
                articlePage=requests.get(articleUrl)
                articleSoup = BeautifulSoup(articlePage.text,'lxml')
                x=articleSoup.select('section.article-content__editor > p')
                articleText=""
                for i in x:
                    if len(i.text)>1:
                        articleText+=i.text
                newsDatas[index]['content']= articleText 
            #===================================        
                sql="insert into news (title,link,date,content) values ('{}','{}','{}','{}')".\
                    format(newsData['title'],newsData['titleLink'],newsData['time']['date'][:10],newsData['content'])
                cursor.execute(sql)
                db.commit()
                print('新增 "{}" 新聞'.format(newsData['title'][:5]))
            else:
                print('該則新聞已存在資料庫裡')
    db.close()

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title('新聞udn搜尋器')
window.geometry('800x600')

tk.Label(window, text='輸入關鍵字',bg="yellow").pack()
keyword=tk.Entry(window)
keyword.pack()

cmd=tk.Button(window, text='執行搜尋', fg='red',bg="green",command=udnSearch)
cmd.pack() #將按鈕顯示於視窗

# 運行主程式
window.mainloop()
   
    
