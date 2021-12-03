from math import log

c = int(input("Enter concentration: "))

PH = log(c, 10)

if PH < 7:
	print("the solution is acidic")
elif PH == 7:	
	print("the solution is neutral")
else:
	print("the solution is basic")

