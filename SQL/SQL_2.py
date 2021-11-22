import pymysql
import pandas as pd


db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="mdu")#連接資料庫
cursor = db.cursor()#cursor是前置緩衝區
"""
sql = '''select *
    from member
    where name like "%a%"'''

cursor.execute(sql)#把新增資料放到資料庫
data = cursor.fetchall()
db.commit()
data = pd.DataFrame(data)
print(data)

#合併
sql = '''select*
    from table1'''
"""
"""
#============== 創建 customers 表單 ==================================
sql = "CREATE TABLE IF NOT EXISTS customers1 ( C_Id int AUTO_INCREMENT, \
                              Name varchar(20),\
                                City varchar(20),\
                                address varchar(50),\
                                Phone varchar(20),\
                                  primary key (C_Id) )"

cursor.execute(sql)
db.commit()
#============== 創建 customers 表單 ==================================
sql = "CREATE TABLE IF NOT EXISTS orders ( O_Id int AUTO_INCREMENT, \
                              Order_No int,\
                                C_Id int,\
                                primary key (O_Id) )"

#FOREIGN KEY<====連結複數的KEY
sql = "CREATE TABLE IF NOT EXISTS orders ( O_Id int AUTO_INCREMENT, \
                              Order_No int,\
                                C_Id int,\
                                primary key (O_Id) \
                                FOREIGN KEY(Order_No) REFRENCES customers(O_Id))"#<====Order_No是customers的O_Id




"""
# #INNER JOIN 把表單合併 customers合併orders 用C_Id當KEY
# sql = '''SELECT *
#     FROM customers
#     INNER JOIN orders
#     ON customers.C_Id=orders.C_Id'''


#============== 創建 留言板msgboard 表單 ==================================
import pymysql

db = pymysql.connect(host="127.0.0.1", user="user",\
      passwd="user1234",database="mdu",charset='utf8')
cursor = db.cursor() 

# sql = "CREATE TABLE IF NOT EXISTS msgboard ( id int AUTO_INCREMENT, \
#                                 mid int ,\
#                                   seq int,\
#                                   author varchar(20),\
#                                   content varchar(1000),\
#                                   tag varchar(100),\
#                                   time datetime,\
#                                   primary key (id) )"
    
sql ='''  
ALTER TABLE msgboard
ADD COLUMN title varchar(35);
'''

# sql = "CREATE TABLE IF NOT EXISTS sys_parameter ( mid int ,\
#                                 primary key (mid) )"


cursor.execute(sql)
db.commit()
# data=cursor.fetchall()
# print(data)
db.close()