"""
Program: NATO alphabet.
Description: Using Lists and Dictionaries comprehension functions.
Author: Joao Teixeira
Date: 2022.04
Version: 1.202204
"""
import pandas as pd

# Variables
phonetic_alphabet_file_url = 'nato_phonetic_alphabet.csv'
phonetic_alphabet_data_frame = pd.read_csv(phonetic_alphabet_file_url)
phonetic_alphabet_dict = {row.letter:row.code for (index,row) in phonetic_alphabet_data_frame.iterrows()}

# Main Logic
input_name = input('Enter a name: \n').upper()
list_of_chars = [char for char in input_name]
result = [phonetic_alphabet_dict[char] for char in input_name if char in phonetic_alphabet_dict.keys()]
print(result)