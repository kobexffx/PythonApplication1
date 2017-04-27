#coding=utf-8
# 作者 ： 叶飞
# 风廓线雷达数据绘图图
import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pylab import *
from matplotlib.ticker import  MultipleLocator,LogLocator
from matplotlib.ticker import  FormatStrFormatter
#=============read data======================
#BST - Beijing Standard Time UTC + 8:00 
#UTC - Universal Time Coordinated
#DATE = '20140510'
print 'please input date:(YYYYMMDD)'
DATE = raw_input()
YEAR = DATE[0:4]
MON  = DATE[4:6]
DAY  = DATE[6:8]

PATH = 'D:\\Data\\radar\\风廓线雷达数据\\54406\\'+YEAR+'\\'
PATH = PATH.decode('utf-8')
print PATH

FILE_NAME_OUT = 'WPR_'+DATE+'_UTC_00:00_to_23:00'
FileNames  = os.listdir(PATH) 
INPUT_FILE = []
TIME       = []
#=======获取2016目录下所有文件名=====================
for files in FileNames:
    INPUT_FILE.append(files)
    #print files 
#==========================================================
for ii in range(len(INPUT_FILE)):
    temp = INPUT_FILE[ii]
    temp = temp.split('_')[4]
    temp = temp[:8]
    if  temp == DATE :
        print 'read file: '+INPUT_FILE[ii]+'OK!'
        file = open(PATH+INPUT_FILE[ii],'r')
        data = file.readlines()
        file.close()
        #break

#=============get time========================
        temp = INPUT_FILE[ii]
        temp = temp.split('_')[4]
        TIME = temp[8:10]
        #TIME.append(temp)
        #TIME.append(ii)
        #print TIME
        #break
#=============define vars=====================
        hgt    = []
        udir   = []
        u      = []
        v      = []
        cn2    = []
        uvalid = []
        vvalid = []
        uu     = []
        vv     = []
        time   = []
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
#==============transfrom data=================
        for i in range(len(u)):
            if u[i] == '/////':
                u[i] = '0'
            temp = u[i]
            uu.append(float(temp))
            
            if v[i] == '/////' or v[i] == '//////' :
                v[i] = '0'
            temp = v[i]
            vv.append(float(temp))
            
            #temp = TIME[ii]
            time.append(int(TIME))
            #print time[i],hgt[i],uu[i],vv[i]
            
        
        
        # Masked arrays are also supported
        masked_uu = np.ma.masked_equal(uu,0)
        #masked_uu[4] = 0  # Bad value that should not be plotted when masked
        #masked_uu[4] = np.ma.masked
        masked_vv = np.ma.masked_equal(vv,0)
        
        # Identical plot to panel 2 in the first figure, but with the point at
        #(0.5, 0.25) missing (masked)
#=========================start fig plot==================================    
        
        #fig = plt.figure()
        #ax = plt.add_subplot(1, 1, 1)
        #plt.xlim(-1,11)
        #plt.ylim(0,14000)
        ax = plt.subplot(111)                                
        plt.axis([0, 23, 0, 2000])                          # 设置坐标范围
        plt.title(FILE_NAME_OUT)                             # 添加标题
        plt.xlabel(DATE+'_UTC_HOUR')                              # x坐标轴标题
        plt.ylabel('HEIGHT:m')                               # y坐标轴标题
                                                             
        #设置主刻度标签的位置,标签文本的格式                                      
        xmajorLocator = MultipleLocator(1)                  # 将x主刻度标签设置为1的倍数
        xmajorFormatter = FormatStrFormatter('%2d')           # 设置x轴标签文本的格式
        xminorLocator = MultipleLocator(0.5)                 # 将x轴次刻度标签设置为0.5的倍数  
        ymajorLocator = MultipleLocator(100)                # 将y轴主刻度标签设置为1000的倍数
        #ymajorLocator = LogLocator(10)                      
        ymajorFormatter = FormatStrFormatter('%d')           # 设置y轴标签文本的格式 
        yminorLocator = MultipleLocator(500)                 # 将此y轴次刻度标签设置为500的倍数 
        
        #显示主刻度标签的位置，文本
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.xaxis.set_major_formatter(xmajorFormatter)
        ax.yaxis.set_major_locator(ymajorLocator)
        ax.yaxis.set_major_formatter(ymajorFormatter)
        
        #显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(xminorLocator)
        ax.yaxis.set_minor_locator(yminorLocator)
        
        #根据风廓线雷达数据绘制不同时刻的风廓线图
        plt.barbs(time, hgt, masked_uu, masked_vv, color='r',pivot='tip')
    
#plt.show()
plt.savefig('./WPR/'+DATE+'.png')