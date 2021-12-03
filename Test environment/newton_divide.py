
def approx_eq(x, y, tolerance=1e-5):
	return abs(x-y) < tolerance

def newton_update(f, df):
	def update(x):
		return x - f(x)/df(x)
	return update

def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess

def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(newton_update(f, df), near_zero)


def raph(f, df, guess=0.6, tolerance=1e-6):
	while abs(f(guess)-0) > tolerance:
		guess = guess - f(guess) / df(guess)	
	return guess

def d_b(a, b):
	def f(x):
		return a*(x**-1) - b
	def df(x):	
		return -a/x**2
	return raph(f, df)



def main():
	result = d_b(345, 5)
	print(result)


if __name__ == "__main__":
	main()
