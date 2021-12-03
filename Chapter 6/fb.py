
def fib(x):
	if x == 1 or x == 0:
		return x
	else:
		return fib(x-1) + fib(x-2)

def fibonacci(n):
	for i in range(n):
		yield fib(i)

t = fibonacci(18)
for x in t:
	print(x)
