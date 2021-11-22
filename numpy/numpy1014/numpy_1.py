# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# #基本運算

# %%
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print(a)
print(a[0])
print(type(a))
print(type(a[0]))
c = a + b
print(c)
d = [x+y for x, y in zip(a,b)]
print(d)


# %%
import numpy as np
x1 = np.array([1, 3, 5, 7])
x2 = np.array(b)
print(x2)
print(type(x2))
x3 = x1 ** x2
print(x3)

# %% [markdown]
# np.array 陣列的產生
# int8, int16, int32, int64 整數bits數
# float16, float32, float64
# uint8, uint16, uint32, uint64 正整數
# np.linspace(start, stop, num=50)

# %%
a = np.array((0,1,2,3,4,5,6,7,8,9))
b = np.arange(0,10,3) #np.arange(start=0,stop,step=1)
print(b)
c = np.arange(0.1, 10, 1.1)
d = np.array([1, 2.1, 3, 4, 5])
print(d)
e = np.array([1, 2.1, 3, 4, 5],dtype=np.int8)
print(e)
print(e.shape)
f = np.linspace(0,10,11)
print(f)
g = np.linspace(0,10)
print(g)
h = np.arange(10)
print(h)

# %% [markdown]
# 2D ndarray #維度, 陣列的大小, 第0軸的維度大小是2, 第1軸的維度大小是3@
# 

# %%
a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
print(a.shape)

b = np.arange(0,12).reshape((3,4)) #重塑,把原始的陣列轉換成3x4的2D陣列
print(b)
b = np.arange(0,15).reshape((-1,5)) #某一個維度值可以給-1,讓系統自動算
c = np.random.randint(1,10,size=(3,4)) #randint(start,stop,size=(a,b))
print(c)                               #產生axb的2D陣列，裡面的值是介於start和stop之間的整數
d = np.random.rand(2,3) #產生2x3的2D陣列,裡面的值是介於0到1的亂數
print(d)
e = np.random.randn(2,3) #產生2x3的2D陣列,裡面的值是服從標準常態分佈的亂數
print(e)
f = np.zeros((2,3)) #產生全部為0的2x3的2D陣列
print(f)
g = np.zeros_like(c) #產生和陣列c一樣大小的2D陣列
print(g)
h = np.ones((2,3)) #產生全部為1的2x3的2D陣列
print(h)

# %% [markdown]
# 基本運算/軸的觀念
# np.sum(array,axis=?) #依axis=?的值,對陣列作加總

# %%
#np.random.seed(10)
a = np.random.randint(10,size=(3,4))
print(a)
sumA = np.sum(a) #沒有給axis的參數,則對陣列a的所有元素作加總
print(sumA)
sumA2 = a.sum() #直接用實體物作a呼叫sum函數作加總運算
print(sumA2)
sumAxis0 = np.sum(a, axis=0) #依第0軸的方向作加總
print(sumAxis0)


