import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

map = Basemap(projection='cyl',llcrnrlon=70, urcrnrlon=140,\
           llcrnrlat=10, urcrnrlat=56, lon_0=125, lat_0=25, resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25,color ='w')
map.drawcountries(linewidth=0.25,color ='w')
#map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='w')
# draw lat/lon grid lines every 30 degrees.
#map.drawmeridians(np.arange(0,360,30))
#map.drawparallels(np.arange(-90,90,30))

# 叠加机场站点图
f = open (r'e:\projects\haifeng\input\airport-20160712.txt','r')
data = f.readlines()
f.close()

air_num = []
air_lon = []
air_lat  = []
for i in range(1,len(data)):
    temp = data[i]
    air_num.append(int(temp.split()[0]))
    air_lon.append(float(temp.split()[1]))
    air_lat.append(float(temp.split()[2]))
for i in range(1,len(data)-1):
    plt.scatter(map,air_lat[i],air_lat[i])
plt.show()

