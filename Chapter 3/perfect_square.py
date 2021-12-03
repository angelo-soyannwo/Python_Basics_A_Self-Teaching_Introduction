import math

def is_perfect_square(x):

	half = x + 1 / 2
	half = math.ceil(half) 
	is_perfect = ''
	b = 0
	for i in range(0, int(half)):
		if i*i == x:
			b = i
			is_perfect = "True"
			
	if is_perfect == "True":
		print(str(x) + " is a perfect square and it's square root is " + str(b))
	else:
		print(str(x) + " is not a perfect square")


is_perfect_square(4)
