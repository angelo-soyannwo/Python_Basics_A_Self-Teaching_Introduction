


def add_rationals(x, y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx*dy + ny*dx, dx*dy)


def numer(x):
	"""Returns the numerator of a real number passed in as a tuple or array containing two numbers"""
	return x[0]

def denom(x):
	"""Returns the denominator of a real number passed in as a tuple or array containing two numbers"""
	return x[1]

def mul_rationals(x, y):
	"""Returns the product of two rational numbers"""
	return (numer(x) * numer(y), denom(x) * denom(y))

def rational(x, y):
	def gcd(a, b):
		if a > b:
			lower = b
			higher = a
		else:
			lower = a
			higher = b
		g = 1
		while lower < higher:
			if b%lower == 0 and a%lower == 0:
				g = lower
			lower += 1
		return g

	g = gcd(x, y)
	return (x//g, y//g)


def pair(x, y):
	def get(index):
		if index == 0:
			return x
		elif index == 1:
			return y
		else:
			return print("index can 0nly be \'0\' or \'1\'")
	return get


def select(p, i):
	return p(i)

def main():
	half = rational(1, 2)
	third = rational(3, 4)

	t = pair(1, 4)
	select(t, 0)


if __name__ == "__main__":
	main()
