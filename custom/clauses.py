#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:47:53 2020

@author: abhijithneilabraham
"""

class Clause:
    def __init__(self):
        self.clauses={("find","search for","what","get me","which","show"):"select {} in {}",
                      ("how many","number of","who all","how much","sum of","total"):"count {} in {}",
                      ("instances","count"):"count {} in {}",
                      }
        self.int_clauses={ ("how many","number of","who all","how much","sum of","total"):"sum of {} in {}",
                           ("max","maximum","highest","biggest","most"):"maximum of {} in {}",
                           ("min","minimum","lowest","smallest","least"):"minimum of {} in {}",
                           ("average","mean of"):"average of {} in {}"
                           }

    def adapt(self,q,inttype=False):
        clauses=self.clauses
        int_clauses=self.int_clauses
        if inttype:
            for clause in int_clauses:
               if any(i in q for i in clause):
                   return int_clauses[clause]
            
        else:
            for clause in clauses:
                if any(i in q for i in clause):
                    return clauses[clause]
    
            
a=Clause().adapt("how many instances of run is there",True) 
print(a)
        