#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:59:14 2019

@author: abhijithneilabraham
"""

class Node:
    def __init__(self,dataval=None):
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
list1=linkedlist()
list1.headval=Node("January")
month2=Node("February")
month3=Node("March")
list1.headval.nextval=month2
month2.nextval=month3
list1.listprint()
                
