import pandas as pd
import numpy as np

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind]
    for c in cols}
    return pd.DataFrame(data, ind)

df1 = make_df('ABC', [1, 2 ,3])
df2 = make_df('BCD', [3, 4 ,5])
df3=pd.concat([df1, df2])
df4=df3.drop('B',axis=1)
#=======================
x=np.array([[3,5,2],[4,5,6],[2,8,9]])

#df9=df8.drop(columns=['x'],axis=1)  #指定刪除的key欄位
z=pd.DataFrame(x) #z 是一個表格資料
z['d']=0 #新增一欄 'd' 是key
z=z.append({}, ignore_index=True) #新增一列
z.index=[1,2,3,'欄位總和']
z.columns=[1,2,3,'平均']
height,width=z.shape
rowSum=0
for i in range(height):
    for j in range(3):
        rowSum+=z.iloc[i,j]
    rowAve=rowSum/3
    z.iloc[i,3]=rowAve
    rowSum=0
   
colSum=0
for i in range(height):
    for j in range((width-1)):
        colSum+=z.iloc[j,i]
    z.iloc[(j+1),i]=colSum
    colSum=0
        
        
        # print(z.iloc[i,j])

# print(z.iloc[2,1])
# print(z.iloc[1:,:])
# print(z['A']) #文字欄
# print(z.loc['a']) #文字列
#pyhon、numpy list or dic 轉 dataframe
#=============

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = x[0:, 1:]



z = pd.DataFrame(x)
z.index = ["a","b","c"]
z.columns = ["A","B","C"]

z['d'] = 0
z = z.reindex(columns=[0,1,2,'D'],fill_value=0)

'''
a = z.values
a=a**(1/2)*10
z = pd.DataFrame(a)
'''
z.index = ["a","b","c"]
z.columns = ["A","B","C"]





print(z)




