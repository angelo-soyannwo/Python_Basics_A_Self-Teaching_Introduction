

class nat_currency:
	def __init__(self, value=None):
		self.value = value

	def __add__(self, other):
		result = nat_currency()
		result = self.value + other.value
		return result

	def __sub__(self, other):
		result = nat_currency()
		result = self.value - other.value
		return result

	def __idd__(self, other):
		self.value = self.value + other.value

	def __mul__(self, factor):
		self.value *= factor

def main():
	a = nat_currency(5)
	b = nat_currency(6)
	c = nat_currency()
	c.value = a + b
	print(c.value)	

if __name__ == '__main__':
	main()
