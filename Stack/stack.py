#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:01:55 2019

@author: abhijithneilabraham
"""
class ArrayStack:
    def __init__(self):
        self.data=[]
    def len(self):
        return len(self.data)
    def isempty(self):
        return len(self.data)==0
    def push(self,e):
        self.data.append(e)
    def top(self):
        #returns the element at the top of stack but does not remove it.-top operation
        if self.isempty():
            return ValueError('stack is empty')
        return self.data[-1]
    def pop(self):
        
        if self.isempty():
            return ValueError('stack is empty')
        return self.data.pop()
s=ArrayStack()
s.push(5)
s.push(3)
print(s.pop())