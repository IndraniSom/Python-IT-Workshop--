# Write a program to take a 3-digit number and then print the reversed number. That is, if the input given is 253, the program should print 352.
x=float(input("Enter the centimeter: "))
if(x<0):
    print("Invalid Input")
else:
    y=(2.54*x)
    print("%.2f cm = %.2f inch" % (x,y))