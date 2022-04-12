"""
Program: car-game
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
def create_cars_wave(cars_wave_list, level):
   cars_wave_list.append(CarManager(screen_size, COLORS, STARTING_MOVE_DISTANCE + STARTING_MOVE_DISTANCE * 0.1 * level))
   cars_wave_list[len(cars_wave_list)-1].initialize_cars()

# Setup/Initialize
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.listen()
screen.tracer(0) # stop graphics drawing
screen_size = screen.screensize()

game_over = False
game_loop = True
pass_level = False
creation_state = False
level = 0

# scoreboard = Scoreboard()
# scoreboard.draw_score_board(level)

player = Player(STARTING_POSITION, screen_size, MOVE_DISTANCE)
scoreboard = Scoreboard(level)
scoreboard.draw_score_board(level)
cars_waves = []
create_cars_wave(cars_waves, level) # initialize with one wave


# Draw
while not game_over: 
   if pass_level:
      level += 1
      print(f'DEBUG Level = {level}')
      game_loop = not game_loop
      pass_level = False
      while len(cars_waves) > 0:
         cars_waves[0].delete()
         cars_waves.pop(0)
      cars_waves.clear()
      create_cars_wave(cars_waves, level)
      player.reset_pos()
      
   while game_loop:
      # Run game
      screen.onkeypress(player.move_up, 'w')
      screen.onkeypress(player.move_down, 's')
      for i in range(0, len(cars_waves)):
         cars_waves[i].move()
         # Detect collisions
         for car in cars_waves[i].cars:
            if car.position()[0] < 80 and car.position()[0] > -80: # filter the car in cars per cars_wave if are close the x_value of player 
               # print(f'[DEBUG] main --> Player is EVAL COL')
               if player.is_colliding(car):
                  print(f'[DEBUG] main --> Player is colliding!')
                  game_loop = False
                  game_over = True
                  break
         if cars_waves[i].check_if_wave_is_on_initial() and not cars_waves[i].to_del():
            creation_state = True
            cars_waves[i].marked_for_delete = True
         # Eval waves memory leak and delete
         if creation_state:
            create_cars_wave(cars_waves, level)
            creation_state = False
         if len(cars_waves) > 5 and cars_waves[i].check_if_wave_is_finished():
            del cars_waves[0]
            break
      
      # Eval Win conditions
      if player.has_reach_finish_line((0, screen_size[1])):
         game_loop = False
         pass_level = True
      
      # Update GUI
      scoreboard.gui.clear()
      scoreboard.draw_score_board(level)
         
      time.sleep(0.1)
      screen.update() # draw graphics

scoreboard.draw_gameover()
print('GAME OVER!')
   
screen.exitonclick()
