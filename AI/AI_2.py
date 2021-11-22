import math
import matplotlib.pyplot as plt
import random
import numpy as np


w=[]
for i in range(16):
    w.append(0)

theta=[]
for i in range(2):
    theta.append(0)

ya=[]
for i in range(2):
    ya.append(0)

training_times = 1 #做了第幾次用
epouch =0#循環第幾次用
all_correct = 0#連續對4次用
yb=[0,1,1,0]#之後寫程式用
xs=[(0,0,0.0),(0.0,1.0),(1.0,0.0),(1.0,1.0)]#之後寫程式用
a=0.1

SE = 0.0
Accuracy = 0.0
MSE = 1.0
Accuracy=eval(input("Accuracy:0.01~0.0001:"))#將輸入值轉成evaluable
epouch_end=(eval(input("最多做幾次個循環:")))

    
