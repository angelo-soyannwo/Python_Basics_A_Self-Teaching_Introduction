
r = open("test.txt", "r")
s = r.read()
for i in s:
	print("Character ", i, "ascii value:\t", ord(i))
r.close()
