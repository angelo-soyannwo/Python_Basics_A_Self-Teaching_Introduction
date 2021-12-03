

def merge_lists(a , b):
	if type(a) == list and type(b) == list:
		return a + b
	else:
		return "They are not both lists"

print(merge_lists([1, 2], [3, 4]))

