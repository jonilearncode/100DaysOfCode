"""
Program: turtle-race
Description: A turtles race with turtle module.
Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

import turtle, random

# Globals   
screen = turtle.Screen()
screen_size = screen.screensize()
pointer_speed = 2
players_names = ['Ralph', 'Melon', 'Crystal', 'Joni', 'Beterraba', 'Poo', 'Slow']
finish_line = screen_size[0] - 50
# screen.colormode(255)

# Aux methods
def initial_pos():
    return [-screen_size[0], 0]

def turtles_move():
    for turtle in screen.turtles():
        turtle.forward(random.randint(1, 25) * pointer_speed)

def turtles_set_start_pos():
    offset = screen_size[1] * 1.8 / 5 # 5 is num of turtles
    counter = 1
    for turtle in screen.turtles():
        turtle.pu()
        turtle.goto(-screen_size[0] + 100 , - screen_size[1] + offset * counter)
        turtle.pd()
        counter += 1
        
def print_winner(turtle_color, player_name):
    if turtle_color == 'green':
        print(f'The winner is: {player_name}')
    else:
        print(f'The winner is: {str(turtle_color)}')
        
# Main logic 
pointer_name = screen.textinput('Your Turtle\'s name', 'Type your Turtle\'s name: ')

# Setup the game
a_turtle = turtle.Turtle()
b_turtle = turtle.Turtle()
c_turtle = turtle.Turtle()
d_turtle = turtle.Turtle()
e_turtle = turtle.Turtle()

a_turtle.color('red')
b_turtle.color('black')
c_turtle.color('green')
d_turtle.color('blue')
e_turtle.color('violet')

turtles_set_start_pos()
race_is_over = False
while not race_is_over:
    turtles_move()
    for turtle in screen.turtles():
        if turtle.pos()[0] > finish_line:
            race_is_over = not race_is_over
            print_winner(turtle.color()[0], pointer_name)
screen.exitonclick()
