# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:46:18 2017

@author: John
"""

print(10 == 10)
print('a' == 'a')
print('david' == 'davidad')


def f_say_hello(age):
    if age >18:
        print('Hola Señor')
    else:
        print('Hola niño')
        

if __name__ == '__main__':
    age = int(input("ingresar edad"))
    f_say_hello(age)