# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:58:55 2017

@author: Asus
"""

def binary_search(numbers,number_to_find,low,high):
    if low > high:
        return False
    mid = int((low + high)/2)
    
    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid]>number_to_find:
        return binary_search(numbers,number_to_find,low,mid-1)
    else:
        return binary_search(numbers,number_to_find,mid+1,high)
        


if __name__ == '__main__':
    numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]
    number_to_find = int(input("Ingresar numero :"))
    resultado = binary_search(numbers,number_to_find,0,len(numbers)-1)
    
    if resultado is True :
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")
    
    
    
    
    
    