
def ap(a, d, n):
	for i in range(n):
		yield a + i*d

x = ap(1, 1, 5)

for i in x:
	print(i, end=", ")
