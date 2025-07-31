"""
guess_the_number.py

A simple terminal-based number guessing game.

The computer randomly selects a number between 1 and 100.
The player tries to guess the number, and after each guess,
the program tells the player whether the guess was too high or too low.
It also counts how many attempts the player took before guessing correctly.

Usage:
    Run this script in a Python environment:
        python3 guess_the_number.py

Features:
    - Random number generation using random.randint()
    - User input via input()
    - Conditional logic with if/else
    - Looping with while
    - Try counter with +=

Author: [GkikF]
Date: [20250731]
"""

import random

tries=0
guess=0
secret_number=random.randint(1,100)

while guess!=secret_number:
    guess=int(input("Guess the number: (1-100):"))   
    tries+=1
    if guess!=secret_number:
        if (guess > secret_number):
            print("Wrong! It's a smaller number. Try again.")        
        else:
            print("Wrong! It's greater number. Try again.")

print("You guessed it.")
print("Total tries:", tries)

#Binary search:
#Binary search is an efficient algorithm used to find a target value in a sorted list.
#It works by repeatedly dividing the list in half and checking if the middle value is too high, too low, or just right.
#This method is much faster than checking each item one by one.