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
# |V| Create snake food
# |V| Detect collision with food
# |V| Create scoreboard
# |V| Detect collisicon with wall
# |V| Detect collision with tail

import turtle, random, time
from snake_food import SnakeFood

# Globals   
screen = turtle.Screen()
screen_size = screen.screensize()
screen_collision_margin = 10 # plus the turtle object width
screen.colormode(255)
snake_speed = 20
screen.listen()
food_collision_box_size = 20

# Initialized data
velocity_vector = (snake_speed, 0)
snake_body = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
snake_body_pos = []  
food = SnakeFood((random.randint(-screen_size[0], screen_size[0]), random.randint(-screen_size[1], screen_size[1])))
for i in range(len(snake_body)):
    snake_body[i].pu()
    snake_body[i].shape('square')
    snake_body[i].speed('fastest')
    snake_body_pos.append((snake_body[i].position()[0] - 25 * i, snake_body[i].position()[1]))

snake_body_pos.append((snake_body[-1].position()[0] - 25 * i, snake_body[-1].position()[1])) # extra slot for the snake growth

# Aux Methods
def mv_forward():
    next_pos_vector = (snake_body[0].position()[0] + velocity_vector[0], snake_body[0].position()[1] + velocity_vector[1])
    snake_body_pos.insert(0, next_pos_vector)
    for i in range(len(snake_body)):
        snake_body[i].goto(snake_body_pos[i])
    snake_body_pos.pop(-1) 
        
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
    if snake_body[0].distance(food_object_pos) < food_collision_box_size:
        return True
    else:
        return False

def check_collision_with_wall():
    if snake_body[0].position()[0] >= screen_size[0] - screen_collision_margin or snake_body[0].position()[0] <= - screen_size[0] + screen_collision_margin:
        return True
    elif snake_body[0].position()[1] >= screen_size[1] - screen_collision_margin or snake_body[0].position()[1] <= - screen_size[1] + screen_collision_margin:
        return True
    return False
    
def check_collision_with_snake():
    for i in range(2, len(snake_body)):
        if snake_body[0].distance(snake_body[i].position()) < 15:
            return True
    return False
    
def add_snake_body():
    new_snake_body = turtle.Turtle()
    new_snake_body.ht()
    new_snake_body.pu()
    new_snake_body.speed('fastest')
    new_snake_body.goto(snake_body_pos[-1])
    snake_body_pos.append(snake_body_pos[-1])
    new_snake_body.shape('square')
    new_snake_body.st()
    # new_snake_body.speed('normal')
    snake_body.append(new_snake_body)
    
# Main logic
# Setup
screen.tracer(0) # stop graphics drawing
game_over = False
# Draw
while not game_over:
    mv_forward()
    if check_collision_with_wall() or check_collision_with_snake():
        game_over = not game_over
        print("GAME OVER - You hit the wall/Snake!")
    
    if check_collision_with_food(food.get_position()):
        print(f'DEBUG Snake is eating a food! snake_body_segments = {len(snake_body)} --- snake_body_segments_pos = {len(snake_body_pos)} ')
        food.delete_food()
        score = food.get_score()
        add_snake_body()
        print(f'SCORE = {score}')
    if not food.has_food():
        food.create_food((random.randint(-screen_size[0], screen_size[0]), random.randint(-screen_size[1], screen_size[1])))
    
    screen.onkeypress(turn_up, 'w')
    screen.onkeypress(turn_down, 's')
    screen.onkeypress(turn_left, 'a')
    screen.onkeypress(turn_right, 'd')
    
    time.sleep(0.1)
    screen.update() # draw graphics
    
screen.exitonclick()
