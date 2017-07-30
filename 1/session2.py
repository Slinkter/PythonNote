"se incia la rama test"
"Funciones"
def hola_usuario(username,greeting):
    print ("hello, %s, from my Function!, I wish you %s"%(username,greeting))
    
def func(a, nombre, c, d=1, e=2, *args, f, g=None, **kwargs):
    print(a, nombre, c, d, e, args, f, g, kwargs)
func(1, 2, 3, f=1)
    
def generica(*args,**Kwargs):
    print ("args : ",args )
    print ("kwargs : ",Kwargs)
    
generica(1, 2, 3, 4, 5, numero=1, lugar="Monterrey")

def externo():
    a = "existo en interno"
    b = 2
    c = 3
    def interno(varname):
        if varname == 'a':
            print (a)
        else:
            print ("...")
    return interno
        
def suma_parcial(func):
    def interno(a,b):
        func(a+b)
    return interno
 
def connect_db(func):
    def wrapper(*args,**Kwargs):
        db=None
        func(db,*args,**Kwargs)
@connect_db
def process(db,uid,gid):
    pass
 
from functools import singledispatch
@singledispatch
def fun(arg,verbose=False):
    if verbose:
        print ("let me just say",end = " ")
    print(arg)    
 
fun(1,verbose=True)     

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

fun("Joel", verbose=True)

###################################################
# Clases
###################################################























