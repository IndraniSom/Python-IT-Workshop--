# Write a program to compute (a + b)3 using the formula a3 + b3 + 3a2b + 3ab2
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
ans=(pow(a,3)+pow(b,3)+(3*(pow(a,2))*b)+(3*a*(pow(b,2))))
print("The result of (a+b)3 : ", ans)