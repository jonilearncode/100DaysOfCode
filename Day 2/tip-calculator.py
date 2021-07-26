"""
Program: tip-calculator
Description: Calculates the value in currency of a tip percentage and divided by any number of persons.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""


# Aux methods
def test_value(value, options):
    for i in options:
        if i == int(value):
            return True
    return False

def division(total, divisor):
    if int(divisor) <= 0:
        divisor = 1
    result = round(int(total)/int(divisor), 2)
    return f'The tip per each should be: {result}€'

# Program Greeting
print("\n\nWelcome to 'Tip Calculator'")
# Input total bill in currency
total = float(input("\nType the bill value: "))
# Input the tip percentage
tip_percentage = int(input("\nSelect the tip percentage: 10, 20, 30, 40: "))
# Test and assert inputs
if not test_value(tip_percentage, [10, 20, 30, 40]):
    print("You did not select the correct value. Try again ...")
    exit()
# Input how many people will divide the tip
divide_by = int(input("\nSplit between how many people: "))
# Print result in currency of how many should each pay
print('\n\n')
print(division(total * tip_percentage / 100, divide_by))



