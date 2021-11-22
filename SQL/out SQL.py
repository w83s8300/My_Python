#備份
import os
"""
cmd='''C:\\xampp\\mysql\\bin\\mysqldump -u user -puser1234 sql_0 customers orders > D:\\Backup.sql '''
os.system(cmd)
"""
#還原
cmd='''C:\\xampp\\mysql\\bin\\mysqldump -u user -puser1234 sql_0 customers orders < D:\\Backup.sql '''
os.system(cmd)


