# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)

# Exercise 1: Change the line below to print "Well, <User's name>, I am thinking of a number between 1 and 20."
print(f"Well, {myName}, I am thinking of a number between 1 and 20.")

# Exercise 2: Change the below to have the user guess for at most 6 times
for guessesTaken in range(6):

    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    # Exercise 3: Fill in blanks in the "if" statements 
    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    
    # Exercise 4: Change the line below to print "Good job, you got it right in <number of user's guesses>."
    print(...)

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')