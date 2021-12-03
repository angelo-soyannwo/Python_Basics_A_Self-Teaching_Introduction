

def divisors(n):
	return [1] + [i for i in range(2, n) if n%i == 0]

def pairs():
	pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]	
	for x, y in pairs:
		print("x: ", str(x), end=" | ")
		print("y: ", str(y))


def is_perfect(n):
	x = divisors(n)
	sum = 0
	for i in x:
		sum += i
	if sum == n:
		return True
	else: 
		return False


def main():
	result = [i for i in range(1, 1000) if is_perfect(i)]
	print(result)

if __name__ == "__main__":
	main()
