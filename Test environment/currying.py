


def curried_pow(x):
	def h(y):
		return pow(x, y)
	return h

def map_to_range(function, start, end):
	while start < end:
		print(function(start))
		start += 1

def curry2(f):
	def g(x):
		def h(y):
			return pow(x, y)
		return h
	return g
	
def uncurry2(f):
	

def main():
	print(map_to_range(curried_pow(2), 0, 10))


if __name__ == "__main__":
	main()
