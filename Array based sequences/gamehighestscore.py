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
    