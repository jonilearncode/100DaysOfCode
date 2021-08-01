"""
Program: calculator
Description: A console program emulating a calculator.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""
import os

# Globals
intro = "\nWelcome to CalculatorPy. To exit type anytime 'ctr+c'."
logo = """
 _____________________
|  _________________  |
| | CALCULATOR   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
# Aux methods
def check_is_float(n):
    try:
        n = float(n)
        return True
    except:
        print(f'\n ERROR --------> \'{n}\' is not a number. Try again.')
        return False

def proccess_operator(oper):
    return oper

def solve(n1, n2, oper):
    if oper == '+':
        return float(n1 + n2)
    elif oper == '-':
        return float(n1 - n2)
    elif oper == '*':
        return float(n1 * n2)
    elif oper == '/':
        return float(n1 / n2)
    else:
        print(f'ERROR - {oper} must be equal to: +, -, *, or /')
# Intro & logo
os.system('cls')
print(intro)
print(logo)
# While loop until '='
cache = ''
while True:
    wait_for_n2 = True
    n2 = 0.0
    ## - Ask for a number
    if isinstance(cache, str):
        n1 = input("\nType a number >  ")
        if check_is_float(n1):
            n1 = float(n1)
        else:
            continue
    else:
        n1 = cache
    ## - Ask for operator
    oper = input("+  -  *  /  >  ")
    oper = proccess_operator(oper)
    ## - Ask for other number
    while wait_for_n2:
        n2 = input("Type other number >  ")
        if check_is_float(n2):
            n2 = float(n2)
            break
        else:
            continue
    cache = float((solve(n1, n2, oper)))
    print(f'\n  -------->  = {cache}')
    ## - finish?
    # Print result
    # Coninue with previous result, new operation or exit?
    finish = input(f'\nType \'q\' to finish operation or \'c\' to continue with {cache} >  ')
    if finish == 'q':
        cache = ''
        continue