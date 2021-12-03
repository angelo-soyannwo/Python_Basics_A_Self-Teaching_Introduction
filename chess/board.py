

Class Chess_piece:
	def __innit__(self, suit):
		self.pos = []
		self.suit = suit
	def move(self, new_position=[0, 0]):
		self.pos[0] += newposition[0]
		self.pos[1] += newposition[1]

Class Pawn(chess_piece):
	def __innit__(self, position):
		self.pos = position
		self.movement = [1, 0]
		self.attack_right = [1, 1]
		self.attack_left = [1, -1]
		self.character = "P"

	def pawn_move(movement_vector):
		move(movement_vector)

def move_piece


def gen_grid():
	"""Generates a 8x8 matrix with the initial positions of chess pieces"""
	x = [["R", "Kn", "B", "Q", "K", "R", "Kn", "B"], ["P" for i in range(8)]]
	x += [["." for i in range(8)] for j in range(4)] + [["P" for i in range(8)], ["R", "Kn", "B", "Q", "K", "R", "Kn", "B"]]
	return x

def print_grid(grid):
	"""Prints the individual elements in the grid"""
	for i in grid:
		for j in i:
			print(j, end=" ")
		print()
def main():
	chess_board = gen_grid()
	print_grid(chess_board)


if __name__ == "__main__":
	main()
