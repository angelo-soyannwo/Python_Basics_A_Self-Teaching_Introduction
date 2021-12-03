

def product(a, b):

	if b == 0:
		return 0
	elif b == 1:
		return a

	return product(a, b-1) + a

print(product(3, 7))
