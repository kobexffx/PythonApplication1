import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pylab import *
#===get all the files under this folder====
# print help(np.median)
# exit(0)
list=os.listdir('H:\\zhanglaoshi\\do_tibetan_station_rain_statistics')
#======get the file with the extension of '.txt'====
filename=[]
for element in list:
	if element.find('.txt')!=-1:
		filename.append(element)
		# print os.path.getsize(element)
		# print element
# print filename
# print len(filename)
###======calculate 4 quartiles=======
output=open('box_result.txt','w')
accord=open('output_stn_info_of_Tibetan_region.txt','r')
locations=accord.readlines()
#=====Basemap settings=====

#=======output file and draw======
rain=[];median=[];shang=[];xia=[];color=[]
lat=[];lon=[];
color_list = plt.cm.Set3(np.linspace(0,0.5,151))
# print color_list
# exit(0)
for name in filename:
	f=open('H:\\zhanglaoshi\\do_tibetan_station_rain_statistics\\'+name,'r')
	# print f
	val=[]
	if os.path.getsize('H:\\zhanglaoshi\\do_tibetan_station_rain_statistics\\'+name)!=42504:
		continue
	content=f.readlines()
	# print len(content)
	for ii in np.arange(len(content)):
		if float(content[ii])>=32700 or float(content[ii])==0:
			continue
		else:
			val.append(float(content[ii]))
	# print val,type(val)
	val=[ele/10 for ele in val]
	# print val,type(val)
	# print len(val)
	# print val,'\n',type(val)
	val=sorted(val);length=len(val)
	# print len(val)
	# xia=val[]
	# median1=(val[int(length/2)])
	# shang1=(val[int(length*3/4)])
	# xia1=(val[int(length/4)])
	median1=np.percentile(val,50);xia1=np.percentile(val,25);shang1=np.percentile(val,75)
	median.append(median1)
	shang.append(shang1)
	xia.append(xia1)
	val=np.array(val)
	# print len(val)
	# boxplot(val)
	# show()
	# exit(0)
	for line in locations:
		# print line
		if line.find(name[0:5])!=-1:
			lat1=line[6:10];lon1=line[11:16]
			output.write(name[0:5]+"  "+lon1+"  "+lat1+"  "+str(xia1)+"  "+str(median1)+"  "+str(shang1)+'\n')	
			lat.append(float(lat1));lon.append(float(lon1));

			

lon=[lon/100 for lon in lon];lat=[lat/100 for lat in lat]
print median
###===========draw median=======
m=Basemap(projection='cyl',llcrnrlat=25,llcrnrlon=70,urcrnrlat=40,urcrnrlon=105,resolution='l')
m.readshapefile('H:\\zhanglaoshi\\tibetan_boundary\\tibet','tibet',linewidth=1,color='gray')
m.drawparallels([25,30,35,40],labels=[1,0,0,0])
m.drawmeridians([70,80,90,100],labels=[0,0,0,1])
cm = plt.cm.get_cmap('PuBu')
# print np.max(median)
plt.scatter(lon,lat,c=median,s=80,marker='o',vmin=0,vmax=4,cmap=cm)
cbar=plt.colorbar(orientation='horizontal',pad=0.05,ticks=[0,0.5,1,1.5,2,2.5,3,3.5,4],extend='max')
cbar.ax.tick_params(labelsize=15)
plt.title('scatter plot')
# plt.show()
plt.savefig('median.png')
# plt.show()
# plt.close()
exit()
#=============draw upper quartile======
m=Basemap(projection='cyl',llcrnrlat=25,llcrnrlon=70,urcrnrlat=40,urcrnrlon=105,resolution='l')
m.readshapefile('H:\\zhanglaoshi\\tibetan_boundary\\tibet','tibet',linewidth=1,color='gray')
m.drawparallels([25,30,35,40],labels=[1,0,0,0])
m.drawmeridians([70,80,90,100],labels=[0,0,0,1])
cm = plt.cm.get_cmap('PuBu')
print np.max(median)
plt.scatter(lon,lat,c=shang,s=80,marker='o',cmap=cm)
cbar=plt.colorbar(orientation='horizontal',pad=0.05,extend='both')
cbar.ax.tick_params(labelsize=15)
plt.title('upper quartile')
plt.savefig('upper_quartile.pdf')
# plt.show()
# print help(gca().set_xlabel)
# print help(plt.axis)
# print help(plt.text)
# plt.xlabel('longtitude',labelpad=20,fontsize=15)
# plt.ylabel('latitude',labelpad=35,fontsize=15)
# plt.axis('equal')
# plt.axis([90,100,30,40])

# print help(plt.colorbar)
# print dir()