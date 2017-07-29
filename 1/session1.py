print ("Hola mundo")

x = 1 
if x == 1 :
    print ("x es 1")

mi_int = 1
mi_float = 7.6
mi_complex = 3.14j

type(mi_complex)
    

mi_lista = []
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
print (mi_lista)

mi_tupla = (1,"Luis ",True)
print (mi_tupla[2])


A1 = list(range(1,5,1))
A2 = list(range(50))


String_simple = 'permite usar comillas "doble"'
String_doble  = "permite usar comillas 'simple'"
String_triple = '''permite escribe varias lineas"asd'das dsa ''' 

print (String_simple[1:5])

variable1 = "python"
print(len(variable1))
print(variable1[0])#1
print(variable1[1])#2
print(variable1[2])#3
print(variable1[3])#4
print(variable1[4])#5
print(variable1[5])#6

print(variable1.upper())

mi_diccionario = {"nombre" : "Luis" , "Edad":25,"Apellido":"Cueva"}
print (mi_diccionario.keys())
print(mi_diccionario["nombre"])
print(mi_diccionario["Edad"])

numero = 3 + 4 - 2 * 5 / 2 ** 9 % 1
print (numero)
import math
print(math.sqrt(numero))

texto = 'esto es comillas simplre' + " y " + "estas son comillas doble "
print (texto)

texto = "comillas"*2
print (texto)

bajos = [0,1,2,3,4,5,6]
altos = [7,8,9,10,11,12]

numeros = bajos + altos 
print (numeros)

lista_nombre  =["juanito", "pepito" , "jaimito" ]
print(lista_nombre)

print("juanito" in lista_nombre)

##########################
#   CONTROL DE FLUJO IF  
##########################

x = 6 
if x < 0 :      
    print ("x es negativo")
elif x == 0 :
    print ("x es cero")
elif x > 0:
    print ("x es positivo")
else :
    print ("es mayor que 5")
    
##########################
#   CONTROL DE FLUJO for
##########################
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]   
for numero in numeros[0:12]:
    print (meses[numero])
    
##########################
#   CONTROL DE FLUJO for
########################## 
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]   
contador = 0
while contador < 12 :
    print (meses[contador])
    contador = contador +1

