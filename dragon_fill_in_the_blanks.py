import random
import time

"""Complete the exercises below to make the program run"""


def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    """Exercise 1: Call the display intro function"""



    """Exercise 2: Use the choose cave function to get user's choice"""
    caveNumber = ...



    """Exercise 3: Call the check cave function"""



    print('Do you want to play again? (yes or no)')
    
    """Exercise 4: Use the input function"""
    playAgain = ...
