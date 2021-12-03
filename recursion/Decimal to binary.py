

def decimalBinary(x, result):
	if x == 0:
		return result

	result =str(x % 2) + result
	return decimalBinary(x / 2, result)

a = ''
print(decimalBinary(4, a))


