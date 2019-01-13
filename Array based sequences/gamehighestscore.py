#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 01:43:25 2019

@author: abhijithneilabraham
"""

class GameEntry:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_score(self):
        return self.score
    def get_name(self):
        return self.name
    def __str__(self):
        return '({0}{1})'.format(self.name,self.score) 
    '''
    the string.format uses these positional arguments 
    to display respectively in the position of the {0} and {1}
    '''