#!/usr/bin/env python

import glob
import numpy as np
import matplotlib.pyplot as plt
from __future__ import division
from __future__ import print_function
# matplotlib inline
from pyhdf import SD
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import cm

#Read MODIS L1B data
hdf_L1B=glob.glob('D:\Data\Satellite\MODIS\MODIS_L1B\MYD021KM.A2013312.0505*.hdf')
print("MODIS L1B file found {}".format(hdf_L1B))
hdf_GEO=glob.glob('D:\Data\Satellite\MODIS\MODIS_L1B\MYD03.A2013312.0505*.hdf')
print("MODIS Geolocation file found {}".format(hdf_GEO))

#Get file objects
L1B_obj=SD.SD(hdf_L1B[0], SD.SDC.READ)
GEO_obj=SD.SD(hdf_GEO[0], SD.SDC.READ)

#List all variables in L1B file
print(L1B_obj.datasets().keys())
raw_C31=L1B_obj.select('EV_1KM_Emissive')[:]
raw_C1=L1B_obj.select('EV_250_Aggr1km_RefSB')[:]
# Check the file size
print("Size of 'EV_1KM_Emissive': {}".format(raw_C31.shape))
print("Size of 'EV_250_Aggr1km_RefSB': {}".format(raw_C1.shape))
print("Attributies of 'EV_1KM_Emissive'\n===============================")
print(L1B_obj.select('EV_1KM_Emissive').attributes())
print("Attributies of 'EV_500_Aggr1km_RefSB'\n===============================")
print(L1B_obj.select('EV_250_Aggr1km_RefSB').attributes())

band_names=L1B_obj.select('EV_1KM_Emissive').attributes()['band_names']
radiance_scales=L1B_obj.select('EV_1KM_Emissive').attributes()['radiance_scales']
radiance_offsets=L1B_obj.select('EV_1KM_Emissive').attributes()['radiance_offsets']

band_names=np.fromstring(band_names, dtype=np.float, sep=',')
radiance_scales=np.array(radiance_scales)
radiance_offsets=np.array(radiance_offsets)

hit=band_names==31
raw_C31=raw_C31[hit, :, :]
C31=(raw_C31 - radiance_offsets[hit] * np.ones(raw_C31.shape)) * radiance_scales[hit]