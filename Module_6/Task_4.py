def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

my_list = [2, 4, 6, 8, 9]

result = sum_of_list(my_list)

print("The sum is:", result)

