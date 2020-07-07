#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:35:47 2019

@author: abhijithneilabraham
"""

a=[3,4,1,2,5,6]


def bubblesort(a):
    x=-1
    flag=1
    while flag:
        flag=0
        x+=1
        for i in range(1,len(a)-x):
            
            
            if a[i]<a[i-1] :
                a[i],a[i-1]=a[i-1],a[i]
                flag=1
            
    return a
print(bubblesort(a))