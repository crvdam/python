import random

while True:
    level = input("Level: ")
    if level.isnumeric() and int(level) > 0:
        break

goal = random.randint(1, int(level))

while True:
    guess = input("Guess: ")
    if guess.isnumeric() and int(guess) > 0:
        guess = int(guess)
        if guess == goal:
            print("Just right!")
            break
        elif guess < goal:
            print("Too small!")
        elif guess > goal:
            print("Too large!")
