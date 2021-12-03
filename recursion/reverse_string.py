
def reverse_string(x):
	if x == "":
		return ""
	return reverse_string(x[1:]) + x[0]

print(reverse_string("hello"))
