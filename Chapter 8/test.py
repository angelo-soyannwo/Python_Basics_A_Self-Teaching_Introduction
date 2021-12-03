#update method
#find zero method
#division function
#approx_equal


def approx_eq(x, y, tolerance=1e-5):
	return abs(x-y) < tolerance

def update(x, f, df):
	x = x - f(x)/df(x)
	return x


def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess
		

def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	def newton_update(x):
		return update(x, f, df)
	return improve(newton_update, near_zero)

def nth_root(a, n):
	def f(x):
		return x**n - a
	def df(x):
		return n*pow(x, (n-1))
	return find_zero(f, df)


def golden_ratio():
	def golden_update(x):
		return (1/x) +1
	square_approx = lambda x: approx_eq(x**2, x+1)
	return improve(golden_update, square_approx)

def main():
	print(golden_ratio())



if __name__ == "__main__":
	main()
