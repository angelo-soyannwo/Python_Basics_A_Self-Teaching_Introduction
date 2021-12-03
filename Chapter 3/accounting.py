tax = 0
taxable_income = 0 

salary = int(input("Enter your salary: "))

TRA = salary * 0.1
HRA = salary * 0.2

gross_income = TRA + HRA + salary

if gross_income >  300000:
	print("gross income is greater than $300000")
else:
	print("gross income is less than $300000")

#tax allowance
if salary < 12570:
	print("No taxable income")
elif 12570 < salary < 50270:
	taxable_income = salary - 12570
	tax  = taxable_income * 0.2
elif 50271 < salary < 150000:
	taxable_income = salary - 50271
	tax  = taxable_income * 0.4
else:
	taxable_income = salary - 150000
	tax  = taxable_income * 0.45

print(tax)

