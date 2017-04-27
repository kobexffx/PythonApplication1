import netCDF4 as nc
from netCDF4 import Dataset
a = Dataset('./data/pres.mon.ltm.nc')
print a.variables.keys()
time = a.variables['time'][:]
print time
print dir(time)
print a.variables['time'].dtype
print a.variables['time'].long_name
print a.variables['time'].ndim
