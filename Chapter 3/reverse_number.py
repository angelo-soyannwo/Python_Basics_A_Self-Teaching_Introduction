
number = int(input("Enter your number: "))

def number_of_digits(a):
	no_digits  = 0
	copy = a
	while copy > 0:
		copy = copy // 10
		no_digits = no_digits + 1
	return no_digits

def reverse(a):
	store = []
	digits = number_of_digits(a)
	for i in range(0, (digits)):
		store.append(str(a%10))
		a = a // 10

	reverse_number = ''

	for i in range(0, (digits)):
		reverse_number += store[i]
	return reverse_number
	
print(reverse(number))
