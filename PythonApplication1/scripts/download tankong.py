# -*- coding: utf-8 -*-
# ���ߣ�MCSǿ
# ���ܣ���������̽������
# �����������������������֮�ã��������ݱ�����������֮������;������ԭ��վ
#       ֮Լ�����ɴ�������һϵ�а�Ȩ�ͷ������⣬����������һ�Ų��е�������Σ�
# �����������������谲װPython���Լ� Beautiful Soup 4 ��

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import calendar
import os
import time

class sounding(object):
    def __init__(self, year, month, dayhourfrom, dayhourto, stnm, region='seasia', format='TEXT%3ALIST'):
        self.mainpage = 'http://weather.uwyo.edu/cgi-bin/sounding'
        self.url = ('{mainpage}?region={region}&TYPE={type}&YEAR={year}'
                    '&MONTH={month:0>2}&FROM={dayhourfrom}&TO={dayhourto}'
                    '&STNM={stnm}').format(mainpage=self.mainpage, region=region,
                                           type=format, year=year, month=month,
                                           dayhourfrom=dayhourfrom,
                                           dayhourto=dayhourto, stnm=stnm)
        self.session = requests.Session()
        self.UA = ("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, "
                   "like Gecko) Chrome/27.0.1453.116 Safari/537.36")
        self.headers = {"User-Agent": self.UA, "Host": "http://weather.uwyo.edu/"}
        html = self.session.get(self.url, headers=self.headers).text
        self.soup = BeautifulSoup(html, "lxml")

    def writer(self, path='E:\\SoundingData'):
        results = [pre.text for pre in self.soup.find_all(['h2', 'pre'])]
        h2 = results[0:-2:3]
        sounds = results[1:-1:3]
        dt = [datetime.strptime(i[-15:], '%HZ %d %b %Y').strftime('%Y-%m-%d_%HZ')
              for i in h2]
        for t, head, sound in zip(dt, h2, sounds):
            with open(os.path.join(path, '{}.txt'.format(t)), 'w') as f:
                f.write(head)
                f.write(sound)


if __name__ == '__main__':
    # ����ʵ��д��, ֱ��ָ��, writer�е�path����ָ�����ݴ�ŵ�·��,
    # �����ָ��ʹ��Ĭ��ֵE:\\SoundingData
    sounding(year=2016, month=7, dayhourfrom='0100', dayhourto='0212', stnm=58238).writer()


    # ����Ϊ��λ���أ�ѭ��һ�ξͽ�һ�������������غ�
    # station = 58238  # վ���
    # years = [2016]  # ����б�����д�� [2006, 2007, 2008, 2009] ���� rane(2006, 2010)
    # months = [7]  # �·��б�����д�� [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12] ���� range(1, 13)
    # for year in years:
    #     for month in months:
    #         dayNums = calendar.monthrange(year, month)[1]
    #         sounding(year=year, month=month, dayhourfrom='0100',
    #                  dayhourto='{}12'.format(dayNums), stnm=station).writer()