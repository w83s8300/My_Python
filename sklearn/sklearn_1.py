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

plt.show()