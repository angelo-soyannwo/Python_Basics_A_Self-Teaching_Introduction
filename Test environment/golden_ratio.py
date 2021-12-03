

def average(x, y):
	return (x + y) / 2

def approx_eq(x, y, tolerance=1e-15):
	return abs(x - y) < tolerance

def square_close_to_successor(guess):
	return approx_eq(guess**2, guess + 1)

def update(guess):
	return (1/guess) + 1

def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess
		

def main():
	phi = improve(update, square_close_to_successor)
	print(phi)
if __name__ == "__main__":
	main()
