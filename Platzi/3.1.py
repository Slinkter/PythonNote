# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:17:29 2017

@author: Asus
"""

def mean_t(temperatura):
        suma = 0
        for t in temperatura:
           suma = suma + float(t)
        return suma/len(temperatura)
    





if __name__ == '__main__':
    temperatura = [21,24,24,26,22,21,23,24]
    resultado = mean_t(temperatura)
    print("la temperatura es {}".format(resultado))
        
    