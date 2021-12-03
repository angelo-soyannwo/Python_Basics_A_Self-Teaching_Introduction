
print("Enter text, press \"\\e\" to exit")
L = []

i = 1
in1 = input("Line number " + str(i) + ": ")
while in1 != "\e":
	L.append(in1)
	i += 1
	in1 = input("Line number " + str(i) + ": ")

print(L)

f = open("file1.txt", "w")
for i in range(len(L)):
	f.write(L[i])
f.close()

f = open("file1.txt", "r")
for i in f.readline():
	print(f.readline(i))
f.close()


