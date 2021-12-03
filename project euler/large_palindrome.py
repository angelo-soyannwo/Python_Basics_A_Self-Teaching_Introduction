def count_digits(num):
	if num == 0:
		return 1
	digits = 0
	while num > 0:
		num //= 10
		digits += 1
	return digits
		
def is_palindrome(num):
	"""
	checks if a number is a palindrome
	"""
	store = 0
	copy = num
	digits = count_digits(num)
	for i in range(digits+1):
		store += (num%10) * 1* 10**(digits-(i+1))
		num //= 10
	if store == copy:
		return True
	else:
		return False

result = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		if is_palindrome(i*j) and i*j > result:
			result = i*j
print(result)

