
def is_prime(n):
	if n == 0:
		return False
	elif n == 1:
		return False
	for i in range(2, int(n/2)+1):
		if n%i == 0:
			return False
	return True

def isprime(n):
	if n == 1:
		return False
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True




def main():
	sum = 0
	for i in range(2000000):
		if isprime(i):
			sum += i
	print(sum)


if __name__ == '__main__':
	main()


#define prime check
# use a for loop to get the sum
