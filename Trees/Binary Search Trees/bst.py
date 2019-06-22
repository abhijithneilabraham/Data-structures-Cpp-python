#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 21:56:26 2019

@author: abhijithneilabraham
"""
#First we create a root node
class Node:
    def __init__(self,data):
        self.leftt=None
        self.right=None
        self.data=data
    def printtree(self):
        print(self.data)
        
    def insert(self,data):
        if self.data:
            if self.data<data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif self.data>data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
                    