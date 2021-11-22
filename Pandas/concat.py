import pandas as pd

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind]
    for c in cols}
    return pd.DataFrame(data, ind)


x = make_df('AB', [0, 1])#到def make_df(cols, ind):做表格
y = make_df('AB', [4, 5])#到def make_df(cols, ind):做表格
#x.index=['北區','南區'] #把x的index變[北區,南區]
#y.index=['北區','南區']#y的index變[北區,南區]
df1=pd.concat([x, y])#合併X,y
# df1.index=range(1,5)
df2= pd.concat([x,y], ignore_index=True)#把合併X,y的index 造順序排
df3=pd.concat([x, y], keys=['銷售部', '生產部']) #分組 group，多重index

a = make_df('ABC', [1, 2])
b = make_df('BCD', [3, 4, 5])
df7=pd.concat([a, b]) #聯集， 預設值為join='outer'
df8=pd.concat([a, b],join="inner") #交集(a和b都有的知料)


