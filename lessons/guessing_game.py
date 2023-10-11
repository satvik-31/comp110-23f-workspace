"""Game that only ends when you guess the right number"""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("guess a number between 1 and 10: "))

while guess != secret: 
    print ("Wrong")
    if (guess % 2) == 0:
        print("Your guess should be odd")
    else: 
        (guess % 2) == 1
        print ("Your guess should be even!")
    guess = int(input("Guess Again: "))
print ("You got it!")