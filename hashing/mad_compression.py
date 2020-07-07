#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 23:00:42 2019

@author: abhijithneilabraham
"""
from random import randrange
#using multiply add and divide compression
class Mapbase:
    def __init__(self,cap=11,p=109345121):
        self.table=cap*[None]
        self.n=0
        self.prime=p
        self.scale=1+randrange(p-1)
        self.shift=randrange(p)
        #incomplete