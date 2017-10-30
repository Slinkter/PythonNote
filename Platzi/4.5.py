# -*- coding: utf-8 -*-
class lampara:
    _LAMPAS = ['''encendida''','''apagada''']

    def __init__(self,is_turned_on):
        self.__is_turned_on = False
    def tun_on(self):
        self.__is_turned_on = True
        self._display_imagen()
    def tunr_off(self):
        self.__is_turned_on = False
        self._display_imagen()
    def _display_imagen(self):
        if self.__is_turned_on:
            print("la lampara esta ", self._LAMPAS[0])
        else:
            print("la lampara esta ", self._LAMPAS[1])

def run():
    lamp = lampara(True)
    while True:
        comando = str(input('''
        Escoger un comando
            [p]render
            [a]pagar
            [s]alir
        '''))
        if comando == 'p':
            lamp.tun_on()
        elif comando == 'a':
            lamp.tunr_off()
        else:
            break






if __name__ == '__main__':
    run()
