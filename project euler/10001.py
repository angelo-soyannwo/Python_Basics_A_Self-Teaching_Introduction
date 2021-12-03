
def is_prime(num):
	if num == 0:
		return False
	elif num == 1:
		return False
	for i in range(2, int(num/2)+2):
		if num%i == 0:
			return False
	return True

i=1
n = 1
result = 1
while i < 10001:
	if is_prime(n):
		result = n
		i+=1
	n += 1
print(result)
