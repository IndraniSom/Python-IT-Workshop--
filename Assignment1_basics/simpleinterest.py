# Write a program to obtain principal amount, rate of interest and time from user and compute simple interest.
p=int(input("Enter the principle amount: "))
r=int(input("Enter the rateo interest: "))
t=int(input("Enter the time period: "))
si=(p*r*t)/100
print ("The simple interest is: ",si)