# Write a program
# Ask a user to guess a number 
# Randomly generate the number
# Guess until you get it right

import random
import sys


answer = random.randint(low := int(sys.argv[1]), high := int(sys.argv[2]))
message = f"Guess a number ({low}~{high}): " #initial message for first input prompt


while True:
    try:
        guess = int(input(message))
        if low <= guess <= high:
            if guess == answer:
                print("Correct! Good job!")
                break
            else:
                message = f"Wrong! Please guess again ({low}~{high}): " #becomes the new input prompt
                continue
        else:
            print(f"Please enter a number between {low} and {high}...")
            continue
    except ValueError:
        print("Please enter a number...")
        continue
