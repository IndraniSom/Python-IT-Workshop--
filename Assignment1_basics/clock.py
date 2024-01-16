# Write a program that reads from user — (i) an hour between 1 to 12 and (ii)
# number of hours ahead. The program should then print the time after those many
# hours, e.g.,
# Enter hour between 1-12 : 9
# How many hours ahead : 4
# Time at that time would be : 1 O'clock
hour=int(input("Enter the hour bet (1-12): "))
ahead=int(input("How many hours ahead? "))
if hour>=1 and hour<=12:
    time=hour+ahead
    if time>12:
        print("Time at that time would be : %d o'clock" %(time-12))
    else:
        print("Time at that time would be : %d o'clock" %time)