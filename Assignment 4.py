import random


def one_play():
    print("Welcome to the higher/lower game")
    solution = random.randint(1, 100)
    number_guesses = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Invalid guess. Please enter a number between 1 and 100.")
            continue

        number_guesses += 1
        if guess > solution:
            print("Lower")
        elif guess < solution:
            print("Higher")
        else:
            print("You guessed it")
            return number_guesses


number_guesses = one_play()
print(f"It took you {number_guesses} guesses.")


