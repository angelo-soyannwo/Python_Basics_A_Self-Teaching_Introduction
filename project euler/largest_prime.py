
def is_prime(num):
	"""
	returns true if a number is prime.
	"""
	if num == 0:
		return False
	elif num == 1:
		return False
	else:
		for i in range(2, (int(num/2) + 1)):
			if num%i==0:
				return False
	return True


def big_prime(num):
	result = 1
	for i in range(1, int(num/2) + 1):
		if num%i == 0 and is_prime(i):
			result = i
			print(result)
	return result

print(big_prime(600851475143))
