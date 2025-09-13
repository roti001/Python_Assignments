# Zender size limit check
zender_length = int(input("Enter the length of your Zender in cm: "))

if zender_length >= 42:
    print("You may keep the fish.")

else:
    difference = 42 - zender_length
    print(f"Release the fish back into the lake. It is {difference} cm below the size limit")