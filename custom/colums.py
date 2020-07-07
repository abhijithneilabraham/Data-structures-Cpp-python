#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:14:54 2020

@author: abhijithneilabraham
"""

class Coltype:
    def inttype(self,val):
        self.val=int(val)
        return self.val
    def strtype(self,val):
        self.val=str(val)
        return self.val
    def convert(self,val,typ):
        if typ=="int":
            return self.inttype(val)
        else:
            return self.strtype(val)
        
print(type(Coltype().convert("5","str")))