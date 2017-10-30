# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:21:43 2017

@author: Asus
"""


def palidrome(word):
    reversed_letter = []
    for letter in word : 
        reversed_letter.insert(0,letter)
    
    reversed_word = ''.join(reversed_letter)  
    
    
    if reversed_word == word :
        return True
    else:
        return False
    

if __name__=='__main__':
    word = str(input("Escribir una palabra, prohibido numeros :"))    
    resultado = palidrome(word)
    
    if resultado is True:
        print("{} si es ".format(word))
    else:
        print("{} no es ".format(word))

