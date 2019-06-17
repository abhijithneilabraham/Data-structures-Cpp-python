#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:23:19 2019

@author: abhijithneilabraham
"""
#Defining nodes  with current and next data values
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
#defining linkedlist class
class linkedlist:
    def __init__(self):
        self.headval=None
list1=linkedlist()
list1.headval=Node("January")
month2=Node("February")
month3=Node("March")
#Linking first node to the second node
list1.headval.nextval=month2
month2.nextval=month3
print(month3.dataval)