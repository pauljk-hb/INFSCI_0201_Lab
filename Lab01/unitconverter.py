user_input = input("Enter a distance or a weight amount (Valid units in, cm, yd, m, oz, g,kg, lb): ")

user_input = user_input.split(" ")
user_unit_number = float(user_input[0])
user_unit = user_input[1]

# unit conversion
if user_unit == "in":
    print(f"{user_unit_number:.2f} in = {user_unit_number * 2.54} cm")
elif user_unit == "cm":
    print(f"{user_unit_number:.2f} cm = {user_unit_number / 2.54} in")
elif user_unit == "yd":
    print(f"{user_unit_number:.2f} yd = {user_unit_number * 0.9144} m")
elif user_unit == "m":
    print(f"{user_unit_number:.2f} m = {user_unit_number / 0.9144} yd")
elif user_unit == "oz":
    print(f"{user_unit_number:.2f} oz = {user_unit_number * 28.349523125} g")
elif user_unit == "g":
    print(f"{user_unit_number:.2f} g = {user_unit_number / 28.349523125} oz")
elif user_unit == "lb":
    print(f"{user_unit_number:.2f} lb = {user_unit_number * 0.45359237} kg")
elif user_unit == "kg":
    print(f"{user_unit_number:.2f} kg = {user_unit_number / 0.45359237} lb")
else:
    print("Invalid unit")
    