
def count(array):
	sum = 0
	for i in array:
		sum +=  len(array[array.index(i)])
	return sum

def count_spaces(string):
	x = 0
	for i in range(len(string)):
		if string[i] == " ":
			x += 1
	return x

def auto_count_spaces(array):
	n = len(array)
	sum = 0
	for i in range(n):
		sum += count_spaces(array[i])
	return sum

def main():
	file = open("test.txt", "r")
	data = file.readlines()
	file.close()

	r = []
	for i in data:
		r.append(i)
	print(file.name)
	print("There are " + str(count(r)) +  " characters in the file.")
	print("The file contains " + str(auto_count_spaces(r)) + " spaces")
	
if __name__ == "__main__":
	main()
