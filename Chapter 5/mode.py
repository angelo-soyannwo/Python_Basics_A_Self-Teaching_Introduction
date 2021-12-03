

def mode():
	numbers = input("Please enter the numbers in the form, x1, x2, x3:\t")
	data = list(map(int, numbers.split(", ")))
	n = len(data)

	result = [data[0]]
	
	max_count = 0

	for i in range(n):
		var_count = 0
		for j in range(n):
			if data[i] == data[j]:
				var_count += 1
		if var_count > max_count:
			max_count = var_count
			result.pop()
			result.append(data[i])
		elif var_count == max_count:
			result.append(data[i]) 
	return set(result)

print(mode())
	
