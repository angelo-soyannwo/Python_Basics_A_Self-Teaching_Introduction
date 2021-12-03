
def main():
	file = open('p18.txt', 'r')
	lines = file.read()
	lines = lines.split('\n')

	for i in range(len(lines)):
		lines[i] = lines[i].split()
	lines.pop()
	sum = 0
	for j in range(len(lines-2, 1,  -1)):
		for k in range(len(lines[j-1], 1, -1)):
			lines[j] = list(map(int, lines[j]))

	t = lines.index(max(lines[-1]))
	for q in range(len(lines-2, 1,  -1)):
		for k in range(len(lines[q-1], 1, -1)):	
			lines[q][t] += max(lines())

	max(lines[j])
	print(sum)

if __name__ == '__main__':
	main()
