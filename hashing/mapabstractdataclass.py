#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:38:24 2019

@author: abhijithneilabraham
"""

class Map:
    def __init__(self):
        self.entrylist=list()
    def __len__(self):
        return len(self.entrylist)
   
    def add(self,key,value):
        ndx=self.findposition(key)
        if ndx is not None:
            self.entrylist[ndx].value=value
            return False
        else:
            entry=_MapEntry(key,value)
            self.entrylist.append(entry)
            return True
    def contains(self,key):
        ndx=self.findposition(key)
        return ndx is not None
    def valueof(self,key):
        ndx=self.findposition(key)
        assert ndx is not None,"Invalid map key"
        return self.entrylist[ndx].value
    def remove(self,key):
        ndx=self.findposition(key)
        assert ndx is not None, "Invalid map key."
        self.entrylist.pop(ndx)
    def iter(self):
        return iter(self.entrylist)
    def findposition(self,key):
        for i in range(len(self)):
            if self.entrylist[i].key==key:
                return i
        return None 
class _MapEntry:
    def __init(self,key,value):
        self.key=key
        self.value=value
mapping=Map()
mapping.add(1,1)
mapping.add(2,5)
mapping.add(3,9)
for entry in iter(mapping):
    print(entry.key)
print(len(mapping))
print(mapping.valueOf(1))

            
                
                
        