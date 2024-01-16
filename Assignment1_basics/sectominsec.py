# Write a program that reads a number of seconds and prints it in form: mins and
# seconds, e.g., 200 seconds are printed as 3 mins and 20 seconds.
# [Hint. use // and % to get minutes and seconds]
input=int(input("Enter the time in seconds: "))
mins=input//60
sec=input%60
print("Time in minute and seconds: ",mins,sec)