#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:35:10 2019

@author: abhijithneilabraham
"""

def selectionsort(arr):
    for i in range(len(arr)):
        minim=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minim]:
                minim=j
        arr[minim],arr[i]=arr[i],arr[minim]
    return arr
print(selectionsort([2,4,7,3,2]))
        
    