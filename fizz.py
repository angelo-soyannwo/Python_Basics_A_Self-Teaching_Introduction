import random
import numpy as np



def solution1():
	for i in range(100):
		if i == 0:
			print(i, end=',')
			continue
		if i%3 == 0:
			print('Buzz', end=',')
		elif i%5 == 0:
			print('Fizz', end=',')
		elif i%15 == 0:
			print('Fizzbuzz', end=',')
		else:
			print(i, end=',')
		if i == 99:
			print()


def solution2():
	for i in range(1, 101):
		print('Fizz'*(i%3<1)+(i%5<1)*'Buzz' or i, end=', ')

def bubSort(array):
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i] < array[j]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return array	

def main():
	t = [random.randint(1, 100) for i in range(10)]
	a = np.arrange(s5)
	print(a)


if __name__ == "__main__":
	main()
