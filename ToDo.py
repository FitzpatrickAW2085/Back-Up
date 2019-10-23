print("Welcome to the To Do List")
todolist = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")

	choice = input("Make your choice:")
	if choice == "q":
		break
	elif choice == "a":
		choice = input("What would you like to add? ")
		todolist.append(choice)
		print(todolist)
		
	elif choice == "r":
		choice = input("What would you like to remove? ")
		todolist.remove(choice)
		print(todolist)
		
		
	elif choice == "p":
		print(todolist)
	
		
	else:
		print("That is not a choice")

count = 1 

for task in todolist:
	print("Task # " + str(count) + " is " + task)
	count = count + 1
	