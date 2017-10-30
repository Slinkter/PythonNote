# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:52:31 2017

@author: Asus
"""

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
 
def prueba(mensaje):
    palabras = mensaje.split(' ')
    print("{} -->palabras - linea 39".format(palabras))
    lista_1 = []
    for palabra in palabras:
        print("{}  -->palabra - linea 42".format(palabra))
        cadena = ''
        for p in palabra:
            print("{} --> p - linea 45".format(p))
            cadena = cadena + keys[p]
            print("{} --> cadena - linea 44".format(cadena))
            lista_1.append(cadena)
            
    return " ".join(lista_1)

def cypher(message):
    words = message.split(' ')
    cypher_message = []
    
    for word in words:
        cadena = ''
        for letter in word:
            cadena = cadena + keys[letter]
            cypher_message.append(cadena)       
    
    return " ".join(cypher_message)    
     
 
def decipher(message):
    words = message.split(' ')
    decipher_message = []
    
    for word in words:
        decipher_word = ' ' 
        for letter in word :
            for key, value in keys.items():
                if value == letter:
                    decipher_word = decipher_word + key
        decipher_message.append(decipher_word)
    return ''.join(decipher_message)            
        
   

def run():
    while True:
        print (
 ''' 
============================================
Bienvenido a criptografia ¿Que Desea Hacer?
   [c]ifra mensaje
   [d]ecifrar mensaje
   [s]alir 
===========================================
       
 ''')
        command = str(input("Ingrese comando :"))
        if command == 'c':
            message = str(input("Escribe tu mensaje"))
            cypher_message= cypher(message)
            print(cypher_message)            
        elif command == 'd':
            message = str(input("escribe tu mensaje cifrado"))
            decypher_message = decipher(message)
            print(decypher_message)
            
        elif command == 's':
            print("salir")
            break
        else:
            print("comando no encontrado")
            

if __name__ == '__main__':
    
    print(" M E N S A J E   C I F R A D O")
    run()
    
        

                 
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
     