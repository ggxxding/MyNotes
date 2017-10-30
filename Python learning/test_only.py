import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
'''
plt.figure 
ax=*.add_subplot(111)
ax.set_title
label
ax.legend
'''
x=np.linspace(-5,5,100)
y=1/(1+np.exp(-x))
fig=plt.figure('ddd')
ax=fig.add_subplot(121)
ax.set_title('test')
y1=np.linspace(1,1,100)
y2=np.linspace(0,0,100)
ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y,label='sigmoid')
ax.legend(loc='upper right')
z=np.log(y)
ax.plot(x,z,label='log')
ay=fig.add_subplot(122)
ay.plot(x,1-z,label='log')
az=fig.add_subplot(223)
plt.plot(x,y)
ay.plot(x,y)
plt.legend()
plt.show()

