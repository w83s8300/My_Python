import pymysql
import pandas as pd

db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區
"""
sql = '''SELECT * 
    from customers 
    WHERE Name like "張%" '''#讀取特定資料(在Name找張)

cursor.execute(sql)#把新增資料放到資料庫
data = cursor.fetchall()
print(data)
"""
sql = '''SELECT *
    FROM customers
    WHERE EXISTS (SELECT C_Id FROM orders WHERE C_Id = customers.C_Id)'''

cursor.execute(sql)#把新增資料放到資料庫
data = cursor.fetchall()
data = pd.DataFrame(data) 
print(data)

sql = '''SELECT * 
    FROM customers
    WHERE C_Id
    IN (SELECT  C_Id FROM orders)'''

cursor.execute(sql)#把新增資料放到資料庫
data = cursor.fetchall()
data = pd.DataFrame(data) 
print(data)


