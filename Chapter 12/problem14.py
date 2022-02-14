


class vector:
	def __init__(self, x=None, y=None, z=None):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, other):
		result = vector()
		result.x = self.x + other.x
		result.y = self.y + other.y
		result.x = self.y + other.y
		return result
		
	def __sub__(self, other):
		result = vector()
		result.x = self.x - other.x
		result.y = self.y - other.y
		result.x = self.y - other.y
		return result

	def __idd__(self, other):
		self.x = self.x + other.x
		self.y = self.y + other.y
		self.x = self.y + other.y


def main():


if __name__ == '__main__':
	main()
