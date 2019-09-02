# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:10:26 2019

@author: Brock

Rock-Paper-Scissors-Lizard-Spock
"""
import random

def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4
    corresponding 'rock', 'Spock', 'paper', 'lizard', 'scissors'
    """

    if name == 'rock':
        number = 0
    elif name == 'Spock' or name == 'spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print("Please enter either 'rock', 'paper', 'scissors', 'lizard', 'Spock'")
    return number

#print(name_to_number('rock'))       # output - 0
#print(name_to_number('Spock'))      # output - 1
#print(name_to_number('paper'))      # output - 2
#print(name_to_number('lizard'))     # output - 3
#print(name_to_number('scissors'))   # output - 4

## name_to_number() TEST
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """

    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print("Please enter a number in the range of 0 - 4")
    return name

### number_to_name() TEST
#print(number_to_name(0))    # output - 'rock'
#print(number_to_name(1))    # output - 'Spock'
#print(number_to_name(2))    # output - 'paper'
#print(number_to_name(3))    # output - 'lizard'
#print(number_to_name(4))    # output - 'scissors'

def rpsls_action(first, second):
    if first or second == 'scissors':
        if first or second == 'paper':
            action = 'cuts'
        elif first or second == 'lizard':
            action = 'decapitates'
        return action

    if first or second == 'paper':
        if first or second == 'rock':
            action = 'covers'
        elif first.lower() or second.lower() == 'spock':
            action = 'disproves'
        return action

    if first or second == 'rock':
        if first or second == 'lizard':
            action = 'crushes'
        elif first or second == 'scissors':
            action = 'crushes'
        return action

    if first or second == 'lizard':
        if first.lower() or second.lower() == 'spock':
            action = 'poisons'
        elif first or second == 'paper':
            action = 'eats'
        return action

    if first.lower() or second.lower() == 'spock':
        if first or second == 'scissors':
            action = 'smashes'
        elif first or second == 'rock':
            action = 'vaporizes'
        return action


def rpsls(player_choice):
    """
    Given string player_choice, play a game
    of RPSLS and print results to console
    """

    print("")
    print("Player has chosen", player_choice)
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print("The computer has chosen", comp_choice)
    print('')

    result = (player_number - comp_number) % 5


    if result == 3 or result == 4:
        print('Computer wins!')
        action = rpsls_action(player_choice, comp_choice)
        print(comp_choice, 'beats', player_choice)
        print(comp_choice, action, player_choice)

    elif result == 1 or result == 2:
        print('Player wins!')
        action = rpsls_action(player_choice, comp_choice)
        print(player_choice, 'beats', comp_choice)
        print(player_choice, action, comp_choice)
    else:
        print('Tie, try again!')
