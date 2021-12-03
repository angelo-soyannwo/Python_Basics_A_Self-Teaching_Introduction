

a = 20
b = 30

if a > b:
	least = b
else:
	least = a

HCF = 1

for i in range(1, least + 1):
	if a % i == 0 and b % i == 0:
		HCF = i

print(HCF)
