"""
Program: snake
Description: Snake game in Python! Using turtle module.
Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

# |V| Create a snake body 
# |V| Move the snake
# Create snake food
# Detect collision with food
# Create scoreboard
# Detect collisicon with wall
# Detect collision with tail

import turtle, random
from snake_food import SnakeFood

# Globals   
screen = turtle.Screen()
screen_size = screen.screensize()
screen.colormode(255)
snake_speed = 10
screen.listen()

velocity_vector = (snake_speed, 0)
snake_body = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
snake_body_pos = []  

food = SnakeFood((random.randint(-screen_size[0], screen_size[0]), random.randint(-screen_size[1], screen_size[1])))
food_collision_box_size = 25

# Initialized data
for i in range(len(snake_body)):
    snake_body[i].pu()
    snake_body[i].shape('square')
    snake_body[i].speed('slow')
    snake_body_pos.append((snake_body[i].position()[0] - 15 * i, snake_body[i].position()[1]))
    
# Aux Methods
def mv_forward():
    print('DEBUG snake_body_pos  = ', snake_body_pos)
    next_pos_vector = (snake_body[0].position()[0] + velocity_vector[0], snake_body[0].position()[1] + velocity_vector[1])
    snake_body_pos.insert(0, next_pos_vector)
    for i in range(len(snake_body)):
        snake_body[i].goto(snake_body_pos[i])
    snake_body_pos.pop(len(snake_body_pos) - 1) 
        
def turn_up():
    global velocity_vector
    if velocity_vector[1] == 0:
        velocity_vector = (0, snake_speed)

def turn_down():
    global velocity_vector
    if velocity_vector[1] == 0:
        velocity_vector = (0, -snake_speed)

def turn_left():
    global velocity_vector
    if velocity_vector[0] == 0:
        velocity_vector = (-snake_speed, 0)

def turn_right():
    global velocity_vector
    if velocity_vector[0] == 0:
        velocity_vector = (snake_speed, 0)

def check_collision_with_food(food_object_pos):
    if snake_body[0].position()[0] + food_collision_box_size <= food_object_pos[0] <= snake_body[0].position()[0] - food_collision_box_size:
        if snake_body[0].position()[1] + food_collision_box_size <= food_object_pos[1] <= snake_body[0].position()[1] - food_collision_box_size:
            return True
    else:
        return False
        
    
    
# Main logic
# Setup
screen.tracer(1, 25) # stop graphics drawing
game_over = False
# Draw
while not game_over:
    mv_forward()
    screen.onkeypress(turn_up, 'w')
    screen.onkeypress(turn_down, 's')
    screen.onkeypress(turn_left, 'a')
    screen.onkeypress(turn_right, 'd')
    
    if check_collision_with_food(food.get_position()):
        print('DEBUG Snake is eating a food!')
        food.delete_food(food.get_position())
        score = food.get_score()
        print(f'SCORE = {score}')
    
    if not food.has_food():
        food.create_food((random.randint(-screen_size[0], screen_size[0]), random.randint(-screen_size[1], screen_size[1])))
    # screen.update() # draw graphics
    
    
    
screen.exitonclick()