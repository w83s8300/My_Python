#ๅไปฝ
import os
"""
cmd='''C:\\xampp\\mysql\\bin\\mysqldump -u user -puser1234 sql_0 customers orders > D:\\Backup.sql '''
os.system(cmd)
"""
#้ๅ
cmd='''C:\\xampp\\mysql\\bin\\mysqldump -u user -puser1234 sql_0 customers orders < D:\\Backup.sql '''
os.system(cmd)


