import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score ,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from sklearn.model_selection import GridSearchCV

print("請等一下")
data = fetch_openml("mnist_784")

print("請等一下")

x, y =np.array(data.data),np.array(data.target)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/7.0)#將data.data和data.target產生資料拆分成訓練及測試二組。
tree =DecisionTreeClassifier(max_depth=5,random_state=10)#設定模式訓練規則 max_depth = 最大深度 random_state=随机状态
tree_params={'max_depth':range(1,15,1)} #用字典方式，設定max_depth的參數，由3次到21次，每次加1。
tree_grid = GridSearchCV(tree, param_grid=tree_params, cv=5 ,n_jobs=-1)
#設定tree_grid模式測試參數，cv:把資料分成5份，4份作訓練、1份作比對，n_jos=-1設定多核CUP運作方式，-1表依機器設定
tree_grid.fit(x_train,y_train) #帶入訓練資料
print(f'Best Params is{tree_grid.best_params_}') #印出測試後的到最佳參數
print(f'Best Score is{tree_grid.best_score_}') #印出測試後的到最佳分數
print(f'accuracy of tree_grid is {accuracy_score(y_test,tree_grid.predict(x_test))}')