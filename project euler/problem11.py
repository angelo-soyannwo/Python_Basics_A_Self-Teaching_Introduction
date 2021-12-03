file = open('grid.txt', 'r')
data = file.read().split()
data = [int(i) for i in data]

grid = [data[i:i+20] for i in range(0, 400, 20)]

def column_4_product(grid):
	"""
	finds the largest product of 4 adjacent number in a column
	"""
	answer = 0
	for i in range(20):
		for j in range(len(grid)-3):
			temp = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
			if answer < temp:
				answer = temp
	return answer


def row_4_product(grid):
	"""
	finds the largest product of 4 adjacent number in a row
	"""
	answer = 0
	for i in range(20):
		for j in range(len(grid)-3):
			temp = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
			if answer < temp:
				answer = temp
	return answer


def left_diagonal_product(grid):
	answer = 0
	for i in range(17):
		for j in range(17):
			temp = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2]* grid[i+3][j+3]
			if answer < temp:
				answer = temp
	return answer

def right_diagonal_product(grid):
	answer = 0
	for i in range(16, -1, -1):
		for j in range(19, 2, -1):
			temp = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2]* grid[i+3][j-3]
			if answer < temp:
				answer = temp
	return answer


#	for j in range(17):
#		temp = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2]* grid[i-3][j+3]
#		sub.append(temp)
#	return max(sub)

def main():
	print(column_4_product(grid))
	print(row_4_product(grid))
	print(left_diagonal_product(grid))
	print(right_diagonal_product(grid))

if __name__ == '__main__':
	main()
