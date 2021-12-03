

def count_digits(x):
	k = 0
	copy = x
	while copy <= 0:
		copy //2
		k += 1
	return k

print(count_digits(21))
