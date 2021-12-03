

def reverse(x):
	
	if x == '':
		return ""
	elif len(x) == 1:
		return x
	else:
		return reverse(x[1:]) + x[0]

print(reverse("123456"))
