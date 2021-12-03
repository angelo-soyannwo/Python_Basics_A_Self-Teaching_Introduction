
def countDigits(n):
	"""Returns the number of digits of n"""
	if n == 0:
		return 1
	else:
		num = n
		count = 0
		while num != 0:
			num //= 10
			count += 1
		return count

def sumDigits(n):
	"""Returns the sum of the digits in n"""
	if n == 0:
		return 0
	else:
		result = 0
		num = n
		while num != 0:
			result += num%10
			num //= 10
		return result

def main():
	print(sumDigits(2**1000))


if __name__ == '__main__':
	main()
