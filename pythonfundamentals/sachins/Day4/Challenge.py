#create a game
#asks for username and welcome message is displayed
#guesses a random secret number between 1 and 100
#asks user to guess and number
#number is between <1 or >100 - display out of play
#number is less than secret number - display number is less than secret number
#number is greater than secret number - display number is greater than secret number
#number equals secret number - display you won
#display the number of tries taken to won the game
#exit
from random import randint
print("Welcome " + input(" Enter username: "))
secret_number = randint(1,100)
counter = 0
for i in range(1, 9):
    counter = i
    guess = int(input("Guess a number:"))
    if guess < 1 or guess > 100:
        print("Number is out of play!")
    elif guess < secret_number:
        print("Number is lower than secret number")
    elif guess > secret_number:
        print("Number is greater than secret number")
    else:
        print("You guessed it right!")
        break

if counter != 8:
    print(f'You guessed secret number in {counter} tries!')