# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:42:26 2017

@author: Asus
"""

mi_diccionario = { }
mi_diccionario['primer_elemplo']= 'Hola'
mi_diccionario['segundo'] = 'Adios'

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['Psicologia'] = 7
calificaciones['Web']=9
calificaciones['Base de datos']=10

for key in calificaciones:
    print(key)
    pass
for value in calificaciones.values():
    print(value)
    pass
for key,values in calificaciones.items():
    print('llave : {}, valor :{} '.format(key,values))
    pass



    
    
