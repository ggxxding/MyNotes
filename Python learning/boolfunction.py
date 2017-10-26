# -*- coding: utf-8 -*-
#T1:
#以下述两类模式为样本，用感知器算法求判别函数：
#ω1:{(0 0 0)t,(1 0 0)t,(1 0 1)t,(1 1 0)t}; 
#ω2:{(0 0 1)t,(0 1 1)t,(0 1 0)t,(1 1 1)t}.
#且令W(1)=(-1 –2 –2 0)t， C=1.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#输入样本数据
X=np.array([[0,0,0,1],
          [1,0,0,1],
          [1,0,1,1],
          [1,1,0,1],
          [0,0,-1,-1],
          [0,-1,-1,-1],
          [0,-1,0,-1],
          [-1,-1,-1,-1]])
W=np.array([-1,-2,-2,0])
C=1
#设定flag标志，false表示未收敛，ture表示已收敛
def perception(X,W,flag):
    while True:
        flag=True
        for i in range(7):
            
            judge=not np.dot(W,X[i,:].T)>0 #判断类别，是否受惩罚
            if judge:
                flag=False
                print ('惩罚')
                W=W+C*X[i,:]
                
            i+=1
        if flag:break
        
    print ("\n function by Perception is:\n g=(%d)*x1+(%d)*x2+(%d)*x3+(%d)" % (W[0],W[1],W[2],W[3]))
perception(X,W,True)
#T2
#画出上题所给的二类样本，及所求的判决界面
ax=plt.subplot(111,projection='3d')
x=X[:,0]
y=X[:,1]
z=X[:,2]
ax.scatter(x[0:4],y[0:4],z[0:4],c='b',marker='o')
ax.scatter(x[4:8],y[4:8],z[4:8],c='r',marker='x')
x=np.arange(-1,1,0.25)
y=np.arange(-1,1,0.25)
ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
x, y = np.meshgrid(x, y)
g = -W[0]/W[2]*x-W[1]/W[2]*y-W[3]/W[2]
ax.plot_surface(x,y,g,rstride=1, cstride=1, cmap='rainbow')
plt.show()

#T3
#用LMSE算法对题1所给的两样本求判别函数 (可取C=1或C=2) 
#此处取C=1，b(1)=(1,1,1,1,1,1,1,1)t
a1=np.mat(X)
#求出X#规范逆矩阵
X_ni=(a1.T*a1).I*a1.T
b=np.mat((1,1,1,1,1,1,1,1)).T
def LMSE(X_ni,a1,b,flag):
    while True:
        flag=True
        WE=X_ni*b
        E=a1*WE-b
        #如果E=0,结束，输出解
        if E.any()==0:
                print ("\n function is:\n g=(%d)*x1+(%d)*x2+(%d)*x3+(%d)" % (WE[0],WE[1],WE[2],WE[3]))
                flag=True
        #如果E<0，该模式非线性可分
        elif E.any()<0:
                    print ('无解')
                    flag=True
        #如果E>0，且大于收敛阈值，继续迭代
        elif np.abs(E[0])>10e-4:
                    flag=False
                    WE=WE+C*X_ni*(E+np.abs(E))
                    b=b+C*(E+np.abs(E))
        if flag:break
    #四舍五入
    WE[0]=np.round(WE[0])
    WE[1]=np.round(WE[1])
    WE[2]=np.round(WE[2])
    WE[3]=np.round(WE[3])
    print ("\n function by LMSE is:\n g=(%d)*x1+(%d)*x2+(%d)*x3+(%d)" % (WE[0],WE[1],WE[2],WE[3]))

LMSE(X_ni,a1,b,True)

            
    
    






