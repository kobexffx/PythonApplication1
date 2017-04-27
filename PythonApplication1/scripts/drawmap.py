# -*- coding: cp936 -*-
#===================================================
#ʹ��cartopy���Ƶ�ͼ
#��Ҫ��http://www.naturalearthdata.com/downloads/����shape�ļ�
#���غ󣬽�ѹ�����ļ���ͳһȥ��"ne_"��ͷ��������D:\Program Files\
#WinPython-32bit-2.7.9.3\settings\.local\share\cartopy\shapefiles\natural_earth\physical\ 
#·�����棬coastline�ļ���Ӧax.coastlines���land�ļ���Ӧland����
#===================================================
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
scale= '110m'
fig  = plt.figure(figsize=(8, 10))
ax   = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
ax.set_global()
#===================================================
#��Ҫ���½����ɫʱʹ��
#ax.add_feature(cfeature.LAND, facecolor='0.75') #Ĭ��Ϊ110m�������ֱ���������������
land = cfeature.NaturalEarthFeature('physical', 'land', scale,edgecolor='face',
                                                              facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='0.75')
#===================================================
#�ı�ax.add_feature��ax.coastlines���Ⱥ�ʹ��˳���ʵ�ֱ߽��ߵ���ʾ����ȫ��串��
ax.coastlines(scale)
#===================================================
#��ע������
ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
#zero_direction_label�������þ��ȵ�0�ȼӲ���E��W
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
#���������
gl = ax.gridlines()
