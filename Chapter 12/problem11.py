
class irr:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def __add__(self, other):
		return (self.a + other.a + self.c * self.b **0.5 + other.c * other.b **0.5)

	def __sub__(self,other):
		return (self.a - other.a + self.c * self.b **0.5 - other.c * other.b **0.5)
		

	def __idd__(self,other):
		self.a += other.a
		self.c = 

	def __mul__(self, factor):
		self.a *= factor
		self.c *= factor
def main():


if __name__ == '__main__':
	main()
