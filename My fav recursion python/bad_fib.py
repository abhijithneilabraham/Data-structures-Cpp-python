#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 03:04:30 2019

@author: abhijithneilabraham
"""

'''
the usual fibonacci
'''
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-2)+ fib(n-1)
for i in range (5):
    print(fib(i))    