#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:27:47 2019

@author: abhijithneilabraham
"""

def good_fib(n):#this fibonacci will run on a much lesser time complexity
    if n<=1:
        return(n,0)
    else:
       a,b=good_fib(n-1)
       return (a+b,a)
for i in range(5):
    print(good_fib(i))