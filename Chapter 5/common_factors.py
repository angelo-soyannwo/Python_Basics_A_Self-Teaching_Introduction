

def common_factors(a, b):
	x = a * b
	factors = []
	if a > b:
		least = b
	else:
		least = a 
	
	for i in range(1, least+1):
		if a % i == 0 and b % i ==0:
			factors.append(i)
	return factors

print(common_factors(232, 64))
