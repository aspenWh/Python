#play_again = y

#While user has pressed "y"
    #Computer generates a random number between 1 and 100 (suto code)

     #while the user has not guessed the number

     #While the user has not guessed the number

        #ask the user for guess between 1 and 100

        #While the guess is < 1 or > 100
        #     print "Invalid guess. please try again"

        #Increment number of guesses

    #If guess is > the number
    #print "Lower"
    #If guess is < to the number 
    #print "Higher"
    #If guess is equal to the number 
    # Print "Congradulations"

#loop

    #print the number of guesses

    #If number of guesses <= 3
    #    print "you are amazing"
    #Else If number of guesses <= 5
    #    print "Impressive"
    #Else If number of guesses <= 7
    #    Print "Good Job"
    #Else If number of guesses <= 9
    #    print "Took a little longer, but you got it!"
    #Else If number of guesses >= 10
    #    print "you need to lock in"

#Ask user to press "y" of they want to play again

#Loop
import random
#user must guess number
guess = int(input("enter your guess"))
secret_number = random.randint(1, 100)
counter = counter+1 
print counter
if guess > secret_number:
    print ("Lower")
elif guess < secret_number:
    print ("Higher")
elif guess == secret_number:
    print ("Congradulations")
else:
    print("Invalid error - try again")

number_input = (1, 100) 

while guess != (secret_number)
# != is when it is the secret number
