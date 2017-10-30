# -*- coding: utf-8 -*-
keys = {
        'a':'1',
        'b':'2',
        'c':'3',
        'd':'4',
        'e':'5',
        'f':'6',
        'g':'7',
        'h':'8',
        'i':'9',
        'j':'10',
        'k':'11',
        'l':'12',
        'm':'13',
        'n':'14',
        'o':'15',
        'p':'16',
        'q':'17',
        'r':'18',
        's':'19',
        't':'20',
        'u':'21',
        'v':'22',
        'w':'23',
        'x':'24',
        'y':'25',
        'z':'26',
        }
# Función segundaria
def encriptar(mensaje):
    m_recibido = mensaje.split(' ')  # oración --> lista
    l_mensaje = []                   # lista vacia
    for m in m_recibido:             # recibir cada lista[m]
        cadena = ' '                      # Cadena
        for letra in m:              # ejemplo Hola
            cadena =  keys[letra]
            l_mensaje.append(cadena)
    return ''.join(l_mensaje)

# Función segundaria
def desencriptar(mensaje):
    m_recibodo =  mensaje.split(' ') # Recibir el código
    l_mensaje = []                   # Lista vacia

    for palabra in m_recibodo:       # recibir cada lista[palabra]
        cadena = ' '
        for letter in word:
            for key,value in keys.items():
                if value == letter:
                    cadena = cadena + key
        l_mensaje.append(cadena)        
    return ' '.join(l_mensaje)

# Función primaria
def run():
    while True:
        print('''
        PROGRAMA PARA encriptar Y desencriptar MESAJES
            Escoja comando :
             [e]ncriptar
             [d]esencriptar
             [s]alir
        ''')
        comando = str(input("Ingresar comando : "))
        if comando == 'e':
                mensaje = str(input("Ingresar tu mensaje para encriptar : "))
                resultado = encriptar(mensaje)
                print(resultado)
        elif comando == 'd':
                mensaje = str(input("Inresar tu mensaje para desencriptar :"))
                resultado1 = desencriptar(mensaje)
                print(resultado1)
        elif comando == 's':
                print("comando de salir")
                break

if __name__=='__main__':
    run()

#
