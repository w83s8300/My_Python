import pymysql 
import pandas as pd
#print(pymysql.__version__)
#CREATE USER 'user'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `user`;GRANT ALL PRIVILEGES ON `user`.* TO 'user'@'localhost';GRANT ALL PRIVILEGES ON `user\_%`.* TO 'user'@'localhost';

db = pymysql.connect(host="127.0.0.1", 
                     user="user",
                     passwd="user1234",
                     database="cocotree")#連接資料庫

cursr = db.cursor()#cursor是前置緩衝區
cursor = db.cursor()
#資料庫四個動作CRUD：新增資料（Create),讀區/收尋資料（Read),更新資料（Update),刪除資料（Delete)
#資料庫四個動作(for SQL)：新增資料（Insert),讀區/收尋資料（Select),更新資料（Update),刪除資料（Delete)



# #新增資料(Insert)
# sql='''insert 
#     into member (name,tel,addr,age) 
#     values ('Se','024','台中','29')'''
# cursr.execute(sql)#把新增資料放到資料庫
# db.commit()##把新增資料放到資料庫

# sql='''insert 
#     into member (name,tel,addr,age) 
#     values ('Ga','09','台北','32')'''
# cursr.execute(sql)#把新增資料放到資料庫
# db.commit()##把新增資料放到資料庫

# #更新資料(Update)
# sql='''Update 
#     member set age="30" 
#     where addr="台中"'''
#     #where<===要修改的資料位子
# cursr.execute(sql)#把新增資料放到資料庫
# db.commit()##把新增資料放到資料庫


#刪除資料(Delete)
sql='''Delete 
    from  students'''
cursr.execute(sql)#把新增資料放到資料庫
db.commit()##把新增資料放到資料庫


# #讀取資料
# sql='''SELECT * 
#     from member 
#     order by age '''
# cursr.execute(sql)#把新增資料放到資料庫
# data = cursr.fetchall()
# c = pd.DataFrame(data) #<========把data變成pd額的表格
# print(c)

# #讀取資料移除重複向
# sql='''select DISTINCT id
#     from member''' #預設值為 由小排到大
# cursor.execute(sql)
# db.commit()
# data=cursor.fetchall()
# c = pd.DataFrame(data) 
# print(c)

# #讀取資料
# sql='''SELECT * 
#     from member 
#     order by age '''
# cursr.execute(sql)#把新增資料放到資料庫
# data = cursr.fetchall()
# c = pd.DataFrame(data) #<========把data變成pd額的表格
# print(c)





db.close()#關閉連接

