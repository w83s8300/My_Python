import matplotlib.pyplot as plt
import numpy as np
plt.axis([-2,2,-2,2])#畫圖的X和Y的直
#plt.plot([1,2,3,4],[1,4,9,16], 'bo')#畫圖下標點[X],[Y],'顏色 標字'
#t=[1,2,3,4]
w=[0.2,0.3]#w1,w2
thete=0.85
x=np.arange(-1,3,0.01)
def line(A):
    return (thete-(x*w[0]))/w[1]


plt.plot([0,0,1],[0,1,0],'bo')#
plt.plot([1],[1], 'ro')#
plt.plot(x,line(x))
print(x)

plt.show()






"""
x1w1+x2w2=0.85
x1*y1+x2*y2=0.85
ax+by-c=0
by(x)=c-ax
y(x)=(c-ax)/b
x2=(0.85-w1x1)/w2

for i in range(-1,4):
    x.append(i)
    y.append((0.85-i)/0.9)

"""
#plt.plot([,0.85],[0.85,0],'r-')#畫圖的[x,y]到[x,y]的直
