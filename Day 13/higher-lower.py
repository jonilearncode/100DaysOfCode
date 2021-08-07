"""
Program: higher-lower
Description: A console game based on Higher Lower.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

from hl_db import data
from hl_art import logo, vs

import random, os

# Globals
intro= '\n\nWelcome to PyHigherLower Game. Made by Joao Teixeira 2021'
instructions = 'Just guess who have more followers!'
# Aux methods
def get_statement(db):
    randindex = random.randint(0, len(db) - 1)
    stat = db[randindex]
    db.pop(randindex)
    return stat, db

def draw_statement(statement, option):
    name = statement['name']
    description = statement['description']
    country = statement['country']
    print(f'\nCompare {option}: \n{name}, a {description} from {country}.')

def check_if_stat1_higher(stat1, stat2):
    if stat1['follower_count'] > stat2['follower_count']:
        return True
    return False

def print_current_score(score):
    print(f'\n You are right! Current SCORE = {score}')

# Main logic
score = 0
stat_buff = {}
data_buff = data.copy()
while True:
    # Intro
    os.system('cls')
    print(logo)
    print(intro)
    print(instructions)
    # Display statements 1 and 2 if there are in db
    if not len(data_buff) > 0:
        print(f'\n\n Congratulations! Game Ended! TOTAL SCORE: {score}')
        break
    if not 'name' in stat_buff:    
        stat1, data_buff = get_statement(data_buff)
        stat2, data_buff = get_statement(data_buff)
    else:
        print_current_score(score)
        stat1 = stat_buff
        stat2, data_buff = get_statement(data_buff)
    draw_statement(stat1, 'A')
    print(vs)
    draw_statement(stat2, 'B')
    # Prompt for response
    answer = input('\nWho has more followers (A/B)  --->  ' ).lower()
    assert answer == 'a' or answer == 'b', f'ERROR - \'{answer}\' is not a option.'
    # Evaluate
    # - if right continue and calc score
    if check_if_stat1_higher(stat1, stat2) and answer == 'a':
        score += 1
        stat_buff = stat1
        continue
    elif not check_if_stat1_higher(stat1, stat2) and answer == 'b':
        score += 1
        stat_buff = stat2
        continue
    # - if false stop and calc score
    print(f'You lost! \n\n Your score: {score}')
    break
input('\n\n Type any key to \'exit\' ... ')
