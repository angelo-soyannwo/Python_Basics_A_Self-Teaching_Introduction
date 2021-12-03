



def sum_n(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return sum_n(n-1) + n


def sum_digits(a):
	if a == 0:
		return 0
	elif a % 10 == 0:
		return a
	else:
		return sum_digits(a//10) + a%10


def fact(n):
	if n == 0:
		return n
	elif n == 1:
		return n
	else:
		return n * fact(n-1)


def is_even(n):
	if n == 0:
		return True
	else:
		return is_odd(n-1)

def is_odd(n):
	if n == 0:
		return False
	else:
		return is_even(n-1)


def cascade(n):
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n//10)
		print(n)


def perm(string):
	print(string)
	if string == "":
		print("")
		return string
	elif len(string) == 1:
		return string
	else:
		a = string[0]
		b = string[1:]
		print(b + a)
		return perm(b) + a



def main():
	perm("abc")



if __name__ == "__main__":
	main()
