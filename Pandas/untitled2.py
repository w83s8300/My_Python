import pandas as pd
import numpy as np
data = pd.read_excel(r"C:\python\110.xlsx")


for i in range(len(data.columns)-1,18,-1):
    data1=data.drop(columns=[data.columns[i]],axis=1)

name_index=[4,6,8,10,12,14,16,18]
names=[np.nan]
#讀取名字
row , col =data.shape
for i in range(2,row):
    for j in name_index:
        if data.iloc[i,j] not in names:
            print(("i=",i,"j=",j,data.iloc[i,j]))
        



'''
x= pd.DataFrame([[1, np.nan,2],[2,3,4],[np.nan,5,6]])

df2=x.dropna()
df3=x.dropna(axis=1)

df4 = x.fillna(0)
'''

                   
                   