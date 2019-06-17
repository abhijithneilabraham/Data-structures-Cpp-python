#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:30:12 2019

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
    def remove(self,node):
        head=self.headval
        if head is not None:
            if head.dataval==node:
                    self.headval=head.nextval
                    head=None
                    return
        while head is not None:
            if head.dataval==node:
                break
            prev=head
            head=head.nextval
        if head==None:
            return
list1=linkedlist()
list1.headval=Node("January")
list1.headval.nextval=Node("February")
list1.listprint()
list1.remove("February")
list1.listprint()
            
        