seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    season = seasons[0]  # Winter
elif month >= 3 and month <= 5:
    season = seasons[1]  # Spring
elif month >= 6 and month <= 8:
    season = seasons[2]  # Summer
elif month >= 9 and month <= 11:
    season = seasons[3]  # Autumn
else:
    season = "Invalid month"

print("The season is:", season)
