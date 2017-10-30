# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:33:16 2017

@author: Ta
"""
def foreign_exchange_calculator(ammount):
    mex_to_col_rate =  145.97
    return mex_to_col_rate*ammount


def run():
    print("CALCULADORA  DE DIVISAS")
    print("Peso Mexicano --> Peso Colombianos")
    print("")
    
    ammount = float(input("Ingresa la cantidad de pesos mexicanos : "))
    result = foreign_exchange_calculator(ammount)
    
    print("${} pesos mexicanos son ${} pesos colombianos".format(ammount,result))
    print("2")
    
if __name__ == '__main__':
    run()
    