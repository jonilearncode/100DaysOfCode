"""
Program: rock-paper-scissors-game
Description: Interactive game best known as Rock Paper Scissors!
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""

from math import ceil
import random

intro = "Welcome to Rock Paper Scissors game.\n"
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n\n"""
paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
\n\n"""
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n\n"""


def get_ascii(index):
    assert 0<=index<=2, "[ERROR] get_ascii Invalid Index"
    if index == 0:
        return rock_ascii
    elif index == 1:
        return paper_ascii
    elif index == 2:
        return scissors_ascii

def generate_rand_response():
    rand = random.randint(0,2)
    return rand

def test_win_condition(player_input, computer_input):
    win = "\nPlayer Wins!"
    draw = "\nDraw!"
    lose = "\nPlayer Loses!"
    if player_input == computer_input:
        return draw
    elif player_input == 0 and computer_input == 2:
        return win
    elif player_input == 2 and computer_input == 1:
        return win
    elif player_input == 1 and computer_input == 2:
        return win
    else:
        return lose

# Intro
print(intro)
# Input from player
player_input = int(input("Pick '0' for 'Rock', '1' for 'Paper' or '2' for 'Scissors': "))
print(get_ascii(player_input))
# Show computer output
computer_input = generate_rand_response()
print(f"\nComputer chooses: {computer_input}")
print(get_ascii(computer_input))
# Check win condition
print(test_win_condition(player_input, computer_input))
# Prompt to exit
input("\nType any key for exit ...")