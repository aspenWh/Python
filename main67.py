import Assignment67

def play_game():
    secret_word = Assignment67.choose_word()
    previous_guesses = []
    won = False

    print("\nGuess the five letter word.")
    print("G = correct letter and positioning")
    print("Y = correct letter, wrong positioning")
    print("- = letter not in the wor")

    # Give the player 6 attempts to guess the word.
    for attempt in range(1, 7):
        print(f"\nAttempt {attempt} of 6")
        guess = Assignment67.get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = Assignment67.evaluate_guess(guess, secret_word)
        Assignment67.display_guess(guess, feedback)

        if Assignment67.has_won(guess, secret_word):
            print("Congratulations! You've guessed the word correctly!")
            won = True
            break

    if not won:
        print(f"Sorry, you've used all attempts. The secret word was: {secret_word}")


#main program
print("Welcome to worddle!")

play_again = "yes"

while play_again == "yes":
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("Thanks for playing!")