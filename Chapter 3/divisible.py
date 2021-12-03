
number = int(input("enter number: "))

a = number % 3
b = number % 13

print(b)

if a == 0 and b == 0:
	print("the number is divisible by 3 and 13")
elif b == 0:
	print("the number is divisible by 13")
elif a == 0:
	print("the number is divisible by 3")
else:
	print("the number is divisible by niether 3 nor 13")


