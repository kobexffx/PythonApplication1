#coding=utf-8
#===================================================
#函数形式，调用cartopy，绘制全球地图
#===================================================
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
def make_map(scale):
    fig=plt.figure(figsize=(8, 10))
    ax=plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    ax.set_global()
    land = cfeature.NaturalEarthFeature('physical', 'land', scale,edgecolor='face',
                                        facecolor=cfeature.COLORS['land'])
    ax.add_feature(land, facecolor='0.75')
    ax.coastlines(scale)
    #标注坐标轴
    ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
    ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    #zero_direction_label用来设置经度的0度加不加E和W
    lon_formatter = LongitudeFormatter(zero_direction_label=False)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    #添加网格线
    #gl = ax.gridlines()
    ax.grid()
    return fig,ax
fig,ax=make_map(scale='110m')
