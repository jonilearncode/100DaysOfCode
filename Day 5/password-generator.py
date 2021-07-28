"""
Program: password-generator
Description: A customable password generator.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""
import random

intro = "Welcome to PyPassword Generator."
question_how_long = "\nHow many characters? "
question_how_many_symbols = "\nHow many symbols? "
question_how_many_numbers = "\nHow many numbers? "

symbols = ['@', '#', '%', '$', '/', '(', ')', '=', '?', '.']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z']

def shuffle_password(passwd):
    result = []
    passwd_copy = passwd.copy()
    while len(passwd_copy) > 0:
        random_index = random.randint(0, len(passwd_copy) - 1)
        result.append(passwd_copy.pop(random_index))
    return result

def get_random_items_from_list(n, a_list):
    result = []
    assert n <= len(a_list)
    for i in range(n):
        rand = random.randint(0, len(a_list) - 1)
        result.append(a_list[rand])
    return result

def passwd_generator(l_length, s_symbols, n_numbers):
    random_symbols = get_random_items_from_list(s_symbols, symbols)
    random_numbers = get_random_items_from_list(n_numbers, numbers)
    random_characters = get_random_items_from_list(abs(l_length - s_symbols + n_numbers), characters)
    result = random_symbols + random_numbers + random_characters    
    return shuffle_password(result)

def print_to_string(a_list):
    return ''.join(a_list)

# Intro
print(intro)
# Input for password length
passwd_length = int(input(question_how_long))
# Input for how many symbols
passwd_symbols = int(input(question_how_many_symbols))
# Input for how many numbers
passwd_numbers = int(input(question_how_many_numbers))
# Generate password
assert passwd_length >= passwd_symbols + passwd_numbers, "ERROR, your password length is less than the total of symbols and numbers."
new_passwd = print_to_string(passwd_generator(passwd_length, passwd_symbols, passwd_numbers))
# Print result
print(f"\nYour Password: {new_passwd}")

input("\n\nType any key to exit ...")
