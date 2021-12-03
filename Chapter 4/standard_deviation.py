import math

numbers = input("Enter your numbers in the form: x1, x2, x3, ..., xn: \t")
data = list(map(int, numbers.split(", ")))

sum_of_squares = 0

def mean(iter):
	n = len(iter)
	sum = 0
	for i in range(len(iter)):
		sum += iter[i]
	mean = sum / n
	return mean

def variance(iter):

	x = mean(iter)
	sum_of_squares = 0
	n = len(iter)

	for i in range(n):
		sum_of_squares +=  iter[i]**2
		
	mean_of_squares = sum_of_squares / n

	variance = mean_of_squares - x**2
	
	return variance

std = (variance(data))**0.5

print("The variance of the data is ", variance(data))
print("The standard deviation of the data is ", std)

