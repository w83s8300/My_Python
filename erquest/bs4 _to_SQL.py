import pymysql
import pandas as pd


db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區
"""
#============== 創建 新聞資料news 表單 ==================================
sql = "CREATE TABLE IF NOT EXISTS news ( id int AUTO_INCREMENT, \
 	                            title varchar(500),\
                                link varchar(500),\
                                date date,\
                                content varchar(1000),\
                                primary key (id) )"
"""
 
 
sql="delete from news"
 
cursor.execute(sql)
db.commit()




