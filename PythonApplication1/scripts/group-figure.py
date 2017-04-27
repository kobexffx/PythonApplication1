import numpy as np
import matplotlib.pyplot as plt

ax1 = plt.subplot(1,2,1)
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
area = np. pi*(15**np.random.rand(100)**2)
plt.scatter(x,y,s=area,c = colors,alpha = 0.5)
############################
ax2 = plt.subplot(1,2,2,projection = 'polar')
N = 20
theta = np.linspace(0.0,2*np.pi,N,endpoint = False)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)
bars = plt.bar(theta,radii,width=width,bottom=0.0)
for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.jet(r/10.0))
    bar.set_alpha(0.5)
plt.show()
