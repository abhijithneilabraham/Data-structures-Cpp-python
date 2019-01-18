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
        we can only anipulate the characters ,since the string is immutable
        '''

    def transform(self,original,code):
        msg=list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j=ord(msg[k])-ord('A')
                msg[k]=code[j]
                return ''.join(msg)
            
    def encrypt(self,message):
        return self.transform(message,self.forward)
    def decrypt(self,message):
        return self.transform(message,self.backward)
if __name__=='__main__':
    cipher=CaesarCipher(3)
    message="THE NAME IS ABHIJITH.AND IT IS HERE TO STAY."
    coded=cipher.encrypt(message)
    print(coded)
    answer=cipher.decrypt(coded)
    print(answer)

                