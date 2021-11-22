import matplotlib.pyplot as plt
import numpy as np
w=[0,0]
w[0]=float(input("w1=(帶入值0.1~0.9):"))
w[1]=float(input("w2=(帶入值0.1~0.9):"))
Theda=float(input("Theda=(帶入值0.1~0.9):"))
a=0.2
plt.axis([-2,2,-2,2])#畫圖的X和Y的直
yb=input("輸注 and 或 or 或 xor: ")# vvvvv 判斷 and 或 or
if yb == "and":
    yb=[0,0,0,1]
    plt.plot([0,0,1],[0,1,0], 'bo')#
    plt.plot([1],[1], 'ro')#
elif yb == "or":
    yb=[0,1,1,1]
    plt.plot([1,0,1],[0,1,1], 'bo')#
    plt.plot([0],[0], 'ro')#
elif yb == "xor":
    yb=[0,1,1,0] 
    plt.plot([1,0],[0,1], 'bo')#
    plt.plot([0,1],[0,1], 'ro')#
x=np.arange(-1,3,0.01)#畫x直的點
xs=[(0,0),(0,1),(1,0),(1,1)] 
f=1#<========判斷要對4次
f1=1#<========做50個循環
def line(A):#畫y直的點
    return (Theda-(x*w[0]))/w[1]#<========帶路直線翻程式
plt.plot(x,line(x),"g--")#初始虛線
while(f < 4 and f1 < 50):#<========判斷要連續對4次
    for i in range(0,4):#
            #vvvvvvv 判斷ya的值
            if (xs[i][0]*w[0])+(xs[i][1]*w[1])>=Theda:
                ya=1
            elif (xs[i][0]*w[0]+xs[i][1]*w[1])<Theda:
                ya=0
            e=yb[i]-ya#<=========
            if e !=0:#vvvvvvvv 變w1和w2的值
                w[0]=round(w[0]+(a*xs[i][0]*e),2) # round()小數點後2位
                w[1]=round(w[1]+(a*xs[i][1]*e),2) # round()小數點後2位
                print("第{}次".format(f1),w[0],w[1])
                plt.plot(x,line(x),"r-")#帶入line(A)>> 畫w1和w2的值
                f=1 #<======= 要連續對4次 應為他是錯的重新開始
                f1+=1
            elif e == 0:
                f=f+1#<======= 對1次加1
print("最後做了第{}次 ".format(f1-1),w[0],w[1])
plt.plot(x,line(x),"k-")#======= 畫w1和w2的值
plt.show()
    