#Game of Rock, Paper, Scissors
import random

#This is getting them to input their choice
def get_player_choice():  
    choice = input("Enter your choice (rock, paper, scissors): ").lower()

    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    return choice

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"

#This will be the introduction to the game
print("Welcome to the Game of Rock, Paper, Scissors!")

rounds = int(input("How many rounds would you like to play? "))

while rounds % 2 == 0:
        print("The number of rounds must be odd.")
        rounds = int(input("How many rounds would you like to play? "))

player_wins = 0
computer_wins = 0
games_played = 0

while games_played < rounds:

    player_choice = get_player_choice()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("The computer chose", computer_choice + ".")

# This is determining the winner of the round
    result = determine_winner(player_choice, computer_choice)
   
    if result == "win":
        print("You win this round!")
        player_wins += 1
        games_played += 1
    elif result == "loss":
        print("You lose this round.")
        computer_wins += 1
        games_played += 1
    else:
        print("This round is a tie! Play again.")

# This is displaying the final results of the game
print("----------------------------------------")
print("Score - You:", player_wins, "Computer:", computer_wins)
if player_wins > computer_wins:
    print("Congratulations! You won the game!")
elif player_wins < computer_wins:
    print("Sorry! The computer won the game.")


print("Thank you for playing!")
#This is the end of the game