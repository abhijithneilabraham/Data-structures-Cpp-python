#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 02:02:52 2019

@author: abhijithneilabraham
"""

class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
stack=Stack()
stack.add("One")
stack.add("Two")
stack.add("Three")
print(stack.peek())