#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:26:33 2019

@author: abhijithneilabraham
"""

"""
merge sort using python
"""
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left,right=mergesort(arr[:mid]),mergesort(arr[mid:])
    return(left, right, arr.copy)
def merge(left, right, merge):
    l1,r1=0,0
    while l1<len(left) and r1<len(right):
        if left[l1]<right[r1]:
            merged[l1+r1]=left[l1]
            l1+=1
        else:
            merged[l1+r1]=right[r1]
            r1+=1
    for l1 in range(l1,len(left)):
        merged[l1+r1]=left[l1]
    for r1 in range(r1,len(right)):
        merged[l1+r1]=right[r1]
    return arr
arr=[3,1,2,5,1]
print(mergesort(arr))
    