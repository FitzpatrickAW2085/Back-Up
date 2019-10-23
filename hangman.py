myWords = ["hello", "America", "Avengers", "Computer", "Football", "Washington", "Tesla"]

letter = input("Type a letter: ")

dashes = "-" * len(myWords)
guesses_left = 13

if letter in myWords:
	print("Letter is in the word")
else:
	print("Letter is not in the word")

count = 0
for l in myWords:
	if l == letter:
		print(count)
	count += 1




#string into list
myString = "America"
myList = list(myString)
print(myList)




#Create list with underscores where the letters go
guessList = []
for a in myList:
	guessList.append("_")
print(guessList)




# How to replace specific item in the list
# so say the user types m for a guess you would 
guessList[1] = "m"
print(guessList)

choice = input ("type a word: ")







secretWord = "America"
secretWord = List(secretWord)
hangmanList = ['''
    +---+
    	|
    	|
    	|
       ===''', "second", "third"]

misses = 0

while misses < 7:
	guess = input("guess a letter: ")
	if guess in secretWord: 
		#loop through secret word and change my guessList at the correct indexes
		print("letters is in the word")
	else:
		misses += 1
		print(hangmanList[misses])

print("Game Over")





if choice == myWords:
	print("Its a match")
else:
	print("Not a match")