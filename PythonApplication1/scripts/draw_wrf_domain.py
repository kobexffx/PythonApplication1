#!/usr/bin/env python
'''
    File name: draw_wrf_domain.py
    Author: Liang Chen
    E-mail: chenliang@tea.ac.cn
    Date created: 2016-12-22
    Date last modified: 2016-12-22

    ##############################################################
    Purpos:
    this function reads in namelist.wps and plot the wrf domain
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
from matplotlib.colors import LinearSegmentedColormap
import shapefile
from matplotlib.collections import LineCollection
import matplotlib.colors
import sys

def draw_screen_poly( lats, lons):
    x, y =  lons, lats 
    xy = zip(x,y)
    poly = plt.Polygon( xy, edgecolor="b",fc="none", lw=2, alpha=1)
    plt.gca().add_patch(poly)

# clear previous figure 
#plt.ion()
#plt.clf()

## read shape files
YR=[228,26,28]
CN=[255,255,50]

#sShapeFiles="./Shapefiles/"
#shape_line=['yellow_river_basin.shp','R_SmoothLine.shp','china_province.shp']
sShapeFiles="./Shapefiles/"
shape_line=['river2.shp','cnhimap.shp']
 
## setting namelist.wps domain information
file_folder="./Namelist/"
file_name="namelist.wps_cn4km"
sfile=file_folder+file_name
name_dict={}
with open(sfile) as fr:
    for line in fr:
        if "=" in line:
           line=line.replace("=","").replace(",","")
           name_dict.update({line.split()[0]: line.split()[1:]})

dx = float(name_dict["dx"][0])
dy = float(name_dict["dy"][0])
max_dom = int(name_dict["max_dom"][0])
parent_grid_ratio = map(int, name_dict["parent_grid_ratio"])
i_parent_start = map(int, name_dict["i_parent_start"])
j_parent_start = map(int, name_dict["j_parent_start"])
e_sn = map(int, name_dict["e_sn"])
e_we = map(int, name_dict["e_we"])
ref_lat=  float(name_dict["ref_lat"][0])
ref_lon=  float(name_dict["ref_lon"][0])
truelat1 = float(name_dict["truelat1"][0])
truelat2 = float(name_dict["truelat2"][0])

## draw map
#fig = plt.figure(figsize=(8,4))
#ax = fig.add_axes([0.05,0.05,0.90,0.90])
fig = plt.figure(figsize=(12,6))
#Custom adjust of the subplots
plt.subplots_adjust(left=0.10,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
ax = plt.subplot(111)

m = Basemap(resolution="l", projection="lcc", rsphere=(6370000.0, 6370000.0), 
lat_1=truelat1, lat_2=truelat2, lat_0=ref_lat, lon_0=ref_lon, 
width=dx*(e_we[0]-1), height=dy*(e_sn[0]-1))

#m.drawcoastlines()
#m.drawcountries(linewidth=2)
#m.drawcountries()

#m.fillcontinents()
#m.fillcontinents(color=(0.8,1,0.8))
#m.drawmapboundary()
#m.fillcontinents(lake_color="aqua")
#m.drawmapboundary(fill_color="aqua")

ii=0
for sr in shape_line:
    print sr
    r = shapefile.Reader(sShapeFiles+sr)
    shapes = r.shapes()
    records = r.records()
    for record, shape in zip(records,shapes):
        lons,lats = zip(*shape.points)
        data = np.array(m(lons, lats)).T

        if len(shape.parts) == 1:
            segs = [data,]
        else:
            segs = []
            for i in range(1,len(shape.parts)):
                index = shape.parts[i-1]
                index2 = shape.parts[i]
                segs.append(data[index:index2])
            segs.append(data[index2:])

        lines = LineCollection(segs,antialiaseds=(1,))
#       lines.set_facecolors(cm.jet(np.random.rand(1)))
        if ii==0:
            lines.set_edgecolors('b')
            lines.set_linewidth(2)
        else:
            lines.set_edgecolors('k')
            lines.set_linewidth(1)
        ax.add_collection(lines)

    ii=ii+1



m.drawparallels(np.arange(-90, 90, 10), labels = [1,0,0,0], fontsize=16,dashes=[1,1])
m.drawmeridians(np.arange(-180, 180, 10), labels = [0,0,0,1], fontsize=16,dashes=[1,1])


## plot center position
cenlon=range(max_dom); cenlat=range(max_dom)
cenlon_model=dx*(e_we[0]-1)/2.0
cenlat_model=dy*(e_sn[0]-1)/2.0

cenlon[0], cenlat[0]=m(cenlon_model, cenlat_model, inverse=True)

#plt.plot(cenlon,cenlat,marker="o",color="gray")
plt.plot(cenlon_model,cenlat_model, marker="o", color="gray")
plt.text(cenlon_model*0.62, cenlat_model*1.01, "({cenlon}, {cenlat})".format(
    cenlon=round(cenlon[0],2), cenlat=round(cenlat[0],2))
        )
#print cenlon, cenlat

#### draw nested domain rectangle
lon=range(4); lat=range(4)

if max_dom >= 2:
    ### domain 2
    # 4 corners
    ll_lon = dx*(i_parent_start[1]-1)
    ll_lat = dy*(j_parent_start[1]-1)
    ur_lon = ll_lon + dx/parent_grid_ratio[1] * (e_we[1]-1)
    ur_lat = ll_lat + dy/parent_grid_ratio[1] * (e_sn[1]-1)
    
    ## lower left (ll)
    lon[0],lat[0] = ll_lon, ll_lat
    ## lower right (lr)
    lon[1],lat[1] = ur_lon, ll_lat
    ## upper right (ur)
    lon[2],lat[2] = ur_lon, ur_lat
    ## upper left (ul)
    lon[3],lat[3] = ll_lon, ur_lat
    
    draw_screen_poly(lat, lon)
    #plt.scatter(lon,lat)
    plt.plot(lon, lat, "o")
#    plt.text(lon[0]*0.9, lat[0]*0.9, "({i}, {j})".format(i=i_parent_start[1], j=j_parent_start[1]))
#    for node in range(4):
#        plt.text(lon[node],lat[node],"({i}, {j})".format(i=i_parent_start[1], j=j_parent_start[1]))
#
    cenlon_model = ll_lon + (ur_lon-ll_lon)/2.0
    cenlat_model = ll_lat + (ur_lat-ll_lat)/2.0
    cenlon[1], cenlat[1]=m(cenlon_model, cenlat_model, inverse=True)

#    plt.plot(cenlon_model, cenlat_model,marker="o")
    
    #print m(cenlon, cenlat)cenlon, cenlat, ll_lon, ll_lat, ur_lon, ur_lat
    #print m(cenlon, cenlat,inverse=True)


if max_dom >= 3:
    ### domain 3
    ## 4 corners
    ll_lon += dx/parent_grid_ratio[1]*(i_parent_start[2]-1)
    ll_lat += dy/parent_grid_ratio[1]*(j_parent_start[2]-1)
    ur_lon = ll_lon +dx/parent_grid_ratio[1]/parent_grid_ratio[2]*(e_we[2]-1)
    ur_lat =ll_lat+ dy/parent_grid_ratio[1]/parent_grid_ratio[2]*(e_sn[2]-1)
    
    ## ll
    lon[0],lat[0] = ll_lon, ll_lat
    ## lr
    lon[1],lat[1] = ur_lon, ll_lat
    ## ur
    lon[2],lat[2] = ur_lon, ur_lat
    ## ul
    lon[3],lat[3] = ll_lon, ur_lat
    
    draw_screen_poly(lat, lon)
    plt.text(lon[0]-lon[0]/10,lat[0]-lat[0]/10,"({i}, {j})".format(i=i_parent_start[2], j=j_parent_start[2]))
    #plt.plot(lon,lat,linestyle="",marker="o",ms=10)

    cenlon_model = ll_lon + (ur_lon-ll_lon)/2.0
    cenlat_model = ll_lat + (ur_lat-ll_lat)/2.0
#    plt.plot(cenlon,cenlat,marker="o",ms=15)
    #print m(cenlon, cenlat)cenlon, cenlat, ll_lon, ll_lat, ur_lon, ur_lat
    #print m(cenlon, cenlat,inverse=True)
    cenlon[2], cenlat[2]=m(cenlon_model, cenlat_model, inverse=True)


if max_dom >= 4:
    ### domain 3
    ## 4 corners
    ll_lon += dx/parent_grid_ratio[1]/parent_grid_ratio[2]*(i_parent_start[3]-1)
    ll_lat += dy/parent_grid_ratio[1]/parent_grid_ratio[2]*(j_parent_start[3]-1)
    ur_lon = ll_lon +dx/parent_grid_ratio[1]/parent_grid_ratio[2]/parent_grid_ratio[3]*(e_we[3]-1)
    ur_lat =ll_lat+ dy/parent_grid_ratio[1]/parent_grid_ratio[2]/parent_grid_ratio[3]*(e_sn[3]-1)
    
    ## ll
    lon[0],lat[0] = ll_lon, ll_lat
    ## lr
    lon[1],lat[1] = ur_lon, ll_lat
    ## ur
    lon[2],lat[2] = ur_lon, ur_lat
    ## ul
    lon[3],lat[3] = ll_lon, ur_lat
    
    draw_screen_poly(lat, lon)
    #plt.plot(lon,lat,linestyle="",marker="o",ms=10)

    cenlon_model = ll_lon + (ur_lon-ll_lon)/2.0
    cenlat_model = ll_lat + (ur_lat-ll_lat)/2.0
#    plt.plot(cenlon,cenlat,marker="o",ms=15)
    #print m(cenlon, cenlat)cenlon, cenlat, ll_lon, ll_lat, ur_lon, ur_lat
    #print m(cenlon, cenlat,inverse=True)
    cenlon[3], cenlat[3]=m(cenlon_model, cenlat_model, inverse=True)

'''
with open("./observation-position-d2.csv") as f:
    f.next()
    for line in f:
        x,y=bm(*map(float, line.strip().split(",")[1:]))
        label=line.strip().split(",")[0]
        plt.plot(x,y,"o",label=label)
#        print(line)
'''
plt.legend(loc="best")
plt.title("WRF Domain",size=18)
#plt.plot(133.1017)

## save domain by pdf and png
plt.savefig("domain-china-4km.pdf", bbox_inches="tight",edgecolor="none")
#plt.savefig("domain-test.png", bbox_inches="tight", edgecolor="none")

# print each domain center lon lat
for i in range(max_dom):
    print cenlon[i], cenlat[i]
