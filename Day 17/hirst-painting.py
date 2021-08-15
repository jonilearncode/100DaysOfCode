"""
Program: hirst-paint-generator
Description: A Hirst painter generator with python. 
Uses an upload image to extract colour pallet.
Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

import colorgram, random
import turtle

# Globals   
n_columns = 20
n_lines = 20
circles_size = 25
origin_offset = (25, 25) # manual correction of turtle screen origin position.
colors_pallet = colorgram.extract('himg.png', 50) # extract colors pallet from a image.
screen = turtle.Screen()
pointer = turtle.Turtle()
pointer.speed('fast')
screen_size = screen.screensize()
screen.colormode(255)

# Main Logic
origin = (-screen_size[0] - origin_offset[0], -screen_size[1]) # left down corner.
next_pos = None
# Define the width (column) and height (line) for the dot drawing center pos.
dot_draw_margins = (int((screen_size[0] * 2) / n_columns), int((screen_size[1] * 2) / n_lines))
print_center_point = (dot_draw_margins[0] + circles_size / 2, dot_draw_margins[1] + circles_size / 2)
while True:
    if next_pos == None:
        next_pos = origin
    else:
        # Evaluate screen borders to stop draw, and advance a new column.
        next_pos = (next_pos[0] + print_center_point[0], next_pos[1])
    pointer.pu()
    pointer.setpos(next_pos)
    pointer.pd()
    colorgram_colour = colors_pallet[random.randint(0, len(colors_pallet) - 1)].rgb
    pointer.dot(circles_size, (colorgram_colour.r, colorgram_colour.g, colorgram_colour.b))
    # Evaluate screen borders to stop draw, and reset new line.
    if next_pos[0] >= screen_size[0] and not next_pos[1] >= screen_size[1]:
        next_pos = (origin[0] - print_center_point[0], next_pos[1] + print_center_point[1])
    if next_pos[1] >= screen_size[1]:
        break
screen.exitonclick()