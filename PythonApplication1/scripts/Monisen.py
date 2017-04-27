# !/usr/bin/python
# -*- coding: utf-8 -*-
# author: Ye Fe
# Look for N Monisen number
#====================import packages=========================
from math import sqrt
#====================define functions=========================
prime_list   = [2]
monisen_list = []
monisen_num  = 5

def isPrime(x):
    x_sqrt  = int(sqrt(x))
    isPrime = False
    for j in prime_list:
        if j <= x_sqrt:
            if x % j == 0:
                break 
        else:
            isPrime = True
            break
    else:
        isPrime = True
    return isPrime

def isMonisen(x):
    isMonisen = False
    for j in prime_list:
        if 2**j-1 == x:
            isMonisen = True
            break
        elif 2**j-1 > x :
            break
    return isMonisen

def monisen(n):
    i    = 3
    step = 2
    while(len(monisen_list) < monisen_num):
        if (isPrime(i)):
            prime_list.append(i)
            if (isMonisen(i)):
                monisen_list.append(i)
        i += step
    return monisen_list[n-1]

def main():
    print 'pleas input number:',monisen(input())
#=====================execute program=======================================
if __name__ == '__main__':
    main()
