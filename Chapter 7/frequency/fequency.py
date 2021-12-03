# open file
data = open("test.txt", "r")

#load text data into a variable
r = data.read()
print(r)

#make a set of the characters using arrays
initial = [i for i in r]
characters = list(set(initial))
tracker = [0 for i in range(len(characters))]

def position(array, val):
	for i in range(len(array)):
		if array[i] == val:
			return i

for i in characters:
	x = initial.count(i)
	pos = characters.index(i)
	tracker[pos] += x
	print("Character ", i, " appears ", (tracker[pos]), "times in the file")
