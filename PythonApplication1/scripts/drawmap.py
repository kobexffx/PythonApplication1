# -*- coding: cp936 -*-
#===================================================
#使用cartopy绘制地图
#需要从http://www.naturalearthdata.com/downloads/下载shape文件
#下载后，解压缩，文件名统一去掉"ne_"开头，拷贝至D:\Program Files\
#WinPython-32bit-2.7.9.3\settings\.local\share\cartopy\shapefiles\natural_earth\physical\ 
#路径下面，coastline文件对应ax.coastlines命令，land文件对应land命令
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
#需要填充陆地颜色时使用
#ax.add_feature(cfeature.LAND, facecolor='0.75') #默认为110m，其它分辨率需用下面命令
land = cfeature.NaturalEarthFeature('physical', 'land', scale,edgecolor='face',
                                                              facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='0.75')
#===================================================
#改变ax.add_feature和ax.coastlines的先后使用顺序可实现边界线的显示或完全填充覆盖
ax.coastlines(scale)
#===================================================
#标注坐标轴
ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
#zero_direction_label用来设置经度的0度加不加E和W
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
#添加网格线
gl = ax.gridlines()
