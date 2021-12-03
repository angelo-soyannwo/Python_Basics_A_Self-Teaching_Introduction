
def is_palindrome(x):
	if x == "":
		return True
	elif len(x) == 1:
		return True

	if x[0] == x[-1]:
		return is_palindrome(x[1:-1])
	else:
		 return False

print(is_palindrome("racecar"))
