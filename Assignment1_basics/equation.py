# Write a program to obtain x, y, z from user and calculate expression: 4x4 + 3y3 + 9z + 6π
x=int(input("Enter the first term: "))
y=int(input("Enter the second term: "))
z=int(input("Enter the third term: "))
py=3.14
s=(4*pow(x,4))+(3*pow(y,3))+(9*z)+(6*py)
print("The result of the equation: ",s)
