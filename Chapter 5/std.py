

def std():
	initial = input("Please enter your numbers in the form x1, x2, x3, ...  xn:\t")
	numbers = list(map(int, initial.split(", ")))
	
	n = len(numbers)
	sum_of_squares = 0

	mean = sum(numbers)/n

	for i in range(n):
		sum_of_squares += numbers[i]**2

	variance = (sum_of_squares/n) - mean**2
	standard_dev = variance**0.5
	
	return(standard_dev)

print(std())
