import pandas as pd

import numpy as np
x=np.array([[3,5,2],[4,5,6],[2,8,9]])


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
    
    
    
        # print(z.iloc[i,j])

# print(z.iloc[2,1])
# print(z.iloc[1:,:])
# print(z['A']) #文字欄
# print(z.loc['a']) #文字列
#pyhon、numpy list or dic 轉 dataframe