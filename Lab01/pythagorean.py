import math


number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))

hypotenuse = math.sqrt(number_one ** 2 + number_two ** 2)
print(f"The hypotenuse is {hypotenuse:.2f}")