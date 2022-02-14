

class date:
	def __init__(self, day, month, year):
		self.day = day
		self.mm = month
		self.year = year

	def __add__(self, other):
		result = date()
		result.day = self.day + other.day
		result.mm = (self.month + other.month)%12
		result.year = self.year + other.year

def main():


if __name__ == '__main__':
	main()
