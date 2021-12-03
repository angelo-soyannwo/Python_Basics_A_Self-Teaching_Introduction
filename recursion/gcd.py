

def gcd(a, b):
	if a > b:
		least = b
		higher = a
	else:
		least = a
		higher = b

	if higher%least == 0:
		return least 
	else:
		return gcd(higher, least-1)

print(gcd(32, 4))
