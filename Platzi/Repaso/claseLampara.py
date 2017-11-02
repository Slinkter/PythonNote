# -*- coding: utf-8 -*-
class lampara:

    LAMPARAS = ["ON", "OFF"]

    def __init__(self,cable):
        self.cable = False
    def turn_on(self):
        self.cable = True
        self._display_imagen()
    def turn_off(self):
        self.cable= False
        self._display_imagen()
    def _display_imagen(self):
        if self.cable:
            print("el cable esta :",LAMPARAS[0])
        else:
            print("el cable esta : ",LAMPARAS[1])
