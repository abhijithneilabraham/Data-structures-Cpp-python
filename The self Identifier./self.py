#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 23:43:40 2019

@author: abhijithneilabraham
"""

class CreditCard:
    def __init__(self,customer,bank,acnt,limit):
        self.customer=customer
        self.bank=bank
        self.account=acnt
        self.limit=limit
        self.balance=500
    def customer_name(self):
        
        return self.customer
    def bank_details(self):
        return self.bank
    def account_details(self):
        self.account
    def get_limit(self):
        return self.limit
    def charge(self,price):#price is recieved to the card
        if price+self.balance>self.limit:
            return False
        else:
            self.balance+=price
            return True
    def payment(self,amount):
        self.balance-=amount
    def mybalance(self):
        return self.balance
    '''
    self :

self represents the instance of the class. 
By using the "self" keyword we can access the attributes and methods of the class in python.

__init__ :

"__init__" is a reseved method in python classes.
 It is known as a constructor in object oriented concepts. This method called when
 an object is created from the class and it allow the class to initialize the attributes of a class.
 '''
'''
 Now I am gonna test the class
 the tests are enclosed within a conditional if __name__=='__main__' 
which makes it to be execuuted as the main program
 '''
if __name__=='__main__':    
    wallet=CreditCard('Abhijith','SBI',12002100,10000)#constructor to create a new creditcard instance
    val=100
    wallet.charge(val)
    print(wallet.mybalance())
    wallet.payment(300)
    print(wallet.mybalance())
    