# -*- coding: utf-8 -*-

import turtle

if ___name___ =='__main__':
    main()


def main():
    
    window = turtle.Screen()
    luis = turtle.Turtle()
    
    make_square(luis)
    turtle.mainloop()


def make_square(luis):
    length=int(raw_input('Tamaño de cuadrado : '))

    for i in range(4):
        make_line_and_turn(luis,length)


def make_line_and_turn(luis,length):
    luis.forward(length)
    luis.left(90)
