

def mean():
	numbers = input("Please enter the numbers in the form, x1, x2, x3:\t")
	data = list(map(int, numbers.split(", ")))
	n = len(data)
	result = 0
	for i in range(n):
		result += data[i]
	result /= n
	return result

print(mean())
	
