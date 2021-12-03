





def approx_eq(x, y, tolerance=1e-4):
	return abs(x - y) < tolerance

def newton_update(f, df, x0):
	x0 = x0 - f(x0) / df(x0)
	return x0 

def improve(f, df, close, guess=1):
	while not close(guess):
		guess = newton_update(f, df, guess)
	return guess


def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(f, df, near_zero)

def nth_root(a, n=2):
	def f(x):
		return x**n - a
	def df(x):
		return n * x ** (n-1)
	return find_zero(f, df)


def main():
	print(nth_root(16))


if __name__ == "__main__":
	main()
