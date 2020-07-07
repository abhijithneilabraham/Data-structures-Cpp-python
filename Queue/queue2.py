#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:01:19 2019

@author: abhijithneilabraham
"""

class Queue:
    def __init__(self):
        self.data=[]
    def insertq(self,dataval):
        if dataval not in self.data:
            self.data.insert(0,dataval)
            return True
        return False
    def deleteq(self):
        del(self.data[-1])
    def peek(self):
        return self.data
q=Queue()
q.insertq("Monday")
q.insertq("Tuesday")
q.insertq("wednesday")
print(q.peek())
q.deleteq()
print(q.peek()) 