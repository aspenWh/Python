#generate code inspired by wordle 
#Computer will generate a secret 5 letter word. Player gets six attempts to guess the word

import random


def choose_word():
    #This function will randomly select a 5-letter word from a predefined list of words
    words = ["Pear", "Mango", "Grape", "Peach", "plum"]
    return random.choice(words)

def get_guess(previous_guesses):
    # Keep guessing until player enters a valid guess
    while True:
        guess = input("enter a 5-letter word: ").upper()

        if len(guess) != 5 or not guess.isalpha():
            print("please enter 5 letters.")
        elif guess in previous_guesses:
            print("you already guessed that word. Try again.")
        else:
            return guess

        def evaluate_guess(guess, secret_word):
            feedback = [] #this will hold the feedback
            for i in range(5):
                if guess[i] == secret_word[i]:
                    feedback.append("G") #G for green
                elif guess[i] in secret_word:
                        feedback.append("Y") #Y for yellow
                else:
                    feedback.append("-") 

        def display_guess(guess, feedback):
            #Display the guess and feedback to the player
            print("Guess:    ", " ".join(guess))
            print("Feedback:  ", " ".join(feedback))

        def has_won(guess, secret_word):
                return guess == secret_word