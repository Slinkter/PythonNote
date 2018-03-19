# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:39:54 2018

@author: Slinkter
"""

#3.1 Tuplas
tupla = (1,2,3)
print(tupla)
print(type(tupla))

tupla_texto = ('aaaaa','bbbbb','ccccc')
print(tupla_texto)
print(type(tupla_texto))

for element in tupla_texto:
    print(element)
#3.2 Lista
lista_numero = [0,1,2,3,4,5,6]
lista_texto  = ['aaa','bbb','ccc']
lista_alfnum = [1,'aaa',2]
print(lista_numero,'\n',lista_texto,'\n',lista_alfnum)

lista_numero.append(7)
lista_texto.append('dddd')
lista_alfnum.append('soy texto')

lista_numero.pop()
lista_texto.pop()
lista_alfnum.pop()

lista_numero.extend(lista_texto)
lista_numero
lista_numero.remove('aaa')

lista_countar = [1,1,1,1,2,2,2,5,5,5,5,5,5,5,8,8,8,8]
print(lista_countar.count(8))
print(lista_countar.count(1))

lista_ordernar =[21,5,53,78,44,19]
lista_ordernar.sort()
print(lista_ordernar)

lista_ordernar.sort(reverse=True)
print(lista_ordernar)

#3.4diccionarios
autores = {'libro 1' : 'Antonio Simon' , 'Libro 2' :'Alien Carst ' , 'Libro 3' : 'Hurter one'}
print(autores['libro 1'])
print(autores.keys())
print(autores.values())
autores.get('libro 1')

diccionario = {'libro 1':1000}
autores.update(diccionario)
autores
diccionario= autores.copy()

diccionario.clear()
#3.5 Funciones
import random
numero = random.randint(50,100)
print(numero)

from math import sqrt 
n = sqrt(25)
print(n)