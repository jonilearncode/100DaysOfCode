"""
Program: treasure-island
Description: Interactive story with choice of path by reader.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""

import random


treasure_ascii = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-'''-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
"""
intro = "Welcome to Treasure Island!\nYour mission is to find the treasure.\n"

first_quest = {"You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ..." : "right"}
second_quest = {"You come to a lake. There is an island in the middle of the lake? Type \"wait\" to wait for a boat, or \"swim\" to swim across." : "wait"}
third_quest = {"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich colour do you choose?  Type \"red\", \"blue\" or \"yellow\" ..." : "yellow"}

negative_solution_0 = "You fell in a hole and died!"
negative_solution_1 = "You entered in a room with beasts! You can't fight them, you are dead."
negative_solution_2 = "You enter the dark room. The door closes behind you, and suddenly you fall asleep. You have been poisoned. You died."

win = "You found a room with a treasure chest! You won!"

def test_string(value):
    if eval(value) == str:
        return True
    return False

def test_answer(quest, answer):
    if quest == first_quest and answer == first_quest["You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ..."]:
        return True
    
    elif quest == second_quest and answer == second_quest["You come to a lake. There is an island in the middle of the lake? Type \"wait\" to wait for a boat, or \"swim\" to swim across."]:
        return True
    
    elif quest == third_quest and answer == third_quest["You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich colour do you choose?  Type \"red\", \"blue\" or \"yellow\" ..."]:
        return True
    return False
    

def set_quest(quest):
    answer = input([k for k in quest.keys()][0] + "\n")
    if test_answer(quest, answer):
        return True
    return False

# Intro www.ascii.co.uk/art
print(treasure_ascii)
print(intro)
# Pick between "rigth" or "left".
# Pick "swim" or "boat".
# Pick "red" " yellow" or "blue" door.
if set_quest(first_quest):
    if set_quest(second_quest):
        if set_quest(third_quest):
            print(win)
            exit()
        else:
            random_negative_solution = random.randint(0,2)
            if random_negative_solution == 0:
                print(negative_solution_0)
            elif random_negative_solution == 1:
                print(negative_solution_1)
            else:
                print(negative_solution_2)
                exit()
print(negative_solution_0)