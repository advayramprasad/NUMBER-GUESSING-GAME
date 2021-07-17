import random
print("Number Guesing Game!")
numbers = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("Guess the number:"))
    if guess == numbers:
        print("congratulations you have guessed the right number")
        break

    elif guess < numbers:
        print("your guess was to low guess a higher number")

    elif guess > numbers:
        print("your guess was to high guess a lower number")
    
    chances = chances+1
if chances >= 5:
    print("YOU LOST . THE ACTUAL NUMBER IS ",numbers)