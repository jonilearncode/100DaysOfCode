"""
Program: Mail serving script.
Description: Script that combines two lists, receivers names and email content.
Author: Joao Teixeira
Date: 2022.04
Version: 1.202204
"""

# Variables
input_directory = "./Input"
output_directory = "./Output"

# Aux Methods
def get_list_names(path_to_txt):
    names_list = []
    with open(path_to_txt) as file:
        for name in file:
             names_list.append(name.strip()) # removes extra unnecessary characters: '/n'
    return names_list

def get_standard_letter(path_to_txt):
    letter = ''
    with open(path_to_txt) as file:
        letter = file.read()
    return letter
    
def serve_mail_with_name(mail, name):
    return mail.replace('[name]', name)

#TODO: Create a letter using starting_letter.txt 
standard_letter = get_standard_letter(input_directory + "./Letters/starting_letter.txt")
names = get_list_names(input_directory + "./Names/invited_names.txt")
for name in names:
    result = serve_mail_with_name(standard_letter, name)
    with open(output_directory + f'./ReadyToSend/MailTo{name}.txt', mode='w') as file:
        file.write(result)
    
#Save the letters in the folder "ReadyToSend".
