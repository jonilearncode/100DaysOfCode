"""
Program: number-guessing
Description: A console Number Guess game, implementing
binary search algorithm.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108   
"""
import random

# Globals
INTRO = """\nWelcome to NumberGuessPy! Made by João Teixeira 2021.
            \nTry to beat me. Guess my number between 0 to 100."""
LOGO = """
                       _                   
                      | |                  
 _ __  _   _ _ __ ___ | |__   ___ _ __ ___ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| | | | |_| | | | | | | |_) |  __/ |  \__ \ 
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/


"""
WIN = """
*******************
*     YOU WIN     *
*******************
"""

# Aux methods
def assert_input(desired_input_list, test_input):
    for i in desired_input_list:
        for j in test_input:
            if i == j:
                return True
    return False

def evaluate_result(user_number, target_number):
    test = user_number - target_number
    if test == 0:
        return [True, WIN]
    elif test > 0:
        return [False, 'number is lower']
    else:
        return [False, 'number is higher']

def generate_number():
    return random.randint(0, 100)

def apply_difficulty(dif):
    if dif == 'e':
        return 10
    else:
        return 5

# Main Logic
# Intro & Logo
print(LOGO)
print(INTRO)
is_game_on = True
numbers = [x for x in range(101)]
while is_game_on:
    # Pick difficulty
    tgt_number = generate_number()
    difficulty = input('Choose a difficulty. Type \'e\' for easy and \'h\' for hard.  ')
    if not assert_input(['e', 'h'], [difficulty]):
        print(f'\n --> Hey, only two options: \'e\' or \'h\'. \'{difficulty}\' it isn\'t.' )
        continue
    life = apply_difficulty(difficulty)
    # Start game
    while True:
        # - Pick a guess
        guess = int(input('Pick a number:  '))

        if not assert_input(numbers, [guess]):
            print(f'\n --> Hey, \'{guess}\' is not possible. Try again.' )
            continue
        # - Evaluate
        eval = evaluate_result(int(guess), int(tgt_number))
        # - Print tip lower, or higher, or WIN, or LOSE
        if eval[0]:
            print(eval[1])
            break
        else:
            life -= 1
            print(eval[1], f'  --> {life} lives left. Try again ...')
            if life > 0:
                continue
            print(" GAME OVER !!")
            break
    # End game or restart
    if not input("\n\nPlay again (y/n)?  ") == 'y':
        print("Bye bye!")
        is_game_on == False
