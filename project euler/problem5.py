
#only check multiples of 19 and 20 
#start at 380, increment by 380


def solution():
	current = 380
	result = 0
	while True:
		for i in range(2,21):
			if  current % i != 0:
				current += 380
				break
		else:
			result = current

		if result != 0:
			break
	return result


def main():
	print(solution())

if __name__ == '__main__':
	main()
