
def sum_3_5(n):
	"""
	returns the sum of multiples of 3 and 5 below n
	"""
	sum = 0
	for i in range(n):
		if i%15 == 0:
			sum += i
			continue
		elif i%5 == 0:
			sum += i
		elif i%3 == 0:
			sum += i
	return sum

print(sum_3_5(1000))

