#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 06:02:17 2020

@author: abhijithneilabraham
"""

class Fam:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    def add_dad(self,dadname):
        self.dadname=dadname
    def add_mom(self,momname):
        self.momname=momname
    def add_child(self,childname):
        self.childname=childname
    def childfullname(self):
        return self.childname+self.dadname
    
f=Fam("Puthenkandathil")
print(f)
f.add_dad("Bond")

f.add_child("James ")
print(f.childfullname())

class NewFam(Fam):
    def __init__(self,name):
        self.name=name
    def add_child(self,childname):
        self.childname=childname
    def add_dad(self):
        pass
    def childfullname(self):
        return "New child name is {} {}".format(self.childname,super().__str__())

nf=NewFam("Pulikkathara")
nf.add_child("Jason Bourne")
print(nf.childfullname())
        
        