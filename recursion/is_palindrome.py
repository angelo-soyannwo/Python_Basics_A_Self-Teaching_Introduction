

def is_palindrome(x):

	if len(x) == 0 or len(x) == 1:
		return True

	if x[0] == x[-1]:
		return is_palindrome(x[1: -1])

	return False

print(is_palindrome("racecar"))

