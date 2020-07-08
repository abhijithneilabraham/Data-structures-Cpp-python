#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:47:53 2020

@author: abhijithneilabraham
"""

class Clause:
    def __init__(self,q,min_kwd=None,max_kwd=None,avg_kwd=None):
        self.which_are_clauses=["find","search for","what","get me","which","show"]
        self.how_many_clauses=["how many","number of","who all","how much","sum of","total"]
        self.count_clauses=["instances","count"]
        self.max_clauses=["max","maximum","highest","biggest","most"]
        self.min_clauses=["min","minimum","lowest","smallest","least"]
        self.avg_clauses=["average","mean of"]
        self.inttype=False
    def adapt(self):
        print(self.q)
        if self.min_kwd:
            return "min"
        elif self.min_kwd:
            return"max"
            
a=Clause(5).adapt() 
        