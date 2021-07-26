"""
Program: name-generator
Description: Console program that prompts for two string values and retrieve them combined to form a new string name.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""

import random

# Ask user for favorite city name
city_name = input("Type your favorite city's name:\n > ")
# Ask user for favorite pet's name
pet_name = input("Type your favorite pet's name:\n > ")
# Combine both inputted names randomly and retrieve them as a band name suggestion
rand_num = random.randint(0, 2)
if rand_num > 1 :
    band_name = city_name + "'s " + pet_name
else:
    band_name = pet_name + "'s " + city_name
    
print(f'Your band should be named as: "{band_name}"')