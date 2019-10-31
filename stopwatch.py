import time
import os

seconds = 0
minutes = 0
hours = 0

while True:
	print(str(hours) +":" + str(minutes) + ":" + str(seconds))
	seconds += 1
	if seconds == 60:
		seconds = 0
		minutes += 1
	if minutes == 60:
		minutes = 0
		hours += 1

	time.sleep(1)
	os.system("cls")