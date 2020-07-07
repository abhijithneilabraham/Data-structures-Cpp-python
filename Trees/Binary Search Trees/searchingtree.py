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
        if val<self.data:
            if self.left is None:
                print(str(val)+'is not found')
                return str(val)
            return self.left.findval(val)
        elif val>self.data:
            if self.right is None:
                print(str(val)+'Not found')
                return str(val)
            return self.right.findval(val)
        else:
            print(str(val)+'is found')
                        
        
                
        
root=Node(20)
root.insert(30)
root.insert(10)
root.insert(5)
root.findval(10)
        
        
                