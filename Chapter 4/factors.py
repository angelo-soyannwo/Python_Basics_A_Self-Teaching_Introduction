import math

x = 44

half = int(math.ceil(x + 1 /2))

initial =  []

for i in range(1, half):
	temp = x / i
	if math.floor(x / temp) == i:
		initial.append(i)

factors = set(initial)

print(factors)
