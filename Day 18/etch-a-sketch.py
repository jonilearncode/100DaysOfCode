"""
Program: etch-a-ketch
Description: An Etch a Ketch emulator with turtle module.
Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

import turtle

# Globals   
screen = turtle.Screen()
pointer = turtle.Turtle()
screen.listen()
pointer_speed = 15

# Aux methods
def move_forward():
    pointer.forward(pointer_speed)

def move_backward():
    pointer.backward(pointer_speed)
    
def rot_right():
    pointer.right(pointer_speed)

def rot_left():
    pointer.left(pointer_speed)

def clear_screen():
    pointer.clear()
    pointer.pu()
    pointer.home()
    pointer.pd()

# Main logic 
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backward, 's')
screen.onkeypress(rot_left, 'a')
screen.onkeypress(rot_right, 'd')
screen.onkeypress(clear_screen, 'c')
screen.exitonclick()
