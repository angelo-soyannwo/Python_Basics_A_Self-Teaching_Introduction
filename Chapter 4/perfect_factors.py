import math

def factors_of(x):
	initial = []
	initial.append(x)
	half =int(math.ceil( x + 1 / 2))
	for i in range(1, half):
		temp = x / i
		if x / math.floor(temp) == i:
			initial.append(i)	
	factors = set(initial)
	return factors

def perfect_square(x):
	half = int(math.ceil( x + 1 / 2))
	is_perfect = ""
	square_root = 0
	for i in range(half):
		if i * i == x:
			is_perfect = "True"
			square_root = i
			print(str(x) + " is a perfect square and it's square root is " + str(i))
			break

	if is_perfect != "True":
			is_perfect = "False"

	if is_perfect == "False":
		print(str(x) + " is not a perfect square.")


print(factors_of(16))

perfect_square(16)
 

		
