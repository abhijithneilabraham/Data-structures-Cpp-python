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
        