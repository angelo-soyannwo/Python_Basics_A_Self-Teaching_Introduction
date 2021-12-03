import math

a = 16
b = 15

LCM = 0
i = 1

if a == b:
	print("the LCM is ", + str(a))

while LCM == 0:

	temp1 = i/a
	temp2 = i/b
	if math.floor(temp1) * a == i and  math.floor(temp2) * b == i:
		LCM = i
		break
	else:
		i += 1

print("the lcm is " + str(LCM))
