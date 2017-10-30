'''
http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=DeepLearning&doc=exercises/ex5/ex5.html

http://www.cnblogs.com/tornadomeet/archive/2013/03/17/2964515.html
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Regularized 线性回归练习
'''
h(x)=w0+w1*x+w2*x^2+...+w5*x^5

w=(X.T*X+λI).-1 X.Ty
'''

x=np.loadtxt('ex5Data/ex5Linx.dat')
y=np.loadtxt('ex5Data/ex5Liny.dat')
# plot training data
fig=plt.figure('data')	#标题
ax=fig.add_subplot(111)	#子图
ax.set_title('test_title')	#子图标题
ax.scatter(x,y,color='r',label='training data') #样本散点图，label用于标记legend图例

#画不同λ的图像

for i in [0,1,5,10]:	# i=λ
 one=np.ones((len(x),1))
 x=x.reshape((len(x),1))
 X=np.hstack((one,one*x,one*x**2,one*x**3,one*x**4,one*x**5))	#X矩阵
 Y=y.reshape((len(y),1))
 w=np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)+i*np.eye(len(X.T))),X.T),Y)	#求参数w

 x_in=np.linspace(-1,1,100)
 x_in=x_in.reshape(len(x_in),1)
 one=np.linspace(1,1,100).reshape(len(x_in),1)
 X_in=np.hstack((one,one*x_in,one*x_in**2,one*x_in**3,one*x_in**4,one*x_in**5))	#X轴
 Y_pre=np.dot(X_in,w)	#对应Y值
 ax.plot(X_in[:,1],Y_pre,label='lambda={}'.format(i))
ax.legend() 
'''
图例 n1,=ax.plot(x,y,[label='***'])
    n2,=ax.plot...
    ax.legend([n1,n2],['label1','label2'],loc='')
'''
plt.show()