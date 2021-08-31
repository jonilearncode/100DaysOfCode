"""
Program: pong
Description: Atari Pong game in Python! Using turtle module.
Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

import turtle, time
from field import Field
from player import Player
from bot import Bot
from ball import Ball

X_BOARD_MARGIN = 40

# Main logic
# Setup/Initialize
screen = turtle.Screen()
screen.colormode(255)
screen.listen()
screen.tracer(0) # stop graphics drawing
screen.bgcolor('black')
screen_size = screen.screensize()

game_over = False

field = Field()
field.draw_middle_field((0,0), screen_size[1])

player = Player((-screen_size[0] + X_BOARD_MARGIN, 0), 'blue', screen_size)
bot = Bot((screen_size[0] - X_BOARD_MARGIN, 0), 'red', screen_size)

ball = Ball((0,0), 'grey', screen_size)

# Draw
while not game_over:
   # Update GUI
   
   # Run game
   screen.onkeypress(player.move_up, 'w')
   screen.onkeypress(player.move_down, 's')
   ball.move(player.get_position())

   time.sleep(0.01)
   screen.update() # draw graphics
    
screen.exitonclick()
