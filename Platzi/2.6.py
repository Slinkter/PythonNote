# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:45:30 2017

@author: Asus
"""

i = 0 
while i < 30:
    print(i)
    i=i+1
    
import random
    
    
def run():
    number_found = False
    rango = int(input("Ingresar el # numero de random : "))
    
    random_number = random.randint(0,rango)
    
    while not number_found:
        number = int(input("Intenta un número:"))
        
        if number == random_number:
            print("Felicidades ha encontrado el número")
            number_found  = True
        elif number> random_number:
            print("el numero es mas pequño")
        else:
            print("El número es mas grande")
            
    
if __name__== '__main__':
    run()
    