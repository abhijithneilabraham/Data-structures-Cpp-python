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
        return '({0},{1})'.format(self.name,self.score) 
    '''
    the string.format uses these positional arguments 
    to display respectively in the position of the {0} and {1}
    
    '''
class ScoreBoard:
    def __init__(self,capacity=10):#scoreboard stores 10 elements
        self.board=[None]*capacity
        self.n=0
    def getitem(self,k):
        return self.board[k]
    def __str__(self):
        return '\n'.join(str(self.board[j]) for j in range(self.n)) #self creates n and iterates through n 
    def add(self,entry):
        score=entry.get_score()
    good=self.n<len(self.board) or score>self.board[-1].get_score()
        
        