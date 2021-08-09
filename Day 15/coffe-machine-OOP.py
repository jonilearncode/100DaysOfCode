"""
Program: coffee-machine-OPP
Description: Main logic for a coffee machine. Managing resources and currency to sell
coffee products to user. Implementation done with OOP.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

# Main Loop
# - Scoop for input with standard input('What would you like? (espresso/latte/cappuccino): ')
# - Evaluate input from pre-actions ('off', 'report', 'espressolatte/cappuccino') 
# - If 'coffee'
# - - Display price and prompt for money (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)
# - - Eval transaction/change
# - - - If good, brew coffee
# - - - Update report (report = Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5)
# - - - Print final result “Here is your {coffee_choice}. Enjoy!”

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Globals
intro = '\n\nWelcome to PyCoffeeMachine. Made by Joao Teixeira 2021.'
logo = ''
txt_switch_off = 'Goodbye!'

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

print(intro)
while True:
    options = menu.get_items()
    user_input = input(f'What would you like ({options})?  ').lower()
    if user_input == 'off':
        print(txt_switch_off)
        break
    elif user_input == 'report':
        coffee_maker.report()
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        item = menu.find_drink(user_input)
        if item != None and coffee_maker.is_resource_sufficient(item):
            item_cost = item.cost
            print(f'The price for a {user_input} is {item_cost}€ ')
            if money_machine.make_payment(item_cost):
               coffee_maker.make_coffee(menu.find_drink(user_input))
                
