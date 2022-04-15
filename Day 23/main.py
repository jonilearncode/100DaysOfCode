"""
Program: Interactive quiz with turtle and pandas module.
Description: Quiz game about U.S.
Author: Joao Teixeira
Date: 2022.04
Version: 1.202204
"""

import pandas as pd
import turtle

# Setup screen
screen = turtle.Screen()
screen.title('U.S. States Game')
background_image_url = 'blank_states_img.gif'
screen.addshape(background_image_url)
turtle.shape(background_image_url)
screen.listen()
screen.tracer(0) # stop graphics drawing
screen_size = screen.screensize()
score_label = turtle.Turtle()
score_label.color('black')
style = ('Courier', 20, 'italic')

# Aux methods
# Setup user answer window
def get_user_answer():
    return screen.textinput(title='Guess the State', prompt="What's another state's name?")

def get_coordinates_with_name(state_name, data):
    """Search for the value state name, if exist on panda datastructure 
    returns corresponding value, if not returns -1."""
    if state_name in data.values:
         coord_data = data[data['state'] == state_name]
         return (coord_data['x'].values[0], coord_data['y'].values[0])
    return -1
    
def update_score(score, score_object):
    score_object.clear()
    score_object.ht()
    score_object.pu()
    score_object.setpos(0,screen_size[1]-40)
    score_object.write(arg=f'Score: {score}/50',move=True,font=style, align='center')

# Main logic
#Get tuple of states names and coordinates from csv with pandas
data = pd.read_csv('50_states.csv')
states_names = data['state']
score = 0
while score <= 50:
    #Prompt user with state
    user_answer = get_user_answer()
    user_answer = user_answer[0].upper() + user_answer[1:].lower()
    #Check if answer exists on state list
    coord = get_coordinates_with_name(user_answer, data)
    if coord != -1:
    #   create a turtle text with the state name on respective coordinates
        state_label = turtle.Turtle()
        state_label.ht()
        state_label.pu()
        state_label.setpos(coord)
        state_label.write(arg=user_answer,move=True)
        score += 1
        update_score(score, score_label)
    #   Reduce a point from the score countdown
    #If false:
    #   Display game over
    else: 
        break
    screen.update()

#End game
state_label = turtle.Turtle()
state_label.ht()
state_label.pu()
state_label.write(arg='GAME OVER',move=True, font=style, align='center')
screen.exitonclick()
# Keeps turtle restarting in an infinite loop (not the program!)
#turtle.mainloop()