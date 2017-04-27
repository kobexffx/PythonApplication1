# !/usr/bin/python
# -*- coding: utf-8 -*-
# author: Ye Fe
# count the amount of A-Z in string
#====================import packages=========================
import string
#====================define functions========================
def countchar(s):
   s = s.lower()                      
   l = []
   for i in string.lowercase:
      l.append(s.count(i))            
   return l                           
#====================execute program=========================
if __name__ == "__main__":
     print 'please input your string:'
     str = raw_input()
     print countchar(str)    