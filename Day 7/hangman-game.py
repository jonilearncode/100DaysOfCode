"""
Program: hangman-game.
Description: The Hang Man word guessing game in python using 
console as UI.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""

import random
from os import system

intro = "Welcome to PyHangman game."
logo = """
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"   
"""
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ['teste', 'carácter', 'amor', 'longevidade', 'presépio', 'gato', 'portugal',
            'imaginar', 'burros', 'atentado' ]

# Aux methods
def generate_new_word(a_word_list):
  return random.choice(a_word_list)

def find_char_in_str(a_word, a_char):
  a_word_list = list(a_word)
  for c in a_word_list:
    if c == a_char:
      return True
  return False

def update_letter_in_guessed_word(character, word, guessed_word):
  count = 0
  list_word = list(word)
  list_guessed_word = list(guessed_word)
  for c in list_word:
    if c == character:
      list_guessed_word[count] = character
    count += 1
  return ''.join(list_guessed_word)

def print_hangman_state(s):
  assert int(s) <= len(hangman_stages) - 1
  print(hangman_stages[int(s)])

def print_spaced_chars(a_string):
  temp_str = list(a_string)
  result = ''
  for c in temp_str:
    result += ' ' + c
  print(result) 

def draw_screen(a_logo, a_guessed_word, a_hang_state):
  system('cls')
  print(a_logo)
  print_spaced_chars(a_guessed_word)
  print_hangman_state(a_hang_state)

# Main Logic
gameover = False
state = 0
word = generate_new_word(word_list)
guessed_word = len(word) * '_'

# Loop until gameover:
while not gameover:
  # Intro & logo
  draw_screen(logo, guessed_word, state)
  #-- Input for guess a letter
  ##-- In case correct -- show the word with guessed letter and blanks
  ##-- In case negative -- show the word with blanks and failure message
  ##-- Show the hangman state
  player_letter_input = input("\nGuess a letter: ")
  if find_char_in_str(word, player_letter_input):
    guessed_word = update_letter_in_guessed_word(player_letter_input, word, guessed_word)
  else:
    state += 1
    input(f'\nWrong guess, the letter \"{player_letter_input}\" isn\'t in the word. ') 
 
  ##-- Test gameover conditions
  if word == guessed_word:
    print("\n -- YOU WIN ! -- ")
    gameover = True
  elif state >= len(hangman_stages) - 1:
    print("\n -- YOU LOSE ! -- ")
    gameover = True

input("\n\nType any key to exit ...")
