#pip install sklearn pydotplus ipywidgets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier

np.random.seed(17)
#rnd = np.random.RandomState(17)
x1 = np.random.normal(size=(100,2))
x2 = np.random.normal(loc=2, size=(100,2))
x = np.vstack((x1,x2))
y1 = np.zeros((100,1))
print(y1.shape)
y2 = np.ones((100,1))
y = np.vstack((y1,y2))
plt.figure(figsize=(12,8))
plt.scatter(x[:,0],x[:,1],c=y,s=50)



tree= DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=17)
print(y.shape)
tree.fit(x,y)
xmin, xmax = x[:,0].min()-1, x[:,0].max()+1
ymin, ymax = x[:,0].min()-1, x[:,0].max()+1
xx ,yy =np.meshgrid(np.linspace(xmin,xmax,1000), np.linspace(ymin,ymax,1000))
yhat = tree.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.figure(figsize=(12,8))
plt.pcolormesh(xx,yy,yhat)
plt.scatter(x[:,0],x[:,1],c=y ,s=50,edgecolors='k')



from io import StringIO
import pydotplus
from sklearn.tree import export_graphviz

dotData = StringIO()
export_graphviz(tree, feature_names=['x','y'],out_file=dotData, filled=True)
img = pydotplus.graph_from_dot_data(dotData.getvalue())

from ipywidgets import Image
Image(value=img.create_png())


plt.show()

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracyscore

rnd = np.random.RandomState(17) #產生亂數表rnd
Data = np.r[rnd.normal(size=(1000,2)),rnd.normal(loc=2,size=(1000,2))] # 產生測試用數值
labels = np.r_[np.zeros(1000),np.ones(1000)]

x_train,x_test,y_train,y_test = train_test_split(Data,labels,test_size=0.3) #將上述產生資料拆分成訓練及測試二組。

tree=DecisionTreeClassifier(max_depth=5,random_state=7) #設定模式訓練規則
tree.fit(x_train,y_train) #帶入訓練資料

y_hat=tree.predict(x_test) #帶入測試資料做驗算，用x_test作出來的Y值(y_hat)和(y_test)比對

from sklearn.metrics import accuracy_score

print(f'accuracy of decision tree width max_depth=5 is {accuracy_score(y_test,y_hat)}') #印出結果 


