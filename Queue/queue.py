#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:15:32 2019

@author: abhijithneilabraham
"""
class ArrayQueue:
    default=10
    def __init__(self):
        self.data=[None]*ArrayQueue.default
        self.size=0
        self.front=0
    def len(self):
        return self.size
    def is_empty(self):
        return self.is_empty==0
    def first(self):
        if self.is_empty:
            raise ValueError('Queue is empty')
        return self.data[self.front]
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        answer=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size-=1
        return answer
    def enqueue(self,e):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avail=(self.front+self.size)%len(self.data)
        self.data[avail]=e
        self.size+=1
    def resize(self,cap):
        old=self.data
        self.data=[None]*cap
        walk=self.front
        for k in range(self.size):
            self.data[k]=old[walk]
            walk=(1+walk)%len(old)
        self.front=0
        