# import random module
import random
# initial message
print("Welcome to the random number guessing game.")
# generate random integer between 1 and 100
randomNumber = random.randint(1,100)
# get user input for guess
guess = int(input("Guess the number that I am thinking of(1-100): "))

# checks if the user gussed the correct number and prints outcome message
if guess == randomNumber:
    print("You guessed it!")
else:
    print(f"Sorry you didn't get it. Your guess was {abs(randomNumber - guess)} away.")
    # gayson
