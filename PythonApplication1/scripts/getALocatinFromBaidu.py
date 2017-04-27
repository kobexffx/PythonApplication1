# !/usr/bin/python
# -*- coding: utf-8 -*-
# author : kobexffx
# version: Python 2.7.11
# goals  : GET LON&LAT FROM BAIDU INTERFACE
#====================import packages=========================
import requests
import urllib
import math
import re
import chardet
#====================define global vars======================
pattern_x=re.compile(r'"x":(".+?")')
pattern_y=re.compile(r'"y":(".+?")')
#====================define functions========================
def mercator2wgs84(mercator):
    #key1=mercator.keys()[0]
    #key2=mercator.keys()[1]
    point_x=mercator[0]
    point_y=mercator[1]
    x = point_x - 0.0065
    y = point_y - 0.006
    z = math.sqrt(x*x+y*y)-0.00002*math.sin(y*math.pi)  
    theta = math.atan2(y,x)-0.000003*math.cos(x*math.pi)
    lon = z*math.cos(theta)
    lat = z*math.sin(theta)

    x=lon/20037508.3427892*180
    y=lat/20037508.3427892*180
    y=180/math.pi*(2*math.atan(math.exp(y*math.pi/180))-math.pi/2)
    return (x,y)

def get_mercator(addr):
    quote_addr=urllib.quote(addr.encode('utf8'))
    city=urllib.quote(u'qiqihaershi'.encode('utf8'))
    province=urllib.quote(u'heilongjiangsheng'.encode('utf8'))
    if quote_addr.startswith(city) or quote_addr.startswith(province):
        pass
    else:
        quote_addr=city+quote_addr
    s=urllib.quote(u'beijing'.encode('utf8'))
    api_addr="http://api.map.baidu.com/?qt=gc&wd=%s&cn=%s&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk62300"%(quote_addr
,s)
    req=requests.get(api_addr)
    content=req.content
    x=re.findall(pattern_x,content)
    y=re.findall(pattern_y,content)
    if x:
        x=x[0]
        y=y[0] 
        x=x[1:-1]
        y=y[1:-1]
        x=float(x)
        y=float(y)
        location=(x,y)
    else:
        location=()
    return location

def main():
    value = raw_input('please input your location:')  
    codess = chardet.detect(value)
    codetype =  codess.get('encoding')
    value = value.decode(codetype)
    mercator=get_mercator(value)
    print "%s,%s,%s"%(value,mercator[0],mercator[1])
    if mercator:
        wgs=mercator2wgs84(mercator)
    else:
        wgs=('NotFound','NotFound')
    print "%s,%s,%s"%(value,wgs[0],wgs[1])
  
#====================execute program=========================
if __name__ == '__main__':
    main()