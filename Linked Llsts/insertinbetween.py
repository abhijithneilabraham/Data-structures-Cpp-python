#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:52:33 2019

@author: abhijithneilabraham
"""

class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def insert(self,middleval,data):
        newdata=Node(data)
        
        