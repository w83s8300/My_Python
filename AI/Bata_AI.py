import matplotlib.pyplot as plt
import numpy as np
#vvvvvv帶入值
w=[0,0]
w[0]=float(input("w1=(帶入值0.1~0.9):"))
w[1]=float(input("w2=(帶入值0.1~0.9):"))
Theda=float(input("Theda=(帶入值0.1~0.9):"))
a=0.2
plt.axis([-2,2,-2,2])#畫圖的X和Y的直
# vvvvv 判斷 and 或 or
yb=input("輸注 and 或 or 或 xor: ")
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
#================
i=[0,1] #<======= x1
j=[0,1] #<======= x2
x=np.arange(-1,3,0.01)#畫x直的點 
f=1#<========判斷要對4次
g=0#<====呼叫 yb的值
z=1#<=====檢視次數
#vvvvvvvv 帶路直線翻程式
def line(A):#畫y直的點
    return (Theda-(x*w[0]))/w[1]
plt.plot(x,line(x),"g--")#初始虛線
while f<5:#<========判斷要連續對4次
    g=0#<======= yb 重新開始
    for x1 in i:#<======= 變x1的值
        for x2 in j:#<======= 變x2的值
            #vvvvvvv 判斷ya的值
            if (x1*w[0])+(x2*w[1])>=Theda:
                ya=1

            elif (x1*w[0])+(x2*w[1])<Theda:
                ya=0
            #=================
            e=yb[g]-ya#<=========
            g+=1#<==== 變yb的值
            #vvvvvvvv 變w1和w2的值
            if e !=0:
                w[0]=round(w[0]+(a*x1*e),2) # round()小數點後2位
                w[1]=round(w[1]+(a*x2*e),2) # round()小數點後2位
                f=f+1 #<======= 要連續對4次 應為他是錯的重新開始
                print("第{}次".format(z),w[0],w[1])
                #vvvvvvvv 畫w1和w2的值
                plt.plot(x,line(x),"r-")#帶入line(A)>>
                z+=1
                f=1
            #=================
            elif e == 0:
                f=f+1#<======= 對1次加1
print("最後做了第{}次 ".format(z-1),w[0],w[1])
#vvvvvvvv 畫w1和w2的值
plt.plot(x,line(x),"k-")
plt.show()
    