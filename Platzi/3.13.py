# -*- coding: utf-8 -*-
#s = {1,2,3}
#t = {3,4,5}
#resutlado = s.intersection(t)
#print (resutlado)
#print("hola")

s = set([1,2,3])
t = set([3,4,5])

union = s.union(t)
print("la unión es : " ,union)

interccion = s.intersection(t)
print("la intercción es : " ,interccion)

diferencia = s.difference(t)
print("la diferencia es :",diferencia)
