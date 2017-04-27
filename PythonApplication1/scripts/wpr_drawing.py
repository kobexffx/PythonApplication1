# !/usr/bin/python
# -*- coding: utf-8 -*-
# author : kobexffx
# version: Python 2.7.11
# goals  : draw all the wind profile pictures
# BST - Beijing Standard Time UTC + 8:00 
# UTC - Universal Time Coordinated
#====================define global vars======================
YEAR = ['2012','2013','2014','2015',]#'2009','2010','2011','2012','2013','2014','2015','2016']
MONS = ['01','02','03','04','05','06','07','08','09','10','11','12']
DAYS = ['01','02','03','04','05','06','07','08','09','10','11','12',
        '13','14','15','16','17','18','19','20','21','22','23','24',
        '25','26','27','28','29','30','31']
path_out = '.\\WPR\\'
#====================import packages=========================
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.ticker import  MultipleLocator,LogLocator
from   matplotlib.ticker import  FormatStrFormatter
#====================define functions========================
def wpr_draw(DATE,PATH,INPUT_FILE):
    file_out = 'WPR_'+DATE+'_UTC_00:00_to_23:00'
    title    = file_out
    yr       = DATE[:4]
    mo       = DATE[4:6]
    for ii in range(len(INPUT_FILE)):
        temp = INPUT_FILE[ii]
        temp = temp.split('_')[4]
        temp = temp[:8]
        if  temp == DATE :
            #print 'read file: '+INPUT_FILE[ii]+'OK!'
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
            plt.axis([-1, 23, 0, 2000])                          # 设置坐标范围
            plt.title(title)                             # 添加标题
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
            plt.barbs(time, hgt, uu, vv, color='r',pivot='tip')
    #plt.show()
    plt.savefig(path_out+yr+'\\'+yr+mo+'\\'+DATE+'.png')
    plt.cla()


def main():
    INPUT_FILE = []
    for yr in YEAR:
        list     = os.listdir(path_out)
        if yr not in list:
            os.mkdir(path_out+yr+'\\')
        path_in  = 'D:\\Data\\radar\\wpr\\54406\\'+yr+'\\'
        filelist = os.listdir(path_in)
        for file in filelist:
            INPUT_FILE.append(file)
       
        for mo in MONS:
            list = os.listdir(path_out+yr+'\\')
            if yr+mo not in list:
                os.mkdir(path_out+yr+'\\'+yr+mo+'\\')
            for day in DAYS:
                DATE = yr + mo + day 
                print DATE
                wpr_draw(DATE,path_in,INPUT_FILE)
                #print DATE+'output ok!'
        print yr+' output ok!'
    print 'mission completed !'
                     
#====================execute program=========================
if __name__ == '__main__':
    main()