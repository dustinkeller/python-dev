import random

low = 1
high = 10

answer = random.randint(1,10)

    
def run_guess(guess, answer):
    if not 1 <= guess <= 10:
        print("Please enter a number between 1 and 10...")
    return guess == answer

if __name__ == '__main__':
    while True:
        try:
            guess = int(input("Guess a number 1 - 10: "))
            output = run_guess(guess, answer)
            if output:
                print("You're a genius!")
                break
            print("Wrong, please try again...")
        except ValueError:
            print("Please enter a number...")