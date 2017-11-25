# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:49:34 2017

@author: John
"""

def run():
    number = int(input("Ingresar un numero"))
    rpta = f_es_primo(number)
    if rpta is True: 
        print('si es primo') 
    else:
        print('no es primo')
    
def f_es_primo(number):
    if number <2 :
        return False
    elif number == 2 :
        return False
    elif number > 2 and number% 2 == 0 :
        return False
    else:
        # number se testea desde el 3 para saber si primo 
        for i in range(3,number):  
            if number % i == 0:
                print( i,'si es divisible' ,number)
                return False
            else : 
                print( i,'no es divisible' ,number)
                return True
        
    

if __name__ == '__main__':
    run()
    