
n = int(input("Enter the number of numbers to be entered: "))

var_holder = {}

for i in range(n):
	var_holder["var_" + str(i)] = input("Enter a number:\t")

locals().update

min = int(var_holder['var_0'])

for i in range(n):
	if int(var_holder["var_" + str(i)]) < min:
		min = int(var_holder["var_" + str(i)])

print(min)


