#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 01:53:26 2019

@author: abhijithneilabraham
"""
A=[]
def sort(A):
    for i in A:
        if A[i]<A[i-1]:
            A[i],A[i-1]=A[i-1],A[i]
    return A
print(sort([1,2,3]))