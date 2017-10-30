# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:55:33 2017

@author: John
"""

import turtle 

def main():
    print("Funciona 100%")
    window = turtle.Screen()
    luis = turtle.Turtle()
    make_square(luis)
    
def make_square(luis):
    print("Funciona 200%")
    
    make_line(luis,100)
    
def make_line(luis,lenght):
    print("Funciona 300%")
    luis.forward(lenght)
    luis.left(90)
    
    
    

if __name__ == '__main__':
    main()
    