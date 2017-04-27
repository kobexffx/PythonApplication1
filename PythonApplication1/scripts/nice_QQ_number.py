# !/usr/bin/python
# -*- coding: utf-8 -*-
# author : kobexffx
# version: Python 2.7.11
# goals  : get nice QQ number owners 
#====================import packages=========================
import pandas as pd
#====================define global vars======================
names  = ['xiaoyun','xiaohong','xiaoteng','xiaoyi','xiaoyang']
QQlist = ['88888','5555555','11111','1234321','1212121']
#data = dict(zip(name,QQ)) 
data = {'name':names,'QQ':QQlist}
frame = pd.DataFrame(data,index = range(1,6))
frame.index.name = 'number'

#====================define functions========================
def finduserQQ(username):                                    # require for user's QQ number
    for ii in range(1,6):                                      
        if username == frame.get_value(ii,'name'):             
            print frame.get_value(ii,'QQ')                     
            return                                             
        elif username !=  frame.get_value(ii,'name'):          
            return True                                        
                                                               
def findniceQQ(length):                                      # find who has nice QQ
    niceQQ = []
    owner  = []
    for ii in range(1,6):
        for qq in QQlist:
            if len(qq) <= length:
                if qq == frame.get_value(ii,'QQ'):
                    owner.append(frame.get_value(ii,'name'))
                    niceQQ.append(qq)
    print 'who has the nice QQ number:',owner

def main():
    length   = 5                                             # define nice QQ length 
    username = raw_input('please input your name:')
    if not(finduserQQ(username)):
        findniceQQ(length)
    elif finduserQQ(username):                               # allow to input again once
        username = raw_input('please refresh your name:')
        finduserQQ(username)
        findniceQQ(length)

#====================execute program=========================
if __name__ == '__main__':
    main()