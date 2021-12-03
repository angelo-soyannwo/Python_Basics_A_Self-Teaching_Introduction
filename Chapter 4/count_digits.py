

def count_digits(x):
	
	i = 0
	copy = x
	while copy > 0:
		copy = copy // 10
		i += 1
	print(str(x) + " has " + str(i) + " digits")

count_digits(12345678)

