# Write a program to take a 3-digit number and then print the reversed number. That is, if the input given is 253, the program should print 352.
num=int(input("Enter the number: "))
number=num
rev=0
while(num!=0):
    digit=num%10
    rev=((rev*10)+digit)
    num=num//10
    
print("The actual number is : ",number)
print("The reversed of the number is: ",rev)