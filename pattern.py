def nthOdd(n):
	"""
	takes in an integer n and returns the nth odd number
	>>>nthOdd(5)
	9
	"""
	return 1 + (n-1)*2

def pattern(rows):
	"""
	takes in number of rows and prints out the pattern
	>>>pattern(2)
	 *
	***
	"""
	end = nthOdd(rows)
	mid = end // 2 + 1
	for i in range(1, end+1, 2):
		spaces = (mid-(i//2 + 1))*' '
		print(spaces, end='')
		for n in range(i):
			print('*', end='')
		print()

pattern(5)
