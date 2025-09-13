USERNAME = "python"
PASSWARD = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWARD:
        print("Welcome")
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. Attempts left: {max_attempts - attempts}")
else:
    print("Access denied")
