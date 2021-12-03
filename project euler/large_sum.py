def main():
	file = open('numbers.txt', 'r')
	numbs = file.read()
	numbs= numbs.split('\n')
	numbs.pop(-1)
	file.close()
	numbs = list(map(int, numbs))
	summation = sum(numbs)
	print(summation) 

if __name__ == '__main__':
	main()
