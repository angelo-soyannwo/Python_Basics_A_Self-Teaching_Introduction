

def pythagorean_check(a, b):
	c_squared = a**2 + b**2
	if c_squared**0.5 == int(c_squared**0.5):
		return True
	return False

#print(pythagorean_check(8, 7))
sample_space = []
for i in range(1, 1000):
	for j in range(1, 1000):
		if pythagorean_check(i, j):
			sample_space += [(i, j,(i**2 + j**2)**0.5 )]

def is_special_triple(a, b, c):
	return a+b+c == 1000

for sample in sample_space:
	if is_special_triple(sample[0], sample[1], sample[2]):
		print(sample[0] * sample[1] * sample[2])
		break
	
