import random

num_dice = int(input("How many dice do you want to roll? "))

total = 0
for i in range(num_dice):
    total += random.randint(1,6)

print("Total sum of all dice is: ", total)