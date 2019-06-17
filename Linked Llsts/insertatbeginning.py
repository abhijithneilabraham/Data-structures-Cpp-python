#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:58:12 2019

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
    def insert(self,data):
        newdata=Node(data)
        newdata.nextval=self.headval
        self.headval=newdata
list1=linkedlist()
list1.headval=Node("February")
month3=Node("March")
list1.headval.nextval=month3
month1="January"
list1.insert(month1)
list1.listprint()

        
        
        
        