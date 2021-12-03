number = input("Enter a four digit number: ")


if len(number) != 4:
	number = input("Please enter a four digit number: ")
else:
	n = int(number)
	unit = n %10
	ten = (n // 10) % 10
	hundred = (n // 100) %10
	thousand = (n // 1000) %10
	
	if unit + thousand == ten + hundred:
		print("unit + thousand = ten + hundred:")
		if ten < 9:
			ten += 1
		elif (ten == 9) and (hundred < 9): 
			hundred += 1
		number = unit + 10*ten + hundred*100 + 1000*thousand
		print(number)
	else:
 		print('unit + thousand != ten + hundred:')
