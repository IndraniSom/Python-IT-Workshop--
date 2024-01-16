# Write a program that asks the user for two numbers and prints 'Close' if the numbers are within 0.001 of each other and 'Not close' otherwise.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

epsilon = 0.001

if abs(a - b) < epsilon:
    print("The numbers are close.")
else:
    print("The numbers are not close.")