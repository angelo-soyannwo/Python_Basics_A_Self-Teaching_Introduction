
def max():
	n = int(input("Enter the number of numbers to be entered:\t"))

	var_holder = {}

	for i in range(n):
		var_holder["var_" + str(i)] = int(input("Please enter a number:\t"))

	locals().update
	maximum = var_holder['var_0']

	for i in range(n):
		if int(var_holder['var_' + str(i)]) > int(maximum):
			maximum = int(var_holder['var_' + str(i)])
	return maximum

print(max())

