# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:20:08 2017

@author: Asus
"""

print(range(5,0,1))
print(range(5,40,5))

for i in range(5):
    print(i)

for i in range(5):
    print("Hola Mundo")
    
for i in range(30):
    if i % 3 != 0 :
        continue
    else:
        print(i**2)
        
r = "ferrocarril"
for letter in r : 
    print(letter)