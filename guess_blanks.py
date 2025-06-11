# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)

# Exercise 1: Change the line below to print "Hi, <User's name>, guess a number from 1 to 20"
print(...)

# Exercise 2: Change the below to have the user guess for 6 times
for guessesTaken in ...:

    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    # Exercise 3: Fill in blanks in the "if" statements 
    if ...:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if ...:
        print('Your guess is too high.')

    if guess == number:
        # Exercise 4: What should we do if the guess is correct? Fill in below.
        # This is not the place where we print the final line. Look at Exercise 5 for details.
        ...

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    
    # Exercise 5: Change the line below to print "Good job, you got it right in <number of user's guesses>."
    print(...)

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')