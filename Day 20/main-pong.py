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
score = (0,0) # player vs bots

field = Field()
field.draw_middle_field((0,0), screen_size[1])
field.draw_score_board(score)

player = Player((-screen_size[0] + X_BOARD_MARGIN, 0), 'blue', screen_size, 10)

bot = Bot((screen_size[0] - X_BOARD_MARGIN, 0), 'red', screen_size, 5)

ball = Ball((0,0), 'grey', screen_size)


# Draw
while not game_over:
   # Update GUI
   
   # Run game
   screen.onkeypress(player.move_up, 'w')
   screen.onkeypress(player.move_down, 's')
   ball.move(player.get_position(), bot.get_position())

   bot.alive(ball.get_speed())
   
   # Eval Win conditions
   if ball.is_ball_out_player_side:
      score = (score[0], (score[1] + 1))
      time.sleep(1)
      ball.reset_ball()
      
   elif ball.is_ball_out_bot_side:
      score = ((score[0] + 1), score[1])
      time.sleep(1)
      ball.reset_ball()
   
   field.score.clear()
   field.draw_score_board(score)
   
   time.sleep(0.01)
   screen.update() # draw graphics
    
screen.exitonclick()
