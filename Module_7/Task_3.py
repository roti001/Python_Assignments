airports = {}

while True:
    print("\nChoose an option:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        icao = input("Enter the ICAO code of the airport: ").upper()
        name = input("Enter the name of the airport: ")
        airports[icao] = name
        print(f"Airport {name} with ICAO {icao} has been added.")

    elif choice == "2":
        icao = input("Enter the ICAO code of the airport: ").upper()
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print("No airport found with that ICAO code.")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
