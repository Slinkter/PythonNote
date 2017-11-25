# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:35:23 2017

@author: John
"""

#Factorial -

def f_factorial(number):
    if number == 0 :
        return 1
    
    rpta = number*f_factorial(number -1)
    
    return rpta

if __name__=='__main__':
    numero = int(input('Ingresar numero : '))
    resultado = f_factorial(numero)
    print ("el factorial de {} es {}".format(numero,resultado))
    