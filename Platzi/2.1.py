# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 17:35:42 2017

@author: Ta
"""

def factorial(number):
    if number == 0:
        return 1
    return number*factorial(number-1)
    
    

if __name__ == '__main__':
    number = int(input("Ingresar un número:"))
    result = factorial(number)
    print ("El resultado es  {}".format(result))
    
