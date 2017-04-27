#coding=utf-8
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
q=Dataset(r'D:/Desktop/GTOPO30_2min.nc')
a=q.variables['HT'][:]
lat=q.variables['lat'][:]
lon=q.variables['lon'][:]
fig=plt.figure(figsize=(8,8))
fig.add_axes([0.05,0.05,0.9,0.9])
m=Basemap(projection='cyl',llcrnrlon=70, urcrnrlon=135,\
          llcrnrlat=10, urcrnrlat=56, lon_0=125, lat_0=25, resolution='l')
m.drawcountries(color='w')
m.drawcoastlines(linewidth=0.4,color='w')
m.drawparallels(circles=np.arange(-80,90,20),labels=[0,1,0,0])
m.drawmeridians(meridians=np.arange(0,360,20),lables=[0,0,0,1],fontsize=10)
ny=a.shape[0]
nx=a.shape[1]
map0=r'D:\Program Files\WinPython-64bit-2.7.5.3\data\China boundary\province boundary\bou2_4l'
m.readshapefile(map0,'world',linewidth=0.5)
########
########�趨��ͼ����
index1=np.logical_and(lat>=10,lat<=56)           #�����볣���߼����㣨�Ƚϴ�С�����õ���������
index2=np.logical_and(lon>=70,lon<=135)
y=lat[index1]
x=lon[index2]
a=a[index1,:]
a=a[:,index2]
########
cs=plt.contourf(x,y,a)
cbar=m.colorbar(cs,location='bottom',pad=0.1,extend='both',extendfrac='auto')
plt.show()
q.close()