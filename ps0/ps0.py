# import math
# x = int(input("Enter any number x: "))
# y = int(input("Enter any number y: "))
# print("x to the power of y is", x**y)
# print("log base 2 of x is", math.log(x, 2))



number = float(input("Type any integer natural number greater than 1: "))

steps = 0

while number > 1:
    if number % 2 == 0:
        number = number/2
    else:
        number = (3*number)+1
    steps += 1

print("It took", steps, "step" if steps == 1 else "steps", "to reduce your number to 1")  # If it took 1 step, print
# "step" instead of "steps"


