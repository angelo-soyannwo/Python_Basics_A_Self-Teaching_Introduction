
def harmonic(a, d, n):
	for i in range(n):
		yield (1/(a + (i*d)))

t = harmonic(1, 1, 5)
for i in t:
	print(i)
