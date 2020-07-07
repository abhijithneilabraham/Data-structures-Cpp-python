#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 01:57:41 2019

@author: abhijithneilabraham
"""



'''
using a recursive algorithm,named binary search
Trying to efficiently locate a target element within a sorted sequence of n elements
'''

def Binary(data,target ,low ,high):#low and high are array indices
    if low>high:         
        return False
    else:
        mid=(low+high)//2 #double slash in python rounds off to nearest whole number.
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return Binary(data,target,low,mid-1)
        else:
            return Binary(data,target,mid+1,high)
        
        
data=[3,7,6,2,9,11,13]
print(Binary(data,10,0,6))
            
'''
this program further slices data into midpoints and midpoints and checks if the given integer is there.
This algorithm runs in O(n) time.
    '''
    