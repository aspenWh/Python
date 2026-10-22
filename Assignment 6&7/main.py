#This imports functions from Assignment67.py

from Wordle_functions import choose_word
from Wordle_functions import get_guess
from Wordle_functions import evaluate_guess
from Wordle_functions import display_guess
from Wordle_functions import has_won


#Front page and welcom message of the game

print("-------------------------")
print("Welcome to Mystery Wordle!!")
print("Guess the five-letter word.")
print("G = correct letter and positioning")
print("Y = correct  letter, wrong position")
print("- = letter is not in the word")
print("--------------------------")

play_again = True

#This is the main game loop - 6 attempts to guess secret word
while play_again == True:
    secret_word = choose_word()
    passed_guesses = []
    won = False
    attempt = 1

    while attempt <= 6 and not won:
        print(f"\nAttempt {attempt} of 6")

        players_guess = get_guess(passed_guesses)

        passed_guesses.append(players_guess)

# Evaluate and display the guess
        feedback = evaluate_guess(players_guess, secret_word)
        display_guess(players_guess, feedback)

        if has_won(players_guess, secret_word):
            won = True
            print("congrats you solved the puzzle!!")
            
        attempt = attempt + 1

#Display results and ask if player wants to play again
    if not won:
        print(f"Game over! The secret word was: {secret_word.upper()}")

    answer = input("\nPlay again? (yes/no): ").lower().strip()
    if answer == "yes" or answer == "y":
        print("\nStarting a new game!")
    else:
        play_again = False
        print("Thanks for playing")