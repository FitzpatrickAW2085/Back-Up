import time
import os

#variables
hours = 0
minutes = 0
seconds = 0

# input
print("Enter the number of hours, minutes, and seconds for the timer")
hours = int(input("hours: "))
#for cash register: price = float(input("Enter the price:"))
minutes = int(input("minutes: "))
seconds = int(input("seconds: "))

#convert to seconds #convert things to pennies-decimal point to pennies: $1.53*100=153 pennies
minutes += hours * 60
seconds += minutes * 60

# Set hours and minutes to 0
hours = 0
minutes = 0

# start countdown loop
while seconds >= 0:
	# convert back to hours, minutes, seconds
	minutes = int(seconds / 60) #going backwards and dividing now: int is put in here to get rid of decimal point
	seconds = seconds % 60 #153 pennies/100 converts it to a dollar... 153 mod 100

	hours = int(minutes / 60)
	minutes = minutes % 60
	#print time
	print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

	#convert to seconds
	minutes += hours * 60
	seconds += minutes * 60

	# Set hours and minutes to 0
	hours = 0
	minutes = 0

	# pause for 1 second
	time.sleep(1)
	#clear screen
	os.system("cls")
	seconds -= 1 #subtract a second makes it keep going

print("Times up")