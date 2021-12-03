
def sum_squares(n):
	"""
	returns the sum of the fist n squares of the natural numbers
	>>>sum_squares(10)
	385
	"""
	sum = 0
	for i in range(1, n+1):
		sum += pow(i, 2)
	return sum


def sum_squared(n):
	"""
	returns the square of the sum of the first naturals
	>>>sum_squared(3):
	36
	"""
	def sum_naturals(n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			return n + sum_naturals(n-1)
	return pow(sum_naturals(n), 2)


def main():
	print(sum_squared(100) - sum_squares(100))
if __name__ == '__main__':
	main()
