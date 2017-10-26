import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#mpl.rcParams['xtick.labelsize']=16
mpl.rcParams['ytick.labelsize']=16
mpl.rcParams['axes.titlesize']=10
mpl.rcParams['axes.labelsize']=14
#mpl.rcParams['xtick.major.size']=0
#mpl.rcParams['ytick.major.size']=0

speed_map={
	'dog':(48,'#7199cf'),
	'cat':(45,'#4fc4aa'),
	'cheetah':(120,'#e1a7a2')
}

fig=plt.figure('Bar chart&Pie chart')

ax=fig.add_subplot(121)
ax.set_title('rrrRunning speed - bar chart')

xticks=np.arange(3)
bar_width=0.5

animals=speed_map.keys()
speeds=[x[0] for x in speed_map.values()]
colors=[x[1] for x in speed_map.values()]
bars=ax.bar(xticks,speeds,width=bar_width,edgecolor='none')

ax.set_ylabel('Speed(kmh')
ax.set_xlabel('fff')
ax.set_xticks(xticks)
ax.set_xticklabels((xticks+bar_width)/2)
ax.set_xlim([bar_width/2-1,3-bar_width/2])
ax.set_ylim([0,125])
for bar,color in zip(bars,colors):
	bar.set_color(color)
ax=fig.add_subplot(122)
ax.set_title('Running speed - pie chart')
labels=['{}\n{} kmh'.format(animal,speed) for animal,speed in zip(animals,speeds)]
ax.pie(speeds,labels=labels,colors=colors)
plt.show()
