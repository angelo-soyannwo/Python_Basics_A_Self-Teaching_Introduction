from math import sqrt

def is_triple(x):
	if type(x) == int:
		for i in range(x):
			for j in range(x):
				if i**2 + j**2 == x**2:
					return (i, j, x)
	else:
		return None

def pythagorean_triples(n):
	if n < 4:
		return 0
	else:
		for i in range(n):
			d = is_triple(i)
			if type(d) == tuple:
				yield d

t = pythagorean_triples(20)
for x in t:
	print(x)

