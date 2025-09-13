# Hemoglbin value checker
gender = input("Enter your gender (male or female: ").lower()
hemoglobin = int(input("Enter your hemoglobin value in g/l: "))

if gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low:")
    elif hemoglobin > 167:
        print("Your hemoglobin value is high:")
    else:
        print("Your hemoglobin value is normal:")

elif gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low:")
    elif hemoglobin > 155:
        print("Your hemoglobin value is high:")
    else:
        print("Your hemoglobin value is normal:")

else:
    print("Invalid gender entered.")