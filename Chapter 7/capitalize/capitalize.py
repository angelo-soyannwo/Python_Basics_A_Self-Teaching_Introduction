
r = open("capitalize.txt", "r+")

data = r.readlines()
capitalized = []

for i in data:
	x = i.split()
	t = ""
	j = 0
	while j < len(x):
		x[j] = x[j].capitalize()
		t += x[j]
		j += 1
		t += " "
		
	capitalized += [t]
r.close()
r = open("capitalize.txt", "w")

for i in capitalized:
	r.write(i)
	r.write("\n")
