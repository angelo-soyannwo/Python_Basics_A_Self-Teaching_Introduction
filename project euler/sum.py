
def fib(n, start=1, second=2):
	"""
	Takes in the nth fibbonnaci number
	"""
	if n == 1:
		return start
	elif n == 2:
		return second
	else:
		return fib(n-1) + fib(n-2)


def fib_sum(floor=1, ceiling=4000000):
	"""
	returns the sum of all the fibonacci numbers less than the ceiling
	>>>fib_sum(2)
	2
	"""
	current_num = 0
	sum = 0
	while True:
		current_num = fib(floor)
		if current_num > ceiling:
			break
		if current_num%2 ==0:
			sum += current_num
		floor += 1
	return sum

print(fib_sum())
