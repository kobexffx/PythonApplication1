#coding=utf-8
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pylab import *
#=============read data======================
PATH = 'D:\\Data\\radar\\风廓线雷达数据\\54406\\2016\\'
PATH = PATH.decode(sys.stdin.encoding)
file = open(PATH+'Z_RADA_I_54406_20160101000000_P_WPRD_PB_ROBS.TXT','r')
data = file.readlines()
file.close()
#=============define vars=====================
hgt  = []
udir = []
u    = []
v    = []
cn2  = []
uvalid = []
vvalid = []
#==============read vars======================
for i in range(3,len(data)-1):
    temp = data[i]
    hgt.append( int(temp.split()[0]))
    udir.append(temp.split()[1])
    u.append(temp.split()[2])
    v.append(temp.split()[3])
    uvalid.append(int(temp.split()[4]))
    vvalid.append(int(temp.split()[5]))
    cn2.append(temp.split()[6])