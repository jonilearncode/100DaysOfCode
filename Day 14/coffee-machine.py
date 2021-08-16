"""
Program: coffee-machine
Description: Main logic for a coffee machine. Managing resources and currency to sell
coffee products to user. Implementation done with PROCEDURAL PROGRAMMING.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108
"""

import time, os

# Globals
intro = '\nWelcome to PyCoffeeMachine. Made by Joao Teixeira 2021.'
logo = """

    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \ 
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \ 
\_____________________/

"""
txt_switch_off = 'Goodbye!'
resources = {'raw' : {'water' : 100, 
                      'milk' : 50, 
                      'coffee' : 75}, 
             'money' : {'quarters' : 0.25, 
                        'dimes' : 0.10, 
                        'nickles' : 0.05, 
                        'pennies' : 0.01,
                        'bank' : 200},
             'cost' : {'espresso' : 1.00, 
                       'latte' : 1.50,
                       'cappuccino' : 2.50}
             }
credit_in_session = 0.0

# Aux methods
def print_report(dict_resources):
    w = dict_resources['raw']['water']
    m = dict_resources['raw']['milk']
    c = dict_resources['raw']['coffee']
    b = dict_resources['money']['bank']
    print(f'Water = {w} ml\nMilk = {m} ml\nCoffee = {c} g\nBank = {b} €')

def process_product(product, dict_resources):
    resources_updated = dict_resources.copy()
    if product == 'espresso':
        dict_resources['raw']['water'] -= 50.0
        dict_resources['raw']['coffee'] -= 4.0
    elif product == 'latte':
        dict_resources['raw']['water'] -= 10.0
        dict_resources['raw']['milk'] -= 50.0
        dict_resources['raw']['coffee'] -= 5.0
    elif product == 'cappuccino':
        dict_resources['raw']['water'] -= 25.0
        dict_resources['raw']['milk'] -= 25.0
        dict_resources['raw']['coffee'] -= 3.0
    return resources_updated    

def can_process(product, dict_resources):
    if product == 'espresso':
        if dict_resources['raw']['water'] >= 50.0 and dict_resources['raw']['coffee'] >= 4.0:
            return True
    elif product == 'latte':
        if dict_resources['raw']['water'] >= 10.0 and dict_resources['raw']['milk'] >= 50.0 and dict_resources['raw']['coffee'] >= 5.0:
            return True
    elif product == 'cappuccino':
         if dict_resources['raw']['water'] >= 25.0 and dict_resources['raw']['milk'] >= 25.0 and dict_resources['raw']['coffee'] >= 3.0:
            return True
    return False

def process_money_cost(actual_credit, product_cost):
    print(f'Please insert {product_cost - actual_credit}€: ')
    q, d, n, p = 0.25, 0.10, 0.05, 0.01
    quarters_inserted = int(input('How many \'Quarters\': '))
    dimes_inserted = int(input('How many \'Dimes\': '))
    nickles_inserted = int(input('How many \'Nickles\': '))
    pennies_inserted = int(input('How many \'Pennies\': '))
    # inserted_amount_by_coin_qdnp = [quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted]
    inserted_amount = round(actual_credit + q * quarters_inserted + d * dimes_inserted + n * nickles_inserted + p * pennies_inserted, 2) 
    diff = round(product_cost - inserted_amount, 2)
    return inserted_amount, diff

def transact_to_bank(amount_to_bank, dict_resources):
    dict_resources['money']['bank'] += amount_to_bank

def run_waiting(time_per_tick):
    os.system('cls')
    print(f'\nBrewing your {user_input}. Please Wait *')
    time.sleep(time_per_tick)
    os.system('cls')
    print(f'\nBrewing your {user_input}. Please Wait * *')
    time.sleep(time_per_tick)
    os.system('cls')
    print(f'\nBrewing your {user_input}. Please Wait * * *')
    time.sleep(time_per_tick)

# Main Logic
print(logo, intro)
while True:
    print(f'\nCredit: {credit_in_session}€')
    user_input = input('What would you like? (espresso/latte/cappuccino):  ').lower()
    if user_input == 'off':
        print(txt_switch_off)
        break
    elif user_input == 'report':
        print_report(resources)
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            if can_process(user_input, resources):
                credit_in_session, missing_amount = process_money_cost(credit_in_session, resources['cost'][user_input])
                if missing_amount > 0.0:
                    print(f'Not enough money. Missing {missing_amount}.')
                    continue
                elif missing_amount <= 0.0:
                    transact_to_bank(resources['cost'][user_input], resources)
                    credit_in_session = 0.0
                    resources = process_product(user_input, resources)
                    n_ite = 0
                    while n_ite < 5:
                        run_waiting(0.4)
                        n_ite += 1
                    print(f'Here is your {user_input}. Enjoy!')
                    print(f'Take your change: {abs(missing_amount)}€')
            else:
                print(f'Can\'t deliver your {user_input}. Out of resources! Pick another one.')

input('Type any key to \'exit\' ... ')
