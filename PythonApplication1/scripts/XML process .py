# !/usr/bin/python
# -*- coding: utf-8 -*--
# author: Ye Fe
# XML Process & Output
#====================import packages=========================
import os,sys
import codecs
import chardet
import xml.dom.minidom
from xml.etree import ElementTree as ET
#====================read files==============================
path = 'D:\\Data\\XML\\'
filenames  = os.listdir(path)
input_file = []
for file in filenames:
    if file[-4:] == '.xml':
        input_file.append(file)
#====================data process============================
for ii in range(len(input_file)):
    print input_file[ii]
    print chardet.detect(input_file[ii])
    s = []
    per=ET.parse(path+input_file[ii],)
    p=per.findall('./')
    f = codecs.open('./XML/'+input_file[ii].split('.')[0]+'.TXT','w','utf-8')
    i = 0
    for parent in p:
        i = i + 1
        #f.write(parent.tag+':')
        #f.write(parent.text)
        text = parent.text
        s.append(parent.tag+':')
        s.append(parent.text)
        #print parent.tag,':',parent.text
        
        for child in parent.getchildren():
            #f.write(child.tag+':')
            #f.write(child.text)
            s.append(child.tag+':')
            s.append(child.text)
            #print child.tag,':',child.text
            
            for grand in child.getchildren():
                #f.write(grand.tag+':')
                #f.write(grand.text)
                s.append(grand.tag+':')
                s.append(grand.text)
                #print grand.tag,':',grand.text
    
    for i in range(len(s)):
        if s[i] != None:
            f.write(s[i]+'\n')
            print s[i],type(s[i])
    f.close()
    
    #x = xml.dom.minidom.parse(path+input_file[ii])
    #root = x.documentElement
    #root_name.append(root.nodeName)
    #for tag in 
    #identifier_list  = root.getElementsByTagName(TagName[i])
    #identifier_value = identifier_list[0].firstChild.data
    #identifier_name.append(identifier_list)

