def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = 3.14 * radius_m * radius_m
    price_per_m2 = price_eur / area_m2
    return price_per_m2

diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
price1 = float(input("Enter the price of the first pizza in euros: "))

diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
price2 = float(input("Enter the price of the second pizza in euros: "))

unit1 = unit_price(diameter1, price1)
unit2 = unit_price(diameter2, price2)

print("Unit price of the first pizza: ", round(unit1, 2), "€/m²")
print("Unit price of the second pizza: ", round(unit2, 2), "€/m²")

if unit1 < unit2:
    print("The first pizza is better value for money.")
elif unit2 < unit1:
    print("The second pizza is better value for money.")
else:
    print("Both pizzas have the same value for money.")