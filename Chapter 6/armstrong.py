

def count_digits(x):
	i = 0
	while x > 0:
		x //= 10
		i += 1
	return i

def is_armstrong(x):
	n = count_digits(x)
	copy = x
	store = 0
	for i in range(n):
		store += (x%10)**n
		x //= 10
	if store == copy:
		return True
	else:
		return False

def armstrongs(n):
	for i in range(n):
		if is_armstrong(i):
			yield i

t = armstrongs(2000)
for x in t:
	print(x)
