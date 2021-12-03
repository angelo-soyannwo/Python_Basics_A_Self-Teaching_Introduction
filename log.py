import math


def find_solution(f, df, update, close, guess=1):
	"""
	Takes in an update method, an approximation method, and the initial guess.
	Returns the first value within the tolerance of the approximator.
	"""

	#Increments the solution until an approximate solution is found

	while not close(guess):
		guess = update(f, df, guess)
	return guess




def newton_update(function, derivative, x):
	x = x - function(x)/derivative(x)
	return x




def approx(value, target, precision=1e-9):
	"""
	takes in a value and calculates whether it approximately equals it's target within the specified precision (if none is specified, defaults to 10^-9). 
	"""
	#abs == absolute value
	return abs(value - target) < precision




def ln(n):
	"""
	Takes in a number n and returns x - the power to which e must be raised to get n.
	"""

	def f(x):
	#Raise n to the power of x and calculate the difference 
		return n - math.exp(x)

	def df(x):
		return -math.exp(x)

	def near_zero(x):
		#Checks how close our f(x) is to zero
		return approx(f(x), 0)

	return find_solution(f, df, newton_update, near_zero)


def log(a, b):
	"""
	Takes in two numbers a and b and returns x - the power to which a must be raised to get b.
	"""
	def f(x):
		return b - a**x

	def df(x):
		return -x*a**(x-1)

	def near_zero(x):
		#Checks how close our f(x) is to zero
		return approx(f(x), 0)

	return find_solution(f, df, newton_update, near_zero)


print('ln(5) is : ' + str(ln(5)))
print('log base 3 of 9 is: ' + str(log(3, 9)))

