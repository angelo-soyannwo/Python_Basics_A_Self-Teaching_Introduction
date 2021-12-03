
def word_set(array):
	words = []
	n = len(array)
	for i in range(n):
		if array[i] not in words:
			words.append(array[i])
	return words

#Count occurrences of a word in the file

def freq(array, val):
	sum = 0
	for i in array:
		if i == val:
			sum += 1
	return sum



#do automate the counting proces using a function

def forward_pass(array, store, val, store_index):
	store[store_index] += freq(array, val)




#function to find the words in the file used the least 
	
def least(array):
	least_times = []
	for i in range(len(array)):
		if array[i] == 1:
			least_times.append(i)
	return least_times



def find(array, val):
	x = array.index(val)
	if type(x) == int:
		return x
	else:
		return str(val) + " is not in the file"
	

def main():
	# open file and parse it intwo words words
	file = open("text.txt", "r")
	r = file.read()
	data = r.split()
	file.close()
	words = word_set(data)

	tracker = [0 for i in words]
	
	for i in range(len(words)):
		forward_pass(data, tracker, words[i], i)

	print(" \'it\' appears " + str(tracker[find(words, 'it')]) + " times in the file")
	


if __name__ == "__main__":
	main()
