

def sumNatural(a):

	if a <= 1:
		return 0

	return sumNatural(a-1) + a

print(sumNatural(5))
