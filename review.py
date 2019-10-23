# Alan
# Period 4

# Variable declaration and assignment
# Examples
myNum = 12 # integer type
myString = "12" # string type
print(myString + "3") # ok
print()
# Make variable and assign it the value of your favorite movie
# Print "My favorite movie is" followed by the variable
favMovie = input("What is your favorite movie? ")
print("My favorite Movie is " + favMovie)

# While loops
# Example - Print 1 to 10
x = 1
while x <= 10:
	print(x)
	x = x + 1
print()
#count down from 100 using a while loop

x = 100
while x >= 1:
	print(x)
	x = x - 1

# String concatenation
# means putting two string together
# EX
myName = "Alan"
print("Hello " + myName)

#input
#EX
yourName = input("What is your name? ")
print("Hello " + yourName + " Have a nice day")
number = input("Enter a number: ")
number = int(number) + 10
print("The number is " + str(number))

# Ask for 2 numbers, add them and print the sum

number1 = input("First number: ")
number2 = input("\nSecond number: ")

sum = float(number1) + float(number2)
print("{0} + {1} = {2}" .format(number1, number2, sum)) 

# if/else statements
# EX
num = int(input("Enter a number: "))
if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

# ask if today is your birthday
# if yes... print Happy Birthday

bDay = input("Is today your birthday? (yes / no): ")
if (bDay == "yes"):
	print("Happy Birthday")

