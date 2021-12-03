

def power(a, b):
	if b == 0:
		return 1
	elif b == 1:
		return a
	else:
		return power(a, b-1) * a
print(power(8, 3))
