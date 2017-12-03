import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 3D图标必须的模块，project='3d'的定义
from mpl_toolkits.mplot3d import Axes3D     

np.random.seed(42)
num_x=100
# 生成格点
x1 = np.linspace(-100, 100, num_x)
x2 = np.linspace(-100, 100, num_x)


X1,X2 = np.meshgrid(x1, x2)

Z=((np.sin(X1**2+X2**2))**2-0.5)/(1+0.001*(X1**2+X2**2))**2-0.5



# 创建图表
fig = plt.figure('3D surface & wire')

ax = fig.add_subplot(111,projection='3d')

# alpha定义透明度，cmap是color map
# rstride和cstride是两个方向上的采样，越小越精细，lw是线宽
ax.plot_surface(X1, X2, Z,cmap='jet')


plt.show()