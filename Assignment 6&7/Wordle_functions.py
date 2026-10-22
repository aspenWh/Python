#This function selects and returns the secret word from this list
import random


def choose_word():
    words = ["Piles", "Pears", "Slate", "Words", "Pearl", "Plant", "Cloud", "Dream", "Flame", "Asset", "Bride", "Pants", "Stone", "Lines", "Light"]
    secret_word = random.choice(words)
    return secret_word.lower()

#This makes sure its a valid guess
def get_guess(passed_guesses):
    meets_criteria = False
    players_guess = ""

    while meets_criteria == False:

        players_guess = input("Enter a five-letter word: ").lower().strip()
        length_of_players_guess = len(players_guess)

        if length_of_players_guess == 5:
            if players_guess.isalpha():
                if players_guess not in passed_guesses:
                    meets_criteria = True
                
                else:
                    print("Please guess a word you haven't guessed before.")
            else:
                print("Please only imput letters.")
        else:
            print("Word is not 5 letters. Please try again")
            
    return players_guess

#This function compares guess to secret word and returns G,Y, or -
def evaluate_guess(players_guess, secret_word):
    feedback = []

    for i in range(len(players_guess)):
        if players_guess[i] == secret_word[i]:
            feedback.append("G")
        elif players_guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback

#This function displays the guess and its feedback
def display_guess(players_guess, feedback):
    print("Guess: " + " ".join(players_guess).upper())
    print("feedback: " + " ".join(feedback))

#This function checks whether the player won
def has_won(players_guess, secret_word):
    return players_guess == secret_word