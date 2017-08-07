
name = 1
if not isinstance(name,str):
    name = "S/1N"
    
print("Mi nombre es " + name)



name = ""
if not isinstance(name,int):
    name = "no es numero"
print ("mi numero es :" + name )



import sys
num = sys.argv[0]

if num.isdigit():
    num = int(num)
else:
    print ("el argumento solo puede contener uno numero")
    sys.exit(-1)
    
try:    
    print("mi nombre es " + name )
except TypeError :
    print("mi nombre es S/N")
    
    
try:
    print("Hola mi nombre es : " + {})
except TypeError as error1:
    print("se Capturo el error : {}".format(error1))
    print("no se puede usar texto con estrofa")
    
    