import h5py
import numpy as np

#Add data file
fn = 'D:\Data\Satellite\FY3C\FY3C_VIRRX_GBAL_L2_GFR_MLT_GLL_20151201_POAD_1000M_MS.HDF'
f = h5py.File(fn,'w')
#Get data variable
v = f['FIRES']
#Get data array
data = v[:,5]
lat = v[:,3]
lon = v[:,4]
#Plot
axesm()
world = shaperead('D:\Data\shp\cntry02.shp')
china = shaperead('D:\Data\shp\bou2_4p.shp')
geoshow(china, edgecolor='gray')
geoshow(world, edgecolor=(100,100,100))
layer = scatterm(lon, lat, data, s=3, colors=['r'], edge=False, marker='+')
title('FY-3C GFR')
axism()