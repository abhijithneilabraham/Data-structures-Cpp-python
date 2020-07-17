#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:06:59 2020

@author: abhijithneilabraham
"""


from eywa.nlu import Classifier




class Clause:
    def __init__(self):
        self.clauses={
                      ("find","search for","what","get me","which","show"):"select {} in {}",
                      ("how many","number of","who all","how much","sum of","total"):"count {} in {}",
                      ("instances","count"):"count {} in {}"
                     
                      }
        self.int_clauses={ ("max","maximum","highest","biggest","most"):"maximum of {} in {}",
                      ("min","minimum","lowest","smallest","least"):"minimum of {} in {}",
                      ("average","mean of"):"average of {} in {}"}
    def adapt(self,q,inttype=False,priority=False):
        clf = Classifier()
        clauses=self.clauses
        int_clauses=self.int_clauses
        clauses.update(int_clauses)
        for i,tup in enumerate(clauses.items()):
            clause=tup[0]
            clf.fit(clause,clauses[clause])
            if inttype and priority:
                clf.fit(("how many","number of","who all","how much","sum of","total"),"sum of {} in {}")
            
        return clf.predict(q)
    
a=Clause()
print(a.adapt("find the type of cancer in men",True,True))
            

    