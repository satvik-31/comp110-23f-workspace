"""Game that only ends when you guess the right number"""

from random import randint

secret: int = randint(1,10)
print(secret)


guess: int = int(input("guess a number between 1 and 10: "))

while guess != secret: 
    print ("Wrong")
    if (guess < 1) or (guess > 10):
        print("Thats not between 1 and 10")
    if guess > secret:
        print ("Your guess is too high!")
    else:
        print("Your guess is too low")
    guess = int(input("Guess Again: "))
print ("You got it!")