

def add(a, b):
	if b == 0:
		return a

	return add(a, b-1) + 1

print(add(9, 15))


