# Assignment 3: Number Guessing Game
# The computer will generate a random number between 1 and 100, and the user will have to guess it.

#This tells program to import the random module so that it can generate a random number
import random

#this is where the game starts
play_again = 'y'

# This is the main loop that will keep the game running as long as the user wants to play again
while play_again.lower() == 'y':
    secret_number = random.randint(1, 100)
    print("Pick a number between 1 and 100")

    # This will count the number of guesses the user has made
    guesses = 0

#This will tell play if they need to guess higher or lower than the number they guessed
    while True:
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
            print("Invalid guess. Please try again.")
        else:
            guesses += 1
            if guess < secret_number:
                print("Higher")
            elif guess > secret_number:
                print("Lower")
            else:
                print(f"Congratulations! You've guessed the number in {guesses} tries.")
                break

#This will give the user feedback based on how many guesses they took to get the right answer
    if guesses <= 3:
        print("You are amazing!")
    elif guesses <= 5:
        print("Impressive!")
    elif guesses <= 7:
        print("Good job!")  
    elif guesses <= 9:
        print("Took a little longer, but you got it!")
    else:
        print("You need to lock in!")

    # This will ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    print("Thank you for playing!")
    