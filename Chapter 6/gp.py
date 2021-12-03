

def gp(a, r, n):
	if n == 0:
		yield 0
	elif n == 1:
		yield a
	else:
		for i in range(n):
			yield a * r**i

x = gp(2, 2, 4)

for i in x:
	print(i, end=", ")


