# -*- coding: utf-8 -*-
#ejemplo 1
pares = []
for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)

print(pares)

even = [num for num in range(1,31) if num % 2 == 0]
print(even)
#ejemplo 2
cuadrados = {}
for x in range(1,11):
    cuadrados[x] = x**2
print(cuadrados)

squares = {x:x**2 for x in range(1,11)}
print(squares)
