import math

numbers = input("Enter your numbers in the form: x1, x2, x3, ..., xn: \t")
data = list(map(int, numbers.split(", ")))

def all_zeros(iter):
	all_zeros = ""
	n = len(iter)
	for i in range(n):
		if iter[i] != 0:
			all_zeros = "False"
			return False
			break

	if all_zeros != "False":
		all_zeros = "True"
	
	if all_zeros == "True":
		
		return True


def common_factor(iter):
	
	least = iter[0]
	CF = 0
	n = len(iter)
	temp = []
	for i in range(n):
		if iter[i] < least:
			least = iter[i]

	for i in range(1, least + 1):
		for j in range(n):
			temp.append(iter[j] % i)
		if all_zeros(temp):
			CF = i
		temp = []
	return CF

if all_zeros(data):
	print("The common factor of numbers is 0")
else:
	print("The common factor of the numbers is ", end=" ")
	print(common_factor(data))


