
def multiples(x, n):
	if x > n or 2*x > n:
		return None
	else:
		i = 1
		result = 0
		while result + x < n:
			result = x * i
			i += 1
			yield result

t = multiples(6, 50)
for i in t:
	print(i)
		
