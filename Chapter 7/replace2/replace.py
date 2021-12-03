def word_list(array):
	words = []
	words = [array[i][j] for i in range(len(array)) for j in range(len(array[i])) if array[i][j] not in words]
	return words

def change_word(x, a, b):
	x.replace(a, b)

def main():
	file = open("text.txt", "r")
	r = file.readlines()
	for i in range(len(r)):
		r[i] = r[i].replace("simply", "zebra")
	file.close()

	file2 = open("text.txt", "w")
	for i in r:
		file2.write(i)
	file2.close()



if __name__ == "__main__":
	main()
