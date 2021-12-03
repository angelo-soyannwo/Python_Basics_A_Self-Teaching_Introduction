def is_prime(x):
	half = x+1 // 2
	check = ""
	for i in range(2, half):
		if x%i == 0:
			check = "False"
	if check == "False":
		return False
	if check != "False":
		return True

def primes(n):
	if n == 0 or n ==1:
		yield 0
	elif n == 2:
		yield 2
	else:
		for i in range(2, n+1):
				if is_prime(i):
					yield i
t = primes(15)
for i in t:
	print(i)
