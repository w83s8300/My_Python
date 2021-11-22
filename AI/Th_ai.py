import matplotlib.pyplot as plt
import numpy as np
w=[0,0]
w[0]=float(input("w1=(帶入值0.1~0.9):"))
w[1]=float(input("w2=(帶入值0.1~0.9):"))
theta=float(input("Theda=(帶入值0.1~0.9):"))
a=0.2
xs=[(0,0),(0,1),(1,0),(1,1)]
yb=[0,0,0,0]
epouch = 0 #最多做幾個循環
training_times = 0 #做了第幾次用
all_correct = 0#連續對4次用
plt.axis([-2,2,-2,2])#畫圖的X和Y的直
x=np.arange(-1,3,0.01)
def line(A):
    return (-A*w[0]+theta)/w[1] #線性方程


yb=input("輸注 and 或 or 或 xor: ")# vvvvv 判斷 and 或 or
if yb == "and":
    yb=[0,0,0,1]
    plt.plot([0,0,1],[0,1,0], 'bo')#下標點
    plt.plot([1],[1], 'ro')#下標點
elif yb == "or":
    yb=[0,1,1,1]
    plt.plot([1,0,1],[0,1,1], 'bo')#下標點
    plt.plot([0],[0], 'ro')#下標點
elif yb == "xor":
    yb=[0,1,1,0] 
    plt.plot([1,0],[0,1], 'bo')#下標點
    plt.plot([0,1],[0,1], 'ro')#下標點
plt.plot(x,line(x),"g--")#初始虛線
while (all_correct < 4 and training_times < 50): #要連續對4次和最多做50個循環
    for i in range(0,4):
        if((xs[i][0]*w[0]+xs[i][1]*w[1]-theta)>=0):
            ya=1
        else:
            ya=0
        e=yb[i]-ya
        if e!=0 :
            training_times +=1#調整次數+1
            all_correct = 0 #要連續對4次，所以歸0
            w[0]=w[0]+a*xs[i][0]*e
            w[1]=w[1]+a*xs[i][1]*e
            print("第{}次".format(training_times),'w1=%4.2f,w2=%4.2f'%(w[0],w[1]))
            plt.plot(x,line(x),"b-")
        else:
            all_correct+=1
print("最後做了第{}次".format(training_times),'w1=%4.2f,w2=%4.2f'%(w[0],w[1]))
plt.plot(x,line(x),"k-")#vvvvvvvv 畫w1和w2的值
plt.show()
