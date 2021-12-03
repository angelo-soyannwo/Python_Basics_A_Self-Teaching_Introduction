

def fibonacci(n):
	if n == 2:
		return 1
	elif n == 1:
		return 1

	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fib_sequence(n):
	sequence_terms = []
	for i in range(1, n+1):
		sequence_terms.append(fibonacci(i))

	for i in range(n):
		print(sequence_terms[i])

fib_sequence(10)
