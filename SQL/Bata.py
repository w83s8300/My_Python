import pymysql 
import pandas as pd

db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="sql_0")#連接資料庫

cursor = db.cursor()#cursor是前置緩衝區
data=pd.read_excel(r"C:\python\SQL\人事資料.xlsx")

height,width=data.shape
for i in range(height):
    sql='''insert into 
    member (id,name,tel,addr,age)             
    values ("{}","{}","{}","{}",{})'''.format(data.iloc[i,0],\
        data.iloc[i,1],data.iloc[i,2],data.iloc[i,3],\
        data.iloc[i,4])
    cursor.execute(sql)#把新增資料放到資料庫
    db.commit()

db.close()#關閉連接





        
