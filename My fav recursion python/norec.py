#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:37:03 2019

@author: abhijithneilabraham
"""

'''
fibonacci without recursion

'''
def fib(n):
    k=0
    l=1
    for i in range(1,n):
        j=k+l
        k,l=l,j
    return j
print(fib(5))    
        
        