# !/usr/bin/python
# -*- coding: utf-8 -*-
# author: KOBEXFFX
# Python 2.7.11
# DOWNLOAD HTML PAGES FROM BAIDU TIEBA
#====================import packages=========================
import urllib
#====================define global vars======================
http      = 'http://tieba.baidu.com/p/100000000'
urls = [http + str(i) for i in range(10)]
path = './HTML/'
#====================define functions========================
def downloadHtml(url):
    f = urllib.urlopen(url)
    data = f.read()
    page = open(path+url[-10:] + '.html','wb')
    page = page.write(data)

def main():
    for url in urls:
        downloadHtml(url)

#====================execute program=========================
if __name__ == '__main__':
    main()