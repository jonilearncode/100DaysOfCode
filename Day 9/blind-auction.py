"""
Program: blind-auction
Description: A console program that emulates a
blind auction for several bidders.
Author: Joao Teixeira
Date: 2021.07
Version: 1.202107
"""

from os import system

# Globals
intro = 'Welcome to the secret Blind Auction program.'
auction_logo_ascii = """
                  _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                    
"""
log_book = []

# Aux methods
def check_higher_bid(log):
    high_bid = 0
    winner_log_entry = {}
    for l in log:
        if float([k for k in l.keys()][0]) > high_bid:
            high_bid = [k for k in l.keys()][0]
            winner_log_entry = l
    return winner_log_entry

# Intro
print(auction_logo_ascii)
print(intro)
while True:
    # Input for entry
    # -- Name and bid value
    name = input('\nWhat\'s your name? ')
    bid = float(input('Place your bid: '))
    assert bid >= 0.0, 'You must place a float value for the bid. Ex.: 23.0'
    log_book.append( {round(float(bid), 2) : name} )
    # Input for another entry or finish
    other_biders = input('\nAre there any ohter biders? Type \'y\' or \'n\': ')
    if other_biders == 'y':
        system('cls')
        continue
    elif other_biders =='n':
    # Show winner
        winner = check_higher_bid(log_book)
        winner_bid = [k for k in winner.keys()][0]
        winner_name = winner[winner_bid]
        print(f'\nThe winner is {winner_name.upper()} with {winner_bid}€')
        break
input('\n\nType any key to \'exit\' ... ')