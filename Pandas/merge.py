import pandas as pd


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
        'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2)#由列合併


df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
'supervisor': ['Carly', 'Guido', 'Steve']})
df5=pd.merge(df3, df4)
df6=pd.DataFrame({'group': ['Accounting', 'Accounting',
'Engineering', 'Engineering', 'HR', 'HR'],
'skills': ['math', 'spreadsheets', 'coding', 'linux',
'spreadsheets', 'organization']})
df7=pd.merge(df1, df6)

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'name': ['Lisa', 'Bob', 'Jake', 'Sue'],
        'hire_date': [2004, 2008, 2012, 2014]})
df8 = pd.merge(df1, df2, left_on="employee", right_on="name")#指定欄位合併
df9=df8.drop(columns=['name'],axis=1)  #指定刪除的key欄位

df10 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
          'food': ['fish', 'beans', 'bread']},columns=['name', 'food'])
df11 = pd.DataFrame({'name': ['Mary', 'Joseph'],
            'drink': ['wine', 'beer']},columns=['name', 'drink'])
df12=pd.merge(df10, df11, how='inner') #預設為交集(a和b都要有的知料) how='inner'，與concat相反
df13=pd.merge(df10, df11, how='outer')#聯集
df14=pd.merge(df10, df11, how='left')#看左邊的資料(df10)
df15=pd.merge(df10, df11, how='right')#看右邊的資料(df11)


#============ group by ===================
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
'data1': range(6),'data2':[2,4,7,2,3,5]},columns = ['key', 'data1', 'data2'])
df1=df.groupby(df['key']).sum() #'key' 是欄位名稱