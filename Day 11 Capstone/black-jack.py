"""
Program: black-jack
Description: A console Black Jack card game. 
Emulates infinite decks for the dealer. 
Card extraction doesn't change probabilities for the next 'hit'.
Split cards is not featured.
Author: Joao Teixeira
Date: 2021.08
Version: 1.202108   
"""

# Basic Blackjack Rules:
#     The goal of blackjack is to beat the dealer's hand without going over 21.
#     Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
#     Each player starts with two cards, one of the dealer's cards is hidden until the end.
#     To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
#     If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
#     If you are dealt 21 from the start (Ace & 10), you got a blackjack.
#     Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
#     Dealer will hit until his/her cards total 17 or higher.
#     Doubling is like a hit, only the bet is doubled and you only get one more card.
#     Split can be done when you have two of the same card - the pair is split into two hands.
#     Splitting also doubles the bet, because each new hand is worth the original bet.
#     You can only double/split on the first move, or first move of a hand created by a split.
#     You cannot play on two aces after they are split.
#     You can double on a hand resulting from a split, tripling or quadrupling you bet.

import os, random, time

# Globals
intro = '\n\nWelcome to PyBlackJack. Made by Joao Teixeira 2021'
logo = """

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                       _/ |                
                      |__/

"""
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
end = False
player_hand = []
dealer_hand = []

# Aux methods
def pull_a_card(target_deck):
    return target_deck[random.randint(0, target_deck[len(target_deck) -1])]

def initial_hit():
    # draws first hands of the game
    dealer_hand.append('X')
    dealer_hand.append(pull_a_card(deck))
    player_hand.append(pull_a_card(deck))
    player_hand.append(pull_a_card(deck))
    return player_hand, dealer_hand 

def p_hit():
    # add new card to player and update player_hand[]
    player_hand.append(pull_a_card(deck))

def p_stand():
    # add new card to dealer and update dealer_hand[]
    dealer_hand.append(pull_a_card(deck))

def get_hand_score(hand):
    total = 0
    catch_11_index = -1
    for c in hand:
        if c == 11:
            catch_11_index = c
        total += int(c)
    # implement ace double value 11 or 1
    if catch_11_index > 0 and total > 21:
        # we want ace to equal 1 instead 11.
        total -= 10
    return total

def show_hands():
    os.system('cls')
    d_score = ' ? '
    print('\n-- DEALER --')
    if dealer_hand[0] != 'X':
        d_score = get_hand_score(dealer_hand)
    print(f'{dealer_hand} -- score = {d_score}')
    print('\n--- YOU ---')
    print(f'{player_hand} -- score = {get_hand_score(player_hand)}')

def eval_bust(hand):
    if get_hand_score(hand) >= 21:
        return True
    else:
        return False

def result():
    p_score = get_hand_score(player_hand)
    d_score = get_hand_score(dealer_hand)
    if p_score == d_score:
        return 'DRAW'
    elif p_score > d_score and p_score <= 21:
        return 'Player WINS'
    elif d_score > p_score and d_score <= 21:
        return 'Dealer WINS'
    elif p_score > 21:
        return 'Dealer WINS'
    elif d_score > 21:
        return 'Player WINS'

# Main-logic
print(logo)
print(intro)
while not end:
    player_hand.clear()
    dealer_hand.clear() 
    player_hand, dealer_hand = initial_hit()
    time.sleep(1.5) # for better user playability
    show_hands()
    is_game_running = True
    while is_game_running:
        # prompt for hit/stand
        pick = input('\nType \'h\' for HIT or \'s\' for STAND >  ')
        if pick == 'h':
            p_hit()
            show_hands()
            time.sleep(1.0) # for better user playability
            if not eval_bust(player_hand):
                continue
            else:
                # reveal dealer hand hidden card
                dealer_hand[0] = pull_a_card(deck)
                break
        elif pick == 's':
            # show dealer hidden card in 'X' dealer_hand[0]
            dealer_hand[0] = pull_a_card(deck) 
            while True:
                if get_hand_score(dealer_hand) < 17:
                    p_stand()
                show_hands()
                time.sleep(1.0) # for better user playability
                if get_hand_score(dealer_hand) >= 17:
                    is_game_running = False
                    break

    show_hands()            
    print(f'\n\n --- RESULTS --- > {result()}')                
    if input('\n\nPlay again (y/n) ?  ') == 'n':
        end = True

input('\n\nThanks for playing. Goodbye! ')