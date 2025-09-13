import random

# computer picks a number between 1 and 10 (inclusive)
number = random.randint(1, 10)

print("I have chosen a number between 1 and 10.")
print("Try to guess it!")

while True:
    guess = int(input("Your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed it!")
        break