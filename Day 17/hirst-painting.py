"""
Program: hirst-paint-generator
Description: A Hirst painter generator with python. 
Uses an upload image to extract colour pallet.
Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

import colorgram, os, math
import turtle


# Hirst paint is a n amount of circle colours drawn in a square arrangement.
# Extract a colour pallet from target image.
# Define the printer movement per n circles.
# Print each spot with a random colour from the pallet.

# Globals   
circles_amount = 30
circles_size = 5
colors_pallet = colorgram.extract('himg.png', 50)

# Aux methods
def get_square_pattern_coordinates(num_circles, circles_siz, screen_siz):
    coordinates = []
    num_col = int(screen_siz[0] / (math.sqrt(num_circles) * circles_siz * 2)) 
    num_li = int(screen_siz[1] / (math.sqrt(num_circles) * circles_siz * 2))
    # print('num_li', num_li, '   num_col', num_col)
    for x in range(num_col):
        for y in range(num_li):
            coordinates.append([x,y])
    return coordinates

# Main Logic
screen = turtle.Screen()
pointer = turtle.Turtle()
# Define the movement with turtle module.
screen_size = screen.screensize()

tgt_list = get_square_pattern_coordinates(circles_amount, circles_size, screen_size)
for coord in tgt_list:
    pointer.goto(coord[0], coord[1])
# pointer.dot(100)
# print(colors_pallet)

screen.exitonclick()