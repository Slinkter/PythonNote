# -*- coding: utf-8 -*-
import claseLampara 
def run():
    lamp = lampara(True)
    while True :
        comando = str(input("Ingresar comando : "))
        if comando == 'p':
            lamp.turn_on()
        elif comando == 'a':
            lamp.turn_off()
        else :
            break

if __name__ == '__main__':
    run()
