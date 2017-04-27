import os
import glob
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
import numpy as np
from pyhdf import SD

# Open file.
FILE_NAME = r'D:\Data\Satellite\MODIS\TERRA\MOD14A1\MOD14A1.A2008049.h28v06.006.2015171143835.hdf'
hdf4_name = glob.glob(FILE_NAME)
print("file found {}".format(hdf4_name))
hdf4_obj  = SD.SD(hdf4_name[0], SD.SDC.READ)
print dir(hdf4_obj)

# List available SDS datasets.
print hdf4_obj.select('fptab')[:]
exit()
 
# Read dataset.
DATAFIELD_NAME='FireMask'
data3D = hdf4_obj.select(DATAFIELD_NAME)
data = data3D[2,:,:]
print data

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

m = Basemap(projection='cyl', resolution='l', llcrnrlat=-90, urcrnrlat = 90, llcrnrlon=-180, urcrnrlon = 180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x, y, data)
cb = m.colorbar()
cb.set_label('Unit:%')

plt.title('{0}\n {1} at H20PrsLvls=11').format(FILE_NAME,DATAFIELD_NAME)
fig = plt.gcf()
plt.show()


