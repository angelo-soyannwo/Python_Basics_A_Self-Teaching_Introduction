

f = open("test.txt", "r")
r = f.readlines()

lines = []

for i in r:
	lines.append(i.split())

#Store occurrence of each unique string
strings =  []

for i in lines:
	for j in range(len(i)):
		if i[j] in strings:
			continue
		else:
			strings.append(i[j])

#Same as above but in one line
sets = list(set([i[j] for i in lines for j in range(len(i))]))


tracker = [[] for i in range(len(strings))]

for i in strings:
	pos = strings.index(i)

	for j in range(len(lines)):
		n = len(lines[j])

		for c in range(n):
			if lines[j][c] == i:
				tracker[pos].append((j, c))

for i in strings:
	pos = strings.index(i)

	print("\"" + i + "\"" + " appears at:")
	n = len(tracker[pos])
	for c in range(n):
			print("line ", tracker[pos][c][0], " in position ", tracker[pos][c][1] )


f.close()
