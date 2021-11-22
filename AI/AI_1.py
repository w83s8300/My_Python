import math
w13=0.5
w14=0.9
w23=0.4
w24=1.0
w35=-1.2
w45=1.1
Theta3=0.8
Theta4=-0.1
Theta5=0.3
yb=[0,1,1,0]#之後寫程式用
xs=[(0,0),(0,1),(1,0),(1,1)]#之後寫程式用
a=0.1

x1=1
x2=1
#p.2判斷值
#x1w13+x2w23-Theda3
x=x1*w13+x2*w23-Theta3#<他是直線
y3=1/(1+math.exp(-x))#exp是把x變弧線 
print("y3=",y3)

x=x1*w14+x2*w24-Theta4#<他是直線
y4=1/(1+math.exp(-x))#exp是把x變弧線
print("y4=",y4)

#y3w35+y4w45-Theda5
x=y3*w35+y4*w45-Theta5#用y3和y4算直線
y5=1/(1+math.exp(-x))#算y5
print("y5=",y5)

e=yb[3]-y5#用y5求e e是誤差值 yb看圖二 應為 x1是1 x2是1 所以 yb是0
print("e=",e)
#p.3改變值
#y5*(1-y5)*e=Theta5
rTheta5=y5*(1-y5)*e#把y5帶入改變值求新的Theta5 把新的Theta5命名成rTheta5
print("Theta5=%.4f"%(Theta5))
rw35=a*y3*rTheta5#用Theta5求新的w35的差值
rw45=a*y4*rTheta5#用Theta5求新的w45的差值
print("w35的差值=%.4f"%(rw35))
print("w45的差值=%.4f"%(rw45))

rTheta3=y3*(1-y3)*(rTheta5)*w35#用原w35的值求新的Theta3的值 把新的Theta3命名成rTheta3
#print(Theta3,"=",y3,"*(1-",y3,")*(",Theta5,"*",w35)
rTheta4=y4*(1-y4)*(rTheta5)*w45#用原w45的值求新的Theta4的值 把新的Theta4命名成rTheta4
print("Theta3=%.4f"%(rTheta3))
print("Theta4=%.4f"%(rTheta4))
w35=rw35+w35#用w35的差值 求新的w35的值
w45=rw45+w45#用w45的差值 求新的w45的值
print("w35的值=%.4f"%(w35))
print("w45的值=%.4f"%(w45))
#==============
rw13=a*x1*rTheta3#用Theta3求新的w13的差值
#print(rw13,"=",a,"*",x1,"*",Theta3)#用新的Theta3求新的w13的差值
rw23=a*x2*rTheta3#用新的Theta3求新的w23的差值
print("w13的差值=%.4f"%(rw13))
print("w23的差值=%.4f"%(rw23))

rw14=a*x1*rTheta4#用新的Theta4求新的w14的差值
#print(rw13,"=",a,"*",x1,"*",Theta3)#用新的Theta4求新的w14的差值
rw24=a*x2*rTheta4#用新的Theta4求新的w24的差值
print("w14的差值=%.4f"%(rw14))
print("w24的差值=%.4f"%(rw24))

#==========================
w13=rw13+w13#用w13的差值 求新的w13的值
w23=rw23+w23#用w23的差值 求新的w23的值

print("w13的值=%.4f"%(w13))
print("w23的值=%.4f"%(w23))

w14=rw14+w14#用w13的差值 求新的w13的值
w24=rw24+w24#用w23的差值 求新的w23的值

print("w14的值=%.4f"%(w14))
print("w24的值=%.4f"%(w24))

#===========================
rTheta5=a*(-1)*rTheta5#用新的Theta5的差值
print("Theta5的差值%.4f"%(rTheta5))
rTheta4=a*(-1)*rTheta4#用新的Theta4的差值
print("Theta4的差值%.4f"%(rTheta4))
rTheta3=a*(-1)*rTheta3#用新的Theta3的差值
print("Theta3的差值%.4f"%(rTheta3))

#print(Theta5,"=",Theta5,"+",rTheta5)#用原Theta5的值 求新的Theta5的值
Theta5=Theta5+rTheta5#用原Theta5的值 求新的Theta5的值
Theta4=Theta4+rTheta4#用原Theta4的值 求新的Theta4的值
Theta3=Theta3+rTheta3#用原Theta3的值 求新的Theta3的值

#==================================
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