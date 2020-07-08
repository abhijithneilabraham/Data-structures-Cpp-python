#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:47:53 2020

@author: abhijithneilabraham
"""

class Clause:
    def __init__(self,q,inttype=False):
        self.clauses={("find","search for","what","get me","which","show"):"select {} in {}",
                      ("how many","number of","who all","how much","sum of","total"):"count {} in {}",
                      ("instances","count"):"count {} in {}",
                      ("max","maximum","highest","biggest","most"):"maximum of {} in {}",
                      ("min","minimum","lowest","smallest","least"):"minimum of {} in {}",
                      ("average","mean of"):"average of {} in {}"}
        self.q=q
    def adapt(self):
        q=self.q
        clauses=self.clauses
        for clause in clauses:
            if any(i in q for i in clause):
                return clauses[clause]
            
            
a=Clause("how many").adapt() 
print(a)
        