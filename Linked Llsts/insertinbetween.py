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
    def insert(self,middlenode,data):
        if middlenode is None:
            print("The mentioned node is absent")
            return       
        newdata=Node(data)
        newdata.nextval=middlenode.nextval
        middlenode.nextval=newdata
list1=linkedlist()
list1.headval=Node("January")
month3=Node("March")
list1.nextval=month3
list1.insert(list1.headval.nextval,Node("february"))
list1.listprint()
        