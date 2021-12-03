def factorial(n):
	result = 1
	for i in range(2, n+1):
		result *= i
	return result

def main():
#for an NxN grid, there are we must travel N units Right and N units Down
#1x1 = RD, DR
#Once we place down all of the Right units, the Downs units are given
#For this problem we just need to firgure out how many different combinations of N can be made from 2N elements

	gridsize = 20
	paths = 1

	answer = factorial(gridsize*2) / (factorial(gridsize) * factorial(2*gridsize-gridsize))
	print(answer)

if __name__ == '__main__':
	main()
