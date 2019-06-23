#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:42:08 2019

@author: abhijithneilabraham
"""

#implementing a search tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
    def findval(self,val):
        if val==self.data or val==self.left or val==self.right:
            print(str(self.data)+'is found')
        else:
            while self.left is not None and self.right is not None :
                self.left.findval(val)
                self.right.findval(val)
                
        
root=Node(20)
root.insert(30)
root.insert(10)
root.insert(5)
root.findval(5)
        
        
                