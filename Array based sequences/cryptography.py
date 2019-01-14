#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 02:03:34 2019

@author: abhijithneilabraham
"""

class CaesarCipher:
    def __init__(self,shift):
        encoder=[None]*26
        decoder=[None]*26
        for k in range(26):
            encoder[k]=chr((k+shift)%26 + ord('A')) #ord returns the ascii value. 
            '''
            this encoder shifts the character by the parameter shift. Which means,Instead of starting from A,
            it starts from D ,if shift is given value 3
            '''
            decoder[k]=chr((k-shift)%26 + ord('A'))
            self.forward=''.join(encoder)
            self.backward=''.join(decoder) #both of these lines just joining the characters into string.
            '''
            we can only  manipulate the characters,since string is immutable
            '''
            