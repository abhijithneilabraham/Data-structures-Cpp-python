#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:47:53 2020

@author: abhijithneilabraham
"""

class Clause:
    def adapt(self,x):
        print(self.x)

# class Which(Clause):
#     def __init__(self,q,min_kwd=None,max_kwd=None,avg_kwd=None):
#         self.min_kwd=None
#         self.max_kwd=None
#         self.avg_kwd=None
#     def adapt(self,x):
#         print(x)
#         if self.min_kwd:
#             return "min"
#         elif self.min_kwd:
#             return"max"
            
a=Clause.adapt(5) 
        