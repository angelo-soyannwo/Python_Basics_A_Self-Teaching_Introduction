import math


def check_prime(x):
	half = (x + 2) * 0.5
	half = int(math.ceil(half))
	factor1 = 0
	factor2 = 0
	IsPrime = ''
	print(half)
	for i in range(2, half):
		temp =  x / i
		if x / math.floor(temp) == i:
			factor1 = i
			factor2 = temp
			IsPrime = 'False'
			print(temp)
			print(str(x) + ' is not a prime number and two of its factors are ' + str(factor1) + ' and ' + str(factor2))
			break
	if IsPrime != 'False':
		IsPrime = "True"
	
	if IsPrime == 'True':
		print(str(x) + " is Prime")

check_prime(8)

		
