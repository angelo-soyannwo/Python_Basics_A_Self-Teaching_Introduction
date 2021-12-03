
def gp(a, r, n):
	for i in range(n):
		yield a * r**i

t = gp(1, 0.5, 5)
for i in t:
	print(i)
