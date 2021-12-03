

a = int(input("Please enter the first number:\t"))
b = int(input("Please enter the second number:\t")) 

copy = a

for i in range(1, a*b):
	a = a * copy
	
print(a)
