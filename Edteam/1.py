datoA = int(input("Ingresar un numero : "))
datoB = int(input("Ingresar otro numero : "))

print(datoA + datoB)

if(datoA>datoB):
    print("los datos son mayor a cero")



#2.6 Ciclo While
x = 1 
while(x<10):
    print(x)
    x+=1
    
y = 10 
while(y>0):
    print(y)
    y-=1
    
#2.7 Ciclo For
x = 1 
for x in range(1,10):
    print(x)

texto = 'abcdef'
for palabra in texto:
    print(palabra)
    
dato = ["dato1","dato2","dato3"]
for x in dato:
    print(x)
    
#2.8 Funciones
def saludo():
    print("hola mundo")

saludo()

def cuadrado(z):
    print(z*z)

cuadrado(10)
    


