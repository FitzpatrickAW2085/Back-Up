# how to make a list
favMovies = ["Hobbs and Shaw", "Star Wars", "Lone Survivor"]
# Print the whole list
print(favMovies)
# print individuals
print(favMovies[0])
# to add you can append or insert
# append adds it to the end
favMovies.append("Joker")
print(favMovies)
# Insert will put item wherever u want
favMovies.insert(1, "Mission impossible: Fallout")
print(favMovies)
# How to remove items
# remove by name or by index
# remove by name use remove
favMovies.remove("Joker")
print(favMovies)
# favMovies.remove("Endgame")
# pop will remove last item unless an index is given
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remove whatever is in index 1
print(favMovies)

# get the length of a list
# this is a function
# the function name is len
print("My list has " + str(len(favMovies)) + " items")
favMovie = input("What is your favorite movie? ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies) - 1])

# loop through a list
count = 1 

for movie in favMovies:
	print("My number " + str(count) + " movie is " + movie)
	count = count + 1

numList = [1, 4, 2, 7, 5, 9]
# Challenge: loop through the list and add all the numbers together, then print the answer

total = 0

for number in numList:
	total = total + number

print(" The sum is " + str(total))

if "Star Wars" in favMovies:
	favMovies.remove("Star Wars")
	print("removed")
else:
	print("not in list")