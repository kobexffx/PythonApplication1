#coding=utf-8
#===================================================
#函数形式，调用cartopy，绘制区域地图
#===================================================
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
def make_map(scale,box,xstep,ystep):
    fig=plt.figure(figsize=(8, 10))
    ax=plt.axes(projection=ccrs.PlateCarree())
    #set_extent需要配置相应的crs，否则出来的地图范围不准确
    ax.set_extent(box,crs=ccrs.PlateCarree())
    land = cfeature.NaturalEarthFeature('physical', 'land', scale,edgecolor='face',
                                                              facecolor=cfeature.COLORS['land'])
    ax.add_feature(land, facecolor='0.75')
    ax.coastlines(scale)
    #===================================================
    #图像地址D:\Program Files\WinPython-32bit-2.7.9.3\python-2.7.9\Lib\site-packages\
    #cartopy\data\raster\natural_earth\50-natural-earth-1-downsampled.png
    #如果有其它高精度图像文件，改名替换即可
    ax.stock_img()
    #===================================================
    #标注坐标轴
    ax.set_xticks(np.arange(box[0],box[1]+xstep,xstep), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(box[2],box[3]+ystep,ystep), crs=ccrs.PlateCarree())
    #zero_direction_label用来设置经度的0度加不加E和W
    lon_formatter = LongitudeFormatter(zero_direction_label=False)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #添加网格线
    ax.grid()
    return fig,ax
box=[100,150,0,50]
fig,ax=make_map(scale='50m',box=box,xstep=10,ystep=10)