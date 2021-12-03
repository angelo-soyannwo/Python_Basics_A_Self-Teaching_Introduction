

def factors(x):
	half = (x // 2) + 1
	factors = []
	
	if x == 0:
		return factors
	
	for i in range(1, half):
		if x % i == 0:
			factors.append(i)
	factors.append(x)
	return factors
	
print(factors(8934))
