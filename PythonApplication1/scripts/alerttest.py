# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import codecs
import chardet
import xml.dom.minidom
#sys.setdefaultencoding( "utf-8" )
#info = "F:\\projects\\XML\\ALERT\\0910\\"
info     = 'D:\\Data\\XML\\'
listfile = os.listdir(info)
filename = codecs.open(info+'alert.txt','w','utf-8')
ss = 'Ô¤¾¯ÐÅÏ¢'
print chardet.detect(ss)
ss = ss.decode('KOI8-R')
ss = ss.encode('utf-8')
print chardet.detect(ss)

for line in listfile:
    print line
    if line[-4:] == ".xml":
        dom = xml.dom.minidom.parse(info+line)
        alert = dom.documentElement
        sen  = alert.getElementsByTagName('sender')[0]
        sender = sen.childNodes[0].data
        filename.write(sender,)
        sendt = alert.getElementsByTagName('sendTime')[0]
        sendtime = sendt.childNodes[0].data
        filename.write(sendtime)
        print chardet.detect(ss)
        filename.write(ss)
        filename.write("\n")
        mess = alert.getElementsByTagName('description')[0]
        message = mess.childNodes[0].data

for index in range(len(message)):
    filename.write(message[index])
    if ((index!=0) and (index%70 ==0)):
        filename.write("\n")
filename.write("\n")
filename.write("\n")