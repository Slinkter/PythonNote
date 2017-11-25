def run():
    print("convetir Dolares --> Soles")
    cantidad = float(input("Ingresar Cantidad :"))
    resultado = f_tipo_de_cambio(cantidad)
    print("${} dolares valen  ${} soles".format(cantidad,resultado))
    
def f_tipo_de_cambio(cantidad):
    dolar = 3.20
    return cantidad*dolar
    
if __name__ == '__main__':
    run()
    
   
