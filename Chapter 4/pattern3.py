

n = int(input("Enter the number of rows:\t"))

for i in range(1, n+1):
	for j in range(1, n-i):
		print(" ", end="")
	for k in range(0, (2*i-1)):
		print("*", end = "")
	print()
