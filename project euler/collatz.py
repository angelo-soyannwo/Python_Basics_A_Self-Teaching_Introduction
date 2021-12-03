
def collatzSteps(start):
	if start == 0 or start == 1:
		return 0
	count = 0
	current_num = start
	while current_num != 1:
		if current_num%2 ==0:
			current_num /= 2
			count += 1
		else:
			current_num = current_num * 3 + 1
			count += 1
	return count


def main():
	result = 0
	steps = 0
	for i in range(3, 10**6):
		temp = collatzSteps(i)
		if temp > steps:
			steps = temp
			result = i
	print(result)

if __name__ == '__main__':
	main()
