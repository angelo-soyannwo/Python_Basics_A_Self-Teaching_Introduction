
data =  input("PLease enter the numbers from which the mean will be calculated in the form, x1, x2, ..., xn. \t")
numbers = list(map(int,data.split(', ')))


def mean(x):
	i = 0
	n = len(x)
	sum = 0
	while i < n:
		sum += x[i]
		i += 1
	mean = sum / n

	return mean

print(mean(numbers))
