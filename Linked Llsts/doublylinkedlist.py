#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:03:35 2019

@author: abhijithneilabraham
"""

class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.next=None
        self.prev=None
class doublylinked:
    def __init__(self):
        self.head=None
    def pushtofront(self,data):
        newdata=Node(data)
        newdata.next=self.head
        newdata.prev=None
        if self.head is not None:
            self.head.prev=newdata
        self.head=newdata
    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.dataval)
            printval=printval.next
list1=doublylinked()
list1.head=Node("January")
month2=Node("February")
list1.head.next=month2
list1.listprint()
list1.pushtofront("December")
list1.listprint()
