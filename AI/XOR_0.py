import math
import matplotlib.pyplot as plt
import random
import numpy as np
w13=random.random()
w14=random.random()
w23=random.random()
w24=random.random()
w35=random.random()
w45=random.random()
Theta3=random.random()
Theta4=random.random()
Theta5=random.random()

print("w13的值=%.4f"%(w13))
print("w14的值=%.4f"%(w14))
print("w23的值=%.4f"%(w23))
print("w24的值=%.4f"%(w24))
print("w35的值=%.4f"%(w35))
print("w45的值=%.4f"%(w45))
print("Theta3的值=%.4f"%(Theta3))
print("Theta4的值=%.4f"%(Theta4))
print("Theta5的值=%.4f"%(Theta5))

mde=0.01

# w13=0.5
# w14=0.9
# w23=0.4
# w24=1.0
# w35=-1.2
# w45=1.1
# Theta3=0.8
# Theta4=-0.1
# Theta5=0.3
# mde=0.01

w=[]
for i in range(6):
    w.append(i)

training_times = 1 #做了第幾次用
epouch =0#循環第幾次用
all_correct = 0#連續對4次用
yb=[0,1,1,0]#之後寫程式用
xs=[(0,0,0.0),(0.0,1.0),(1.0,0.0),(1.0,1.0)]#之後寫程式用
a=0.1
y3=0
y4=0
y5=0


#簡化用
# w=[w13,w23,w14,w24,w35,w45]
# ya=[y3,y4,y5]#y3 y4 y5
# theta=[Theta3,Theta4,Theta5]
# mde= [mde]
#=============


plt.plot([1,0],[0,1], 'bo')#下標點
plt.plot([0,1],[0,1], 'ro')#下標點
x=np.arange(-1,3,0.01)

def line1(A):
    return (-A*w13+Theta3)/w23 #線性方程
def line2(A):
    return (-A*w14+Theta4)/w24 #線性方程    
def axis(A):
    return 0*A #線性方程
plt.plot(x,line1(x),"c--")#初始虛線
plt.plot(x,line2(x),"g--")#初始虛線
plt.plot(x,axis(x),"k-")#初始虛線
plt.plot(axis(x),x,"k-")#初始虛線

SE = 0.0
Accuracy = 0.0
MSE = 1.0
Accuracy=eval(input("Accuracy:0.01~0.0001:"))#將輸入值轉成evaluable
epouch_end=(eval(input("最多做幾次個循環:")))
MSElist=[]#畫弧線的

while (MSE > Accuracy and epouch < epouch_end): #要連續對4次和最多做50個循環
    SE = 0.0#初始SE
    epouch +=1
    print("第{}次".format(training_times))
    for i in range(0,4):
        y3=1/(1+math.exp(-(xs[i][0]*w13+xs[i][1]*w23-Theta3)))#exp是把它變弧線 
        #x=xs[i][0]*w14+xs[i][1]*w24-Theta4#<他是直線
        y4=1/(1+math.exp(-(xs[i][0]*w14+xs[i][1]*w24-Theta4)))#exp是把它變弧線 
        #x=y3*w35+y4*w45-Theta5#用y3和y4算直線
        y5=1/(1+math.exp(-(y3*w35+y4*w45-Theta5)))#算y5
        e=yb[i]-y5#用y5求e e是誤差值 yb看圖二 應為 x1是1 x2是1 所以 yb是0
        #==============
        rTheta5=y5*(1-y5)*e#把y5帶入改變值求新的Theta5 把新的Theta5命名成rTheta5
        rw35=a*y3*rTheta5#用Theta5求新的w35的差值
        rw45=a*y4*rTheta5#用Theta5求新的w45的差值
        rTheta3=y3*(1-y3)*(rTheta5)*w35#用原w35的值求新的Theta3的值 把新的Theta3命名成rTheta3  
        rTheta4=y4*(1-y4)*(rTheta5)*w45#用原w45的值求新的Theta4的值 把新的Theta4命名成rTheta4
        w35=rw35+w35#用w35的差值 求新的w35的值
        w45=rw45+w45#用w45的差值 求新的w45的值
        #==============
        rw13=a*xs[i][0]*rTheta3#用Theta3求新的w13的差值
        rw23=a*xs[i][1]*rTheta3#用新的Theta3求新的w23的差值
        rw14=a*xs[i][0]*rTheta4#用新的Theta4求新的w14的差值
        rw24=a*xs[i][1]*rTheta4#用新的Theta4求新的w24的差值
        #==========================
        w13=rw13+w13#用w13的差值 求新的w13的值
        w23=rw23+w23#用w23的差值 求新的w23的值
        w14=rw14+w14#用w13的差值 求新的w13的值
        w24=rw24+w24#用w23的差值 求新的w23的值
        #===========================
        rTheta5=a*(-1)*rTheta5#用新的Theta5的差值
        rTheta4=a*(-1)*rTheta4#用新的Theta4的差值
        rTheta3=a*(-1)*rTheta3#用新的Theta3的差值
        Theta5=Theta5+rTheta5#用原Theta5的值 求新的Theta5的值
        Theta4=Theta4+rTheta4#用原Theta4的值 求新的Theta4的值
        Theta3=Theta3+rTheta3#用原Theta3的值 求新的Theta3的值
        SE+=e*e#誤差
        #==================================
        print("y3=",y3,"y4=",y4,"y5=",y5)
        
    training_times+=1
    print("MSE的值=%.4f"%(MSE))
    print("=====================") 
    MSE=SE/4.0#要平均誤差所以/4 
    MSElist.append(MSE)#畫弧線的


plt.plot(x,line1(x),"c-")#初始虛線
plt.plot(x,line2(x),"g-")#初始虛線

print("第{}次".format(training_times))
print("=====================")
print("w13的值=%.4f"%(w13))
print("w14的值=%.4f"%(w14))
print("w23的值=%.4f"%(w23))
print("w24的值=%.4f"%(w24))
print("w35的值=%.4f"%(w35))
print("w45的值=%.4f"%(w45))
print("Theta3的值=%.4f"%(Theta3))
print("Theta4的值=%.4f"%(Theta4))
print("Theta5的值=%.4f"%(Theta5))
print("=====================") 

plt.show()


plt.plot((range(epouch)),MSElist)#畫弧線的
plt.show()

