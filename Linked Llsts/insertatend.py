#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:37:01 2019

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
        if self.headval is None:
            self.headval=newdata
            return
        last1=self.headval
        while(last1.nextval):
            last1=last1.nextval
        last1.nextval=newdata
                
list1=linkedlist()
list1.headval=Node("January")
month2=Node("February")
list1.headval.nextval=month2
list1.insert("March")
list1.listprint()
        