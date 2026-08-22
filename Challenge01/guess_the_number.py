"""
Instructions:

You’re going to make a Guess the Number game. The computer will think of a secret number from 1 to 20 and ask the user to guess it. After each guess, the computer will tell the user whether the number is too high or too low. The user wins if they can guess the number within six tries. Here’s what the Guess the Number program looks like to the player when it’s run. The player’s input is marked with >:
""" 
import random

number = random.randint(1, 20)

def main():
    name = input("Hello! What is your name?\n> ");

    guess = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n > "))

    i = 1
    while(guess != number):
        i+=1

        if(guess > number):
            guess = int(input(f"Your guess is too high.\nTake a guess.\n > "))
        else:
            guess = int(input(f"Your guess is too low.\nTake a guess.\n > "))

    print(f"Good job, {name}! You guessed my number in {i} guesses!")
    return;


if __name__ == "__main__":
    main()