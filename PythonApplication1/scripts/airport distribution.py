import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pylab import *
###===========read files ========
file = open(r'E:\Projects\haifeng\input\airport-20170308.txt','r')
airport = file.readlines()
file.close()
#===================================================================
num = []
lon = []
lat = []

for i in range(1,len(airport)):
    temp = airport[i]
    num.append( temp.split()[0])
    lon.append(float(temp.split()[1]))
    lat.append(float(temp.split()[2]))
###===========draw map =========================================================================
m=Basemap(projection='cyl',llcrnrlat=0,llcrnrlon=70,urcrnrlat=55,urcrnrlon=140,resolution='l')
m.readshapefile(r'D:\data\shp\bou2_4l','china',linewidth=2,color='black')
parallels = np.arange(0.,55.,10.)
#m.drawparallels(parallels, labels=[1,0,0,0], color='grey',linewidth=1.0)
meridians = np.arange(70.,140.,10)
#m.drawmeridians(meridians,labels=[0,0,0,1],color='grey',linewidth='1.0')
#cm = plt.cm.get_cmap('PuBu')
#print np.max(median)
#plt.show()

###============south ocean=======================================================================
#so = Basemap(projection='cyl',llcrnrlat=0,llcrnrlon=110,urcrnrlat=20,resolution='l')
#so.readshapefile(r'D:\data\shp\bou2_4l','china',linewidth=2,color='black')


###===========draw airport================
m.scatter(lon,lat,s=10,marker='x',vmin=0,vmax=4,cmap=m,color='red')
#mappable = np.arange(0.,4.,0.5)
#cbar=plt.colorbar(mappable,orientation='horizontal',pad=0.05,ticks=[0,0.5,1,1.5,2,2.5,3,3.5,4],extend='max')
#plt.ax.tick_params(labelsize=15)
plt.title('airport distribution ')
plt.show()
#plt.savefig('median.png')
def draw_southocean(ax):
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredEllipse
    # draw an ellipse of width=0.1, height=0.15 in the data coordinate
    ae = AnchoredEllipse(ax.transData, width=0.1, height=0.15, angle=0.,
                         loc=3, pad=0.5, borderpad=0.4, frameon=True)

    ax.add_artist(ae)

#if 1 :
#    ax = plt.gca()
#    ax.set_aspect(1.)
#    draw_southocean(ae)

#    plt.show()
