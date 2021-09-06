"""
Program: pong
Description: Turtle Against Cars. Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.09
Version: 1.202109
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Aux Methods
def create_cars_wave(cars_wave_list):
   cars_wave_list.append(CarManager(screen_size, COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT))
   cars_wave_list[len(cars_wave_list)-1].initialize_cars()

# Setup/Initialize
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.listen()
screen.tracer(0) # stop graphics drawing
screen_size = screen.screensize()

game_over = False
level = 0

# scoreboard = Scoreboard()
# scoreboard.draw_score_board(level)

player = Player(STARTING_POSITION, screen_size, MOVE_DISTANCE)
cars_waves = []
create_cars_wave(cars_waves) # initialize with one wave

creation_state = False

# Draw
while not game_over:
   # Update GUI
   
   # Run game
   screen.onkeypress(player.move_up, 'w')
   
   for i in range(0, len(cars_waves)):
      print('1inside for loop -- ', len(cars_waves))
      cars_waves[i].move()
      if cars_waves[i].check_if_wave_is_finished() and not cars_waves[i].to_del():
         creation_state = True
         cars_waves[i].marked_for_delete = True
      # Eval waves memory leak and delete
      if creation_state:
         create_cars_wave(cars_waves)
         creation_state = False
      elif len(cars_waves) > 4:
         del cars_waves[i]
      
   # Eval Win conditions
  
   
   # scoreboard.score.clear()
   # scoreboard.draw_score_board(level)
   
   time.sleep(0.1)
   screen.update() # draw graphics
    
screen.exitonclick()
