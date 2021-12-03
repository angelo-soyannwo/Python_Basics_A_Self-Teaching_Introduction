

# 1) Generator for triangular numbers
# 2) Function to find the factors
# 3) Use a while loop to find the first triangular number with 100 factors

#1)
def triangular_num(term):
	"""Returns the nth triangular number
	>>>triangular_num(1)
	1
	>>>triangular_num(2)
	2
	"""
	return term*(term+1) / 2

def triangular_nums(n):
	"""returns the first n triangular numbers"""
	for i in range(1, n+1):
		yield triangular_num(i)

def num_factors(num):
	"""Returns the number of factors of the input num"""
	if num == 0:
		return 0
	if num == 1:
		return 1
	if num == 2:
		return 2
	else:
		count = 2
		for i in range(2, int(num**0.5)+1):
			if num%i == 0:
				count += 2
	return count

def main():

	i = 1
	while num_factors(triangular_num(i)) < 500:
		i += 1
	print(i)
	print(num_factors(triangular_num(i)))
	print(triangular_num(i))

if __name__ == '__main__':
	main()
